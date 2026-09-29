#!/usr/bin/env python3
"""Validate every Golden Reference YAML spec and the existing locked contracts."""
from pathlib import Path
import argparse, json
import yaml
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
try:
    from .validate_governance import load_registries, validate_references, validate_future_brief
except ImportError:
    from validate_governance import load_registries, validate_references, validate_future_brief


def validate_spec(spec, templates, validator):
    errors=[]
    for error in validator.iter_errors(spec):
        location='/'.join(str(part) for part in error.absolute_path) or '$'
        errors.append(f'{location}: {error.message}')
    if errors:
        return errors
    ref=spec['template']
    tid=ref if isinstance(ref,str) else ref['id']
    variant=ref.get('variant') if isinstance(ref,dict) else None
    if tid not in templates:
        errors.append(f'template: unknown template {tid}')
    elif variant is not None and variant not in templates[tid].get('variants',[]):
        errors.append(f'template/variant: unknown template variant {variant} for {tid}')
    return errors


def validate_repository(root=ROOT):
    def load(rel): return json.loads((root/rel).read_text(encoding='utf-8'))
    errors=[]
    try:
        policy=load('governance/validation-policy.json')
        groups,registry_errors=load_registries(root)
        errors.extend(registry_errors)
    except (OSError,ValueError,KeyError,TypeError) as e:
        return {'status':'fail','checked':[],'errors':[f'governance/registries: {e}']}
    resolved_aliases=[]; contract_paths=set()
    components={x['id'] for x in load('registries/components.json')['objects']}; comps={x['id'] for x in load('registries/compositions.json')['objects']}; pats={x['id'] for x in load('registries/patterns.json')['objects']}; tmpls={x['id']:x for x in load('registries/templates.json')['objects']}; assets={x['id']:x for x in load('registries/assets.json')['assets']}
    for rid in ('GR-01','GR-04'):
        spec=load(f'locked-build-specs/{rid}_LOCKED_BUILD_v0.1.json')
        ref_errors,aliases=validate_references(spec,groups,policy,f'locked-build-specs/{rid}_LOCKED_BUILD_v0.1.json')
        errors.extend(f'{rid}: {e}' for e in ref_errors)
        if spec.get('build_mode')!='LOCKED_BUILD': errors.append(f'{rid}: not LOCKED_BUILD')
        if spec.get('determinism')!='D3': errors.append(f'{rid}: not D3')
        if spec.get('instructional_pattern') not in pats: errors.append(f'{rid}: unknown pattern')
        if spec.get('composition') not in comps: errors.append(f'{rid}: unknown composition')
        t=spec.get('template',{}); tid=t.get('id'); variant=t.get('variant')
        if tid not in tmpls: errors.append(f'{rid}: unknown template {tid}')
        elif variant not in tmpls[tid].get('variants',[]): errors.append(f'{rid}: unknown template variant {variant}')
        sh=spec.get('shell',{}).get('id')
        if sh and sh not in components: errors.append(f'{rid}: unknown shell {sh}')
        for cid in spec.get('components',[]):
            if cid not in components: errors.append(f'{rid}: unknown component {cid}')
        asset=spec.get('asset')
        if asset:
            aid=asset.get('id')
            if aid not in assets: errors.append(f'{rid}: unknown asset {aid}')
            elif not (root/assets[aid]['path']).is_file(): errors.append(f'{rid}: asset file missing')
    schema=load('schemas/golden-reference.schema.json')
    Draft202012Validator.check_schema(schema)
    validator=Draft202012Validator(schema)
    checked=[]; legacy=[]
    for folder in sorted((root/'golden-references').iterdir()):
        if not folder.is_dir() or not (folder.name.startswith('GR-') or (folder/'spec.yaml').is_file()): continue
        rid=folder.name; checked.append(rid)
        try:
            spec=yaml.safe_load((folder/'spec.yaml').read_text(encoding='utf-8'))
        except (OSError,yaml.YAMLError) as error:
            errors.append(f'{rid}/spec.yaml: {error}')
            continue
        errors.extend(f'{rid}/spec.yaml: {error}' for error in validate_spec(spec,tmpls,validator))
        if isinstance(spec,dict):
            source=f'golden-references/{rid}/spec.yaml'
            if spec.get('id')!=rid:errors.append(f'{source}: id must match directory {rid}')
            ref_errors,aliases=validate_references(spec,groups,policy,source)
            errors.extend(f'{source}: {e}' for e in ref_errors)
            errors.extend(validate_future_brief(spec,root,policy,source))
            if isinstance(spec.get('template'),str):legacy.append(rid)
            if 'prototype_contract' in spec:
                ref=spec['prototype_contract']
                if not isinstance(ref,str):errors.append(f'{source}: prototype_contract must be a path')
                else:
                    path=(folder/ref).resolve()
                    if not path.is_relative_to(root.resolve()) or not path.is_file():errors.append(f'{source}: missing/outside-repository prototype_contract {ref}')
                    else:contract_paths.add(path)
    for path in (root/'prototype-specs').glob('*CONTRACT*.json'):
        try:
            c=json.loads(path.read_text(encoding='utf-8'))
            if c.get('contract',{}).get('status','').startswith('FROZEN'):contract_paths.add(path.resolve())
        except (ValueError,AttributeError) as e:errors.append(f'{path.relative_to(root)}: malformed contract: {e}')
    contracts_checked=[]
    for path in sorted(contract_paths):
        source=path.relative_to(root.resolve()).as_posix();contracts_checked.append(source)
        try:
            c=json.loads(path.read_text(encoding='utf-8'))
            if not isinstance(c,dict) or not c.get('contract',{}).get('status','').startswith('FROZEN'):errors.append(f'{source}: referenced contract is not frozen')
            ref_errors,aliases=validate_references(c,groups,policy,source)
            errors.extend(f'{source}: {e}' for e in ref_errors)
            for a in aliases:
                if a not in resolved_aliases:resolved_aliases.append(a)
        except (ValueError,AttributeError,TypeError) as e:errors.append(f'{source}: malformed contract: {e}')
    if not checked: errors.append('No Golden Reference specifications found')
    return {'status':'pass' if not errors else 'fail','checked':checked,
            'locked_checked':['GR-01','GR-04'],'schema':'schemas/golden-reference.schema.json',
            'legacy_template_strings':legacy,'contracts_checked':contracts_checked,'dependency_aliases':resolved_aliases,'external_python_packages_required':True,
            'python_packages':['PyYAML','jsonschema'],'errors':errors}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output'); args=ap.parse_args()
    result=validate_repository(); payload=json.dumps(result,indent=2)+'\n'; print(payload,end='')
    if args.output:
        output=Path(args.output); output=output if output.is_absolute() else ROOT/output
        output.parent.mkdir(parents=True,exist_ok=True); output.write_text(payload,encoding='utf-8')
    return 0 if not result['errors'] else 1


if __name__=='__main__':
    raise SystemExit(main())
