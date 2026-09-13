import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
from build import ROOT, PAGES, inline, markdown

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.h1 = 0
    def handle_starttag(self, tag, attrs):
        if tag == 'h1':
            self.h1 += 1
        for key, value in attrs:
            if key in ('href', 'src'):
                self.links.append(value)

class BuildTests(unittest.TestCase):
    def test_markup_escaping(self):
        self.assertEqual(inline('<script>alert(1)</script>'), '&lt;script&gt;alert(1)&lt;/script&gt;')
        with self.assertRaises(ValueError):
            inline('[unsafe](javascript:alert)')
        self.assertIn('&quot;', inline('[safe](https://example.com/"x)'))

    def test_list_closes_before_heading(self):
        self.assertIn('</ul>\n<h2>', markdown('- one\n- two\n\n## Next'))

    def test_generated_pages_and_downloads(self):
        output = ROOT / 'docs'
        self.assertEqual(len(list(output.rglob('*.html'))), len(PAGES) + 1)
        for path in output.rglob('*.html'):
            parser = Links()
            parser.feed(path.read_text(encoding='utf-8'))
            self.assertEqual(parser.h1, 1, str(path))
            for link in parser.links:
                url = urlsplit(link)
                if url.scheme or not url.path:
                    continue
                target = (path.parent / unquote(url.path)).resolve()
                self.assertTrue(target.is_relative_to(output.resolve()), link)
                self.assertTrue(target.exists(), f'{path}: {link}')
        for slug, *_ in PAGES:
            self.assertEqual((ROOT / 'resumes' / f'{slug}.md').read_bytes(),
                             (output / slug / 'resume.md').read_bytes())

    def test_public_output_contains_only_delivery_files(self):
        allowed = {'index.html', '.nojekyll', 'assets/style.css', 'assets/print.js'}
        for slug, *_ in PAGES:
            allowed.update({f'{slug}/index.html', f'{slug}/resume.md'})
        actual = {str(p.relative_to(ROOT / 'docs')) for p in (ROOT / 'docs').rglob('*') if p.is_file()}
        self.assertEqual(actual, allowed)
        for page in (ROOT / 'docs').rglob('*.html'):
            content = page.read_text(encoding='utf-8')
            for private_marker in ('Interview-notes', '/Users/', 'job_documents', '待確認', 'hunter'):
                self.assertNotIn(private_marker, content)

if __name__ == '__main__':
    unittest.main()
