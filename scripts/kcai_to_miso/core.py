import re, glob, os
from kindmap import kind_of
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
def read(p): return open(os.path.join(REPO, p), encoding='utf-8').read()
def fence(text, lang=''):
    assert '````' not in text, 'nested 4-backtick fence'
    return '````%s\n%s%s````\n' % (lang, text, '' if text.endswith('\n') else '\n')
def parse_traces():
    out = []
    for f in sorted(glob.glob(os.path.join(REPO, 'knowledge', '*.md'))):
        if f.endswith('README.md'): continue
        s = open(f, encoding='utf-8').read()
        m = re.match(r'---\n(.*?)\n---\n(.*)\Z', s, re.S)
        fm, body = m.group(1), m.group(2)
        g = lambda k: (re.search(r'^%s:\s*(.*)$' % k, fm, re.M) or [None, ''])[1].strip()
        t = dict(path=os.path.relpath(f, REPO), id=g('id'), title=g('title'), status=g('status'), verified_how=g('verified_how'),
                 dataset_rev=g('dataset_rev'), as_of=g('as_of'), updated=g('updated'), reviewed_by=g('reviewed_by'), fm_raw=fm, body=body)
        rel = re.search(r'^related:\s*\[(.*)\]\s*$', fm, re.M)
        t['related'] = [x.strip() for x in rel.group(1).split(',') if x.strip()] if rel else []
        t['kind'] = kind_of(t['id'])
        out.append(t)
    return out
def parse_sources():
    rows = []
    for ln in read('SOURCES.md').split('\n'):
        if ln.startswith('| ') and not ln.startswith('| id') and not ln.startswith('|---'):
            c = [x.strip() for x in ln.strip().strip('|').split(' | ')]
            if len(c) >= 6: rows.append(dict(id=c[0], publisher=c[1], title=c[2], url=c[3], version=c[4], fetched=c[5]))
    return rows
def vp(t): return '/%s/%s' % (t['kind'], t['id'])
def render_trace(t, idpath):
    st = ['# ' + vp(t), '- status: stated%s' % (', derived' if t['kind'] == 'syntheses' or '解釈' in t['body'] else ''),
          '- kcai-status: %s' % (t['status'] or 'draft'), '- human-review: %s' % ('none' if t['reviewed_by'] in ('[]', '') else t['reviewed_by']),
          '- verified-how: %s' % t['verified_how'], '- origin-file: %s' % t['path'], '- title: %s' % t['title']]
    if t['dataset_rev']: st.append('- dataset-rev: %s' % t['dataset_rev'])
    if t['as_of']: st.append('- as_of: %s' % t['as_of'])
    st.append('- updated: %s' % t['updated'])
    src = []
    if t['verified_how'] in ('searched-undocs', 'mixed'): src.append('/sources/un-docs')
    if t['verified_how'] in ('read-official', 'mixed'): src.append('/sources/undocs-site')
    if src: st.append('- source: %s' % ', '.join(src))
    rel = [idpath[x] for x in t['related'] if x in idpath]
    if rel: st.append('- related: %s' % ', '.join(rel))
    st += ['', '<!-- kcai front matter (verbatim) -->', fence(t['fm_raw'] + '\n', 'yaml').rstrip('\n'), '']
    return '\n'.join(st) + '\n' + t['body'].rstrip('\n') + '\n\n'
def render_source(r, users):
    return '\n'.join(['# /sources/%s' % r['id'], '- status: stated', '- publisher: %s' % r['publisher'], '- title: %s' % r['title'],
        '- url: %s' % r['url'], '- version: %s' % r['version'], '- fetched_at: %s' % r['fetched'],
        '- rights: 出典自体の権利は発行者に従う。本文は転載せず、要約と出典の提示にとどめる',
        '- cited-by: %s' % (', '.join(users) if users else '(個別の踏み跡の front matter からは機械的に引けない)'), '']) + '\n'
def render_original(path_id, relpath, note='', kind='system-record'):
    return '# /%s/%s\n- status: stated\n- origin-file: %s\n- 備考: %s\n\n%s\n' % (kind, path_id, relpath, note or '原文のまま(4つのバッククォートの囲みの中が原文)。', fence(read(relpath), 'markdown'))
