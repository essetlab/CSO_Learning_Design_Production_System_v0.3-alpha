"""Registry references and build authority for specs and frozen contracts."""
from pathlib import Path
import json,re
from jsonschema import Draft202012Validator

OBJECT_TOKEN=re.compile(r'\b(?:SHELL|UI|BLK|INT|CMP|TPL|IP|PRA|SVC|AST)-[A-Z0-9-]+-\d{2}\b')
SCALARS={'component':'components','component_id':'components','interaction':'interactions','interaction_id':'interactions','learning_block':'blocks','learning_block_id':'blocks','composition':'compositions','composition_id':'compositions','instructional_pattern':'patterns','supporting_pattern':'patterns','pattern_id':'patterns','template':'templates','template_id':'templates','owner_candidate':'components'}
LISTS={'components':'components','component_ids':'components','learning_blocks':'blocks','learning_block_ids':'blocks','interactions':'interactions','interaction_ids':'interactions','patterns':'patterns','instructional_patterns':'patterns','templates':'templates','compositions':'compositions','shared_ui':'components','required_existing_objects':'all','reuse':'all','adapt_proposed':'all'}

def load_registries(root):
    groups={}
    errors=[]
    import yaml
    seen=set()
    for name in ['components','compositions','patterns','templates']:
        data=json.loads((root/f'registries/{name}.json').read_text(encoding='utf-8'))
        items=data['objects'];ids=[o['id'] for o in items]
        if len(ids)!=len(set(ids)):errors.append(f'registries/{name}: duplicate IDs')
        if seen.intersection(ids):errors.append(f'registries/{name}: ID duplicated across registry kinds')
        seen.update(ids)
        mirror=root/f'registries/{name}.yaml'
        if not mirror.is_file() or yaml.safe_load(mirror.read_text(encoding='utf-8'))!=data:errors.append(f'registries/{name}: JSON/YAML mismatch')
        groups[name]={o['id']:o for o in items}
    assets=json.loads((root/'registries/assets.json').read_text(encoding='utf-8'))
    if yaml.safe_load((root/'registries/assets.yaml').read_text(encoding='utf-8'))!=assets:errors.append('registries/assets: JSON/YAML mismatch')
    groups['assets']={o['id']:o for o in assets['assets']}
    groups['blocks']={k:v for k,v in groups['components'].items() if k.startswith('BLK-')}
    groups['interactions']={k:v for k,v in groups['components'].items() if k.startswith('INT-')}
    groups['all']={k:v for group in groups.values() for k,v in group.items()}
    return groups,errors

def validate_references(document,groups,policy,source):
    errors=[];aliases=[]
    def error(path,message):errors.append(f'{path or "$"}: {message}')
    def reference(value,group,path):
        if not isinstance(value,str) or not value:
            error(path,'reference must be a nonempty registered ID');return
        alias=policy['dependency_aliases'].get(value)
        if alias and source==alias['document'] and path==alias['pointer'] and alias['owner'] in groups['components']:
            aliases.append(dict(source=source,pointer=path,label=value,owner=alias['owner']));return
        if value not in groups[group]:error(path,f'unknown {group} reference {value}')
    def variant(obj,key,group,path):
        ref=obj.get(key);id=ref.get('id') if isinstance(ref,dict) else ref
        declared=ref.get('variant') if isinstance(ref,dict) else obj.get(key+'_variant')
        if isinstance(ref,dict):reference(id,group,path+'/'+key+'/id')
        if (isinstance(ref,dict) and 'variant' in ref) or key+'_variant' in obj:
            if not isinstance(declared,str) or not isinstance(id,str) or id not in groups[group] or declared not in groups[group][id].get('variants',[]):error(path+'/'+key+'_variant',f'unknown {key} variant {declared} for {id}')
        if isinstance(ref,dict) and key+'_variant' in obj and obj[key+'_variant']!=ref.get('variant'):
            error(path+'/'+key+'_variant','conflicting variant declarations')
    def authority(value,path):
        if isinstance(value,str):
            if value not in policy['authority_levels']:error(path,'unsupported authority mode '+value)
        elif isinstance(value,dict):
            if not value:error(path,'authority declaration must not be empty')
            for k,v in value.items():
                if isinstance(v,list):
                    if k not in policy['authority_levels'] or not all(isinstance(x,str) and x.strip() for x in v):error(path+'/'+k,'unsupported authority level or malformed authority statements')
                elif not isinstance(v,str) or v not in policy['authority_levels']+policy['restriction_modes']:error(path+'/'+k,'unsupported authority/restriction mode')
        else:error(path,'authority must declare supported modes')
    def walk(obj,path=''):
        if isinstance(obj,dict):
            for kind in ['template','composition']:
                if kind in obj or kind+'_variant' in obj:variant(obj,kind,kind+'s',path)
            for key,value in obj.items():
                p=path+'/'+key
                if key=='build_mode' and value not in policy['supported_build_modes']:error(p,f'unsupported build mode {value}')
                # These two frozen fields are source citations, not build-mode declarations.
                citation=(source,p) in {
                    ('prototype-specs/GR-03_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json','/content_limits/authority'),
                    ('prototype-specs/GR-06_AUTHORING_CONTENT_STATE_CONTRACT_v0.1.json','/human_semantic_validation/authority')}
                if key=='authority_mode' or (key=='authority' and not citation):authority(value,p)
                if key in SCALARS:
                    if key=='instructional_pattern' and isinstance(value,dict):
                        for role in ['primary','supporting']:
                            if role in value:reference(value[role],'patterns',p+'/'+role)
                    elif key not in ['composition','template'] or not isinstance(value,dict):reference(value,SCALARS[key],p)
                elif key in LISTS:
                    if not isinstance(value,list):error(p,'references must be an array')
                    else:
                        for i,item in enumerate(value):reference(item,LISTS[key],p+'/'+str(i))
                elif key=='id' and ('/proposed_shared_candidates/' in path or '/new_unregistered_proposals/' in path):reference(value,'all',p)
                elif isinstance(value,str):
                    for token in OBJECT_TOKEN.findall(value):reference(token,'all',p)
                walk(value,p)
        elif isinstance(obj,list):
            for i,value in enumerate(obj):
                p=path+'/'+str(i)
                if isinstance(value,str):
                    for token in OBJECT_TOKEN.findall(value):reference(token,'all',p)
                else:walk(value,p)
    walk(document)
    return sorted(set(errors)),aliases

def validate_future_brief(spec,root,policy,source):
    errors=[]
    if spec.get('id') not in policy['existing_reference_exemptions']:
        for field in policy['future_required_fields']:
            if field not in spec:errors.append(f'{source}: future reference requires {field}')
    if 'experience_differentiation_brief' not in spec:return errors
    ref=spec['experience_differentiation_brief']
    if not isinstance(ref,str):return errors+[f'{source}: experience_differentiation_brief must be a repository-relative path']
    path=(root/ref).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():return errors+[f'{source}: missing/outside-repository differentiation brief {ref}']
    try:
        brief=json.loads(path.read_text(encoding='utf-8'));schema=json.loads((root/'schemas/experience-differentiation-brief.schema.json').read_text(encoding='utf-8'))
        errors += [f'{ref}: {e.message}' for e in Draft202012Validator(schema).iter_errors(brief)]
        if brief.get('reference')!=spec.get('id'):errors.append(f'{ref}: reference ID mismatch')
    except (ValueError,OSError) as e:errors.append(f'{source}: invalid brief: {e}')
    return errors
