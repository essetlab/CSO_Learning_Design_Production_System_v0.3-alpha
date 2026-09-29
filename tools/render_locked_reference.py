#!/usr/bin/env python3
from pathlib import Path
from string import Template
import argparse, html, json
ROOT=Path(__file__).resolve().parents[1]
def e(v): return html.escape(str(v),quote=True)
def links(items,kind):
    if kind=='style': return '\n'.join(f'  <link rel="stylesheet" href="{e(x)}">' for x in items)
    return '\n'.join(f'  <script src="{e(x)}"></script>' for x in items)
def menu_html(items): return ''.join(f'<a href="{e(x["href"])}">{e(x["label"])}</a>' for x in items)
def load_spec(path):
    p=Path(path); p=p if p.is_absolute() else ROOT/p
    return json.loads(p.read_text(encoding='utf-8'))
def render_gr01(spec):
    t=Template((ROOT/'templates/course-entry/structure.html').read_text(encoding='utf-8'))
    c=spec['content']; shell=spec['shell']; asset=spec['asset']; pf=c['practice_focus']; j=c['journey']; q=c['question_thread']; close=c['close']
    qitems=''.join(f'<li>{e(x)}</li>' for x in q['items'])
    jitems=''.join(f'<li><span class="journey__number">{e(x["number"])}</span><strong>{e(x["title"])}</strong><span>{e(x["body"])}</span></li>' for x in j['items'])
    pitems=''.join(f'<label class="focus-row"><input name="practice-focus" type="radio" value="{e(x["value"])}"/><span aria-hidden="true" class="focus-row__number">{e(x["number"])}</span><span class="focus-row__text">{e(x["label"])}</span><span aria-hidden="true" class="focus-row__mark">↗</span></label>' for x in pf['options'])
    return t.substitute(document_title=e(c['document_title']),style_links=links(spec['locked_dependencies']['styles'],'style'),shell_variant=e(shell['variant']),skip_label=e(shell['skip_label']),course_title=e(shell['course_title']),course_context=e(shell['course_context']),progress_label=e(shell['progress_label']),progress_percent=e(shell['progress_percent']),drawer_eyebrow=e(shell['drawer_eyebrow']),menu_links=menu_html(shell['menu']),vertical_marker=e(c['vertical_marker']),eyebrow=e(c['eyebrow']),course_name=e(c['course_name']),headline_html=f'{e(c["headline"]["first_line"])}<br/><em>{e(c["headline"]["emphasis_line"])}</em>',proposition=e(c['proposition']),context_line=e(c['context_line']),primary_href=e(c['primary_href']),primary_cta=e(c['primary_cta']),secondary_href=e(c['secondary_href']),secondary_action=e(c['secondary_action']),hero_alt=e(asset['alt']),hero_height=e(asset['height']),hero_width=e(asset['width']),hero_src=e(asset['src']),question_thread_aria=e(q['aria_label']),question_thread_intro=e(q['intro']),question_thread_items=qitems,chapter_number=e(c['chapter']['number']),chapter_label=e(c['chapter']['label']),journey_kicker=e(j['kicker']),journey_heading=e(j['heading']),journey_intro=e(j['intro']),journey_items=jitems,practice_kicker=e(pf['kicker']),practice_heading=e(pf['heading']),practice_support=e(pf['support']),practice_legend=e(pf['legend']),practice_storage_key=e(pf['storage_key']),practice_items=pitems,practice_empty_status=e(pf['empty_status']),practice_clear_label=e(pf['clear_label']),close_aria=e(close['aria_label']),close_kicker=e(close['kicker']),close_heading=e(close['heading']),close_body=e(close['body']),script_links=links(spec['locked_dependencies']['scripts'],'script'))
def render_gr04(spec):
    t=Template((ROOT/'templates/scenario/structure.html').read_text(encoding='utf-8'))
    c=spec['content']; shell=spec['shell']; ev=c['evidence']; d=c['decision']; tw=c['takeaway']; beh=spec['behavior']
    eitems=''.join(f'<li><span class="evidence-list__index" aria-hidden="true">{e(x["number"])}</span><div><strong>{e(x["title"])}</strong><p>{e(x["body"])}</p></div></li>' for x in ev['items'])
    opts=''.join(f'<label class="option-row option-row--lettered" data-option="{e(x["id"])}" data-option-row="{e(x["id"])}"><input name="decision-choice" type="radio" value="{e(x["id"])}"/><span aria-hidden="true" class="option-row__letter">{e(x["id"])}</span><span class="option-row__content"><span>{e(x["text"])}</span></span></label>' for x in d['options'])
    responses={x['id']:{'state':x['state'],'rowState':x['row_state'],'label':x['feedback_label'],'title':x['feedback_title'],'body':x['feedback_body']} for x in d['options']}
    pitems=''.join(f'<li><span>{e(x)}</span></li>' for x in tw['path'])
    return t.substitute(document_title=e(c['document_title']),style_links=links(spec['locked_dependencies']['styles'],'style'),shell_variant=e(shell['variant']),skip_label=e(shell['skip_label']),course_title=e(shell['course_title']),course_context=e(shell['course_context']),progress_label=e(shell['progress_label']),progress_percent=e(shell['progress_percent']),drawer_eyebrow=e(shell['drawer_eyebrow']),menu_links=menu_html(shell['menu']),eyebrow=e(c['eyebrow']),heading=e(c['heading']),lead=e(c['lead']),stage_aria=e(c['stage_aria']),evidence_kicker=e(ev['kicker']),evidence_heading=e(ev['heading']),evidence_intro=e(ev['intro']),evidence_list_aria=e(ev['list_aria']),evidence_items=eitems,evidence_cue_html=ev['cue_html'],decision_kicker=e(d['kicker']),learner_question=e(d['learner_question']),decision_legend=e(d['legend']),decision_options=opts,review_button=e(d['review_button']),clear_button=e(d['clear_button']),responses_json=json.dumps(responses,ensure_ascii=False),reasoning_label=e(d['reasoning_label']),reasoning_body=e(d['reasoning_body']),revise_button=e(d['revise_button']),takeaway_kicker=e(tw['kicker']),takeaway_heading=e(tw['heading']),takeaway_body=e(tw['body']),path_aria=e(tw['path_aria']),path_items=pitems,initial_completion_status=e(beh['initial_completion_status']),complete_status=e(beh['complete_status']),qa_complete_value=e(d['strongest_option']),revise_status=e(beh['revise_status']),script_links=links(spec['locked_dependencies']['scripts'],'script'))
def render_spec(spec):
    if spec['reference_id']=='GR-01': return render_gr01(spec)
    if spec['reference_id']=='GR-04': return render_gr04(spec)
    raise ValueError('Unsupported locked reference '+spec['reference_id'])
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('spec'); ap.add_argument('--output',required=True); a=ap.parse_args()
    spec=load_spec(a.spec); out=Path(a.output); out=out if out.is_absolute() else ROOT/out; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(render_spec(spec).strip()+'\n',encoding='utf-8'); print(out)
if __name__=='__main__': main()
