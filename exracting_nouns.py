from lxml import etree
import re
import logging

ns = 'http://www.mediawiki.org/xml/export-0.8/'

def fast_iter(context, func):
    for event, elem in context:
        if func(elem):
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]
    del context


def extract_page(elem):
    if elem.tag != '{' + ns + '}' + 'page':
        return False
    title = elem.xpath('t:title', namespaces={'t': ns})
    text = elem.xpath('t:revision/t:text', namespaces={'t': ns})
    if not text or not text[0].text:
        return True
    # ===\s*Морфологические\s*и\s*синтаксические\s*свойства\s*===\s*
    if text[0].text.find("{{сущ ru") == -1:
        return True
    pattern = "{{сущ ru\s+(\S+)\s+(\S+)\s+([\d\*\w\(\)\?^°'-]*)\n*.*?\|основа\d*\s*=\s*([^|\n\s]*)"
    good = False
    for m in re.finditer(pattern, text[0].text, re.S | re.M):
        good = True
        print ("{0}, {1}, {2}, {3}".format(title[0].text, m.group(1), m.group(2), m.group(3), m.group(4)))
    if not good:
        logging.warning("{0}".format(title[0].text))
    return True

out = open('titles.xml', 'w')
context = etree.iterparse('ruwiktionary-latest-pages-articles.xml', events=('end',))

fast_iter(context, extract_page)
