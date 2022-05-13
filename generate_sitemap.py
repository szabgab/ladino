import os

xml = []
for dirname, dirs, files in os.walk('docs'):
    for filename in files:
        if filename.endswith('md'):
            if filename == 'index.md':
                if dirname == 'docs':
                    xml.append(f'<url><loc>https://ladino.szabgab.com/{dirname[5:]}</loc></url>')
                else:
                    xml.append(f'<url><loc>https://ladino.szabgab.com/{dirname[5:]}/</loc></url>')
            else:
                xml.append(f'<url><loc>https://ladino.szabgab.com/{dirname[5:]}/{filename[0:-3]}</loc></url>')
xml.append('<url><loc>https://ladino.szabgab.com/wordle/</loc><lastmod>2022-05-12T07:30:41+00:00</lastmod></url>')

xml.sort()

xml.insert(0, '<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
xml.insert(0, '<?xml version="1.0" encoding="UTF-8"?>')
xml.append('</urlset>')

with open('docs/sitemap.xml', 'w') as fh:
    for line in xml:
        print(line, file=fh)

