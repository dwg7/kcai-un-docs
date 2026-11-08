import sys as _sys
if '--force-migration' not in _sys.argv:
    _sys.exit('この道具は、kcai-un-docs の knowledge/(2026-11-08 時点の凍結した写し)から miso/un-docs.md を組み立てた移行の記録です。miso/un-docs.md が正本になったため、実行すると正本を上書きします(DECISIONS.md の 2026-11-08)。本当に再生成するなら --force-migration を付けてください。')
import os, collections, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core
from kindmap import KINDS
HERE = os.path.dirname(os.path.abspath(__file__))
VERSION = '0.1.0'; AS_OF = '2026-11-08'
OUT = os.path.join(core.REPO, 'miso', 'un-docs.md')
T = core.parse_traces(); S = core.parse_sources()
idpath = {t['id']: core.vp(t) for t in T}
def sec(n):
    p = os.path.join(HERE, 'sections', n)
    return open(p, encoding='utf-8').read().rstrip('\n') + '\n\n'
def gen_index():
    st = ['# /navigation/object-index', '- status: derived', '- scope: 踏み跡の id から仮想パスを引く索引(機械生成)', '']
    for k, n, _ in KINDS:
        st += ['## %s(%s)' % (k, n), '', '| id | 仮想パス | verified-how | 更新 | 題名 |', '|---|---|---|---|---|']
        for t in T:
            if t['kind'] == k: st.append('| `%s` | `%s` | %s | %s | %s |' % (t['id'], core.vp(t), t['verified_how'], t['updated'], t['title'].replace('|', '/')))
        st.append('')
    return '\n'.join(st) + '\n'
def gen_path_map():
    st = ['# /system-record/path-map', '- status: stated', '- scope: 元のリポジトリのファイルと、仮想パスの対応(機械生成)。`knowledge/README.md` の索引のリンク `<id>.md` は、ここで仮想パスに引ける', '', '| 元のファイル | 仮想パス |', '|---|---|']
    for t in T: st.append('| `%s` | `%s` |' % (t['path'], core.vp(t)))
    for a, b in (('README.md','/system-record/readme-original'),('knowledge/README.md','/system-record/knowledge-readme-original'),('AGENTS.md, CLAUDE.md','/system-record/agents-original'),('DECISIONS.md','/system-record/decision-log'),('QUESTIONS.md','/system-record/questions-original'),('SOURCES.md','/system-record/sources-ledger-original(個々の出典は `/sources/<id>`)'),('LICENSE','/system-record/license-original')):
        st.append('| `%s` | `%s` |' % (a, b))
    return '\n'.join(st) + '\n\n'
def gen_originals():
    p = [core.render_original('readme-original', 'README.md'), core.render_original('knowledge-readme-original', 'knowledge/README.md', '踏み跡の一覧(元の索引)。リンク先の `<id>.md` は `/system-record/path-map` で仮想パスに引く。原文のまま。'),
         '# /system-record/agents-original\n- status: stated\n- origin-file: AGENTS.md, CLAUDE.md\n- 備考: 移行前の作業指針。移行後の規則は `/system-record/agent-contract` が優先する(矛盾するときは agent-contract に従い、利用者に確認する)。\n\n## AGENTS.md\n\n' + core.fence(core.read('AGENTS.md'), 'markdown') + '\n## CLAUDE.md\n\n' + core.fence(core.read('CLAUDE.md'), 'markdown') + '\n',
         core.render_original('decision-log', 'DECISIONS.md', '判断の記録。追記のみで、既存の記録は削除しない。'),
         core.render_original('questions-original', 'QUESTIONS.md', '種の問いの台帳と、hfu への質問。'),
         core.render_original('sources-ledger-original', 'SOURCES.md', '出典台帳の原文の表(各行は `/sources/<id>` にも展開した)。'),
         core.render_original('license-original', 'LICENSE')]
    return ''.join(p)
def assemble():
    users = {}
    body = ''.join([sec('01_contract.md'), sec('02_instance.md'), gen_index(), '\n', sec('03_derived.md'),
        ''.join(core.render_trace(t, idpath) for k, _, _ in KINDS for t in T if t['kind'] == k),
        sec('05_tests.md'), sec('06_open.md'),
        ''.join(core.render_source(r, users.get(r['id'])) for r in S),
        '# /system-record/agent-contract-reminder\n- status: normative\n- 再掲: 更新したら、統合した正本の全文を `.md` の添付で返すこと(`/system-record/agent-contract`)。\n\n',
        gen_path_map(), gen_originals()])
    for ph, fn in (('{{MIGRATION_RECORD}}', '_migration_record.txt'), ('{{TEST_BACKLOG}}', '_test_backlog.txt')):
        p = os.path.join(HERE, 'sections', fn)
        body = body.replace(ph, open(p, encoding='utf-8').read().rstrip('\n') if os.path.exists(p) else '(未生成)')
    body = body.replace('{{VERSION}}', VERSION).replace('{{AS_OF}}', AS_OF).replace('{{N_TRACES}}', str(len(T)))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(body)
    print('wrote', OUT, len(body.encode('utf-8')), 'bytes', len(body), 'chars')
if __name__ == '__main__': assemble()
