"""Build static resume pages using only the Python standard library."""
from html import escape
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
PAGES = (
    ('general', 'Professional Profile', '綜合履歷', '後端開發、資料庫效能、認證整合與雲端部署的完整概覽。'),
    ('ideku-backend', 'Backend Engineering', '後端與產品開發', '高流量 API、金流串接、資料庫效能與 SaaS 交付。'),
    ('asus-oauth', 'Identity & Access', '認證與服務整合', 'Keycloak、OAuth 串接、JWT 生命週期與跨服務授權。'),
    ('asus-webrtc', 'Realtime Systems', '即時通訊與系統', 'Socket、WebSocket、非阻塞開發與系統可觀測性。'),
    ('asus-cloud-lead', 'Cloud Delivery', '雲端與跨專案交付', 'Kubernetes、多專案環境整合與開發流程改善。'),
)

def inline(value):
    """Render this project's limited Markdown. Escape HTML; allow safe link schemes."""
    pattern = r'\[([^\]\n]+)\]\(([^\s)]+)\)|\*\*([^*\n]+)\*\*'
    result, end = [], 0
    for match in re.finditer(pattern, value):
        result.append(escape(value[end:match.start()]))
        label, url, strong = match.groups()
        if strong is not None:
            result.append(f'<strong>{escape(strong)}</strong>')
        elif url.startswith(('https://', 'mailto:')):
            result.append(f'<a href="{escape(url, quote=True)}">{escape(label)}</a>')
        else:
            raise ValueError('Unsupported link scheme')
        end = match.end()
    result.append(escape(value[end:]))
    return ''.join(result)


def markdown(source):
    result, in_list = [], False
    for line in source.splitlines():
        if not line.strip():
            continue
        if not line.startswith('- ') and in_list:
            result.append('</ul>')
            in_list = False
        if line.startswith('- '):
            if not in_list:
                result.append('<ul>')
                in_list = True
            result.append(f'<li>{inline(line[2:])}</li>')
        elif match := re.match(r'^(#{1,3}) (.+)$', line):
            level, title = len(match[1]), inline(match[2])
            result.append(f'<h{level}>{title}</h{level}>')
        else:
            result.append(f'<p>{inline(line)}</p>')
    if in_list:
        result.append('</ul>')
    return '\n'.join(result)


def document(title, description, body, prefix='./'):
    return f'''<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{escape(description, quote=True)}">
<meta name="color-scheme" content="light">
<title>{escape(title)} · 蕭學鴻</title>
<link rel="stylesheet" href="{prefix}assets/style.css">
<script src="{prefix}assets/print.js" defer></script>
</head>
<body>
<a class="skip" href="#main">跳至主要內容</a>
{body}
</body>
</html>
'''


def build():
    output = ROOT / 'docs'
    (output / 'assets').mkdir(parents=True, exist_ok=True)
    for name in ('style.css', 'print.js'):
        shutil.copyfile(ROOT / 'assets' / name, output / 'assets' / name)
    (output / '.nojekyll').write_text('', encoding='utf-8')
    cards = []
    for number, (slug, english, title, description) in enumerate(PAGES, 1):
        source = (ROOT / 'resumes' / f'{slug}.md').read_text(encoding='utf-8')
        destination = output / slug
        destination.mkdir(exist_ok=True)
        (destination / 'resume.md').write_text(source, encoding='utf-8')
        body = f'''<header class="toolbar">
<a class="brand" href="../">蕭學鴻<span> / RESUME</span></a>
<nav aria-label="履歷工具"><a href="resume.md" download="{slug}.md">下載 Markdown</a><button type="button" data-print hidden>列印 / 存成 PDF</button></nav>
</header>
<main id="main" class="resume-shell">
<div class="edition"><span>{english}</span><span>RESUME / {number:02d}</span></div>
<article class="resume">{markdown(source)}</article>
</main>
<footer class="footer">蕭學鴻 <span>·</span> {title}</footer>'''
        (destination / 'index.html').write_text(document(title, description, body, '../'), encoding='utf-8')
        cards.append(f'''<a class="card" href="{slug}/"><span class="card-number">0{number}</span>
<div><p class="eyebrow">{english}</p><h2>{title}</h2><p>{description}</p></div><span class="arrow" aria-hidden="true">↗</span></a>''')
    home = '''<header class="toolbar"><a class="brand" href="./">蕭學鴻<span> / RESUME</span></a>
<nav aria-label="聯絡方式"><a href="mailto:henry255164@gmail.com">Email ↗</a><a href="https://www.linkedin.com/in/henry255164">LinkedIn ↗</a></nav></header>
<main id="main" class="home">
<section class="hero"><p class="eyebrow">SENIOR BACK-END ENGINEER · NEW TAIPEI</p>
<h1>讓服務穩定運作，<br>讓系統持續改善<span class="dot">。</span></h1>
<p class="intro">我是蕭學鴻。從高流量 API、資料庫調校，到認證整合與雲端部署，<br class="wide-only">我專注於釐清問題、完成交付，並讓既有系統更易於維護。</p>
</section>
<section class="versions" aria-labelledby="versions-title"><div class="section-label"><h2 id="versions-title">專業經歷</h2>'''+ f'<span>{len(PAGES):02d} RESUMES</span></div>\n' + '\n'.join(cards) + '''</section></main>
<footer class="footer">蕭學鴻 <span>·</span> Backend / Systems / Cloud</footer>'''
    (output / 'index.html').write_text(document('專業履歷', '蕭學鴻的後端開發、認證整合、即時通訊與雲端交付履歷。', home), encoding='utf-8')
    print(f'Built index + {len(PAGES)} resume pages in docs/')

if __name__ == '__main__':
    build()
