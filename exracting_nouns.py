from lxml import etree
import re
import logging

from modifying_nouns import getWordForms

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
    if not text or not text[0].text or not title or not title[0].text:
        return True
    title = title[0].text
    if title.startswith("Викисловарь:") or title.startswith("Wiktionary:") or title.startswith("Шаблон:"):
        # no need to process this pages
        return True 
    # ===\s*Морфологические\s*и\s*синтаксические\s*свойства\s*===\s*
    pos = text[0].text.find("{{сущ ru") 
    if pos == -1:
        return True
    pattern = "{{сущ ru([^}]*)}}"
    # \s+(\S+)\s+(\S+)\s+([\d\*\w\(\)\?^°'-]*)\n*.*?\|основа\d*\s*=\s*([^|\n\s]*)
    good = False
    for m in re.finditer(pattern, text[0].text, re.S | re.M):
        descr = m.group(1).strip()
        if not descr:
            logging.warning("empty description for " + title)
            continue
        info = descr.split('|')
        if info[0].strip().startswith("-old"):
            continue
        infoPattern = "(\S+)\s+(\S+)(?:\s+(.*))?"
        im = re.match(infoPattern, info[0].strip())
        if not im:
            logging.warning("info '{}' for '{}' not parsed".format(info[0].strip(), title))
            continue
        good = True
        gender = im.group(1)
        if im.group(2) == 'a':
            animacy = True
        elif im.group(2) == 'ina':
            animacy = False
        else:
            logging.warning("Bad anymacy '{}' for {}".format(im.group(2), title))
            animacy = False
        inflection = im.group(3) if im.group(3) else ""
        
        print ("{0}, {1}, {2}, {3}".format(title, gender, animacy, inflection))
        kws = {}
        logging.warning("processing '{}'".format(descr))
        for i in info[1:]:
            r = i.split('=')
            if len(r) != 2:
                logging.warning("Unparsed '{}' for '{}'".format(i, title))
                continue
            kws[r[0].strip()] = r[1].strip()
        logging.warning("processing [{},{},{},{},{}]".format(title, gender, animacy, inflection, kws))
        getWordForms(title, gender, animacy, inflection, **kws)
    if not good:
        logging.warning("{0} not good".format(title))
    return True

out = open('titles.xml', 'w')
context = etree.iterparse('ruwiktionary-latest-pages-articles.xml', events=('end',))

fast_iter(context, extract_page)
