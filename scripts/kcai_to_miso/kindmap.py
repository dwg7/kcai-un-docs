"""un-docs インスタンスの踏み跡の種別(仮想パスの第1区分)の割り当て。
先行例(survey-training)の対応表は使わず、このインスタンス用に作り直したもの。
種別:
  guides    … 読み方・記号・落とし穴・作業量の見立て(コーパスの読み方の踏み跡)
  searches  … コーパスに対する検索・集計・初出などの問いの踏み跡
  readings  … 個別の文書(S/PV、S/ 文書、決議など)を読んだ踏み跡
  syntheses … 複数の読みや検索をまたいで整理した踏み跡
"""
import re
KINDS = [
    ('guides', '読み方・記号・落とし穴', ''),
    ('searches', '検索・集計・初出の問い', ''),
    ('readings', '個別文書の読み', ''),
    ('syntheses', '複数の読みの整理', ''),
]
GUIDES = {'un-docs-reading-guide', 'un-document-symbols-primer', 'large-corpus-work-volume-versus-trace-yield', 'geospatial-search-terms'}
SYNTHESES = {
    'un-geospatial-institutions-in-un-docs', 'un-geospatial-organization-timeline', 'un-ggim-ecosoc-geospatial-institutional-arc',
    'un-operational-coordinate-formats', 'un-open-gis-initiative-member-state-links', 'un80-oict-ungsc-2026-changes-for-geospatial',
    'peace-operations-review-2026-implications-for-un-open-gis', 'state-positions-on-un-boundary-assistance',
    'member-state-statements-on-geospatial-japan-korea-italy-finland-us', 'unlb-gis-centre-proposal-2006-origin-and-considerations',
    'geospatial-themes-frameworks-conclusions', 'geospatial-geographic-tendency',
    'satellite-imagery-in-security-council-who-and-why', 'satellite-imagery-sessions-two-patterns-synthesis',
    'satellite-imagery-substitute-for-access-s-pv-readings', 'sage-access-and-who-sees-it', 'sage-and-unite-aware-relationship',
    'sage-in-security-council-discussions', 'sage-situational-awareness-geospatial-enterprise',
    'west-africa-2001-proposal-implementation-first-traces',
}
SEARCHES = {
    'geospatial-first-appearance', 'geospatial-activity-over-time', 'responsibility-to-protect-first-appearance',
    'keyword-human-security-in-un-docs', 'keyword-nexus-in-un-docs', 'keyword-agency-in-un-docs',
    'japan-statements-on-human-security-in-un-docs', 'agency-agentive-use-by-meeting-type-in-un-docs',
    'mission-budgets-geospatial-output-lines', 'outer-space-resolutions-geospatial-wording-2006-2025',
    'coordinate-grids-mgrs-utm-in-un-docs', 'first-and-latest-cartographer-appointments',
    'boundary-demarcation-un-cartographer-involvement-timeline', 'un-mission-gis-mentions-in-un-docs',
    'unlb-gis-function-in-budget-documents', 'satellite-imagery-claims-by-state-in-s-pv',
}
def kind_of(i):
    if i in GUIDES: return 'guides'
    if i in SYNTHESES: return 'syntheses'
    if i in SEARCHES: return 'searches'
    if re.match(r'^(s-pv-|s-20|a-res-|a-63-)', i): return 'readings'
    raise KeyError('未分類の踏み跡: ' + i)
