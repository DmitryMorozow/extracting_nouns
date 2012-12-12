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

class NounDef(object):
    def __init__(self, word, gender, animacy, inflection, props):
        self.word = word
        if gender:
            self.gender = gender.strip()
        else:
            self.gender = gender
        if animacy and animacy.strip() == 'a':
            self.animacy = True
        elif animacy and animacy.strip() == 'ina':
            self.animacy = False
        else:
            logging.warning("Bad anymacy '{}' for {}".format(animacy, word))
            self.animacy = None
        if inflection:
            self.inflection = inflection.strip()
        else:
            self.inflection = inflection
        self.props = props

    def __str__(self):
        return "{}: ({}, {}, {}), {}".format(
            self.word, self.gender, self.getAnimacyRepr(self.animacy), self.inflection,
            repr(self.props)
        )
    @classmethod
    def getAnimacyRepr(cls, animacy):
        if animacy:
            return "a"
        elif animacy is None:
            return "-"
        else:
            return "ina"

    @classmethod
    def findall(cls, word, text):
        defStartRe = re.compile("{{сущ\s+ru(?=\s|\||}})", re.S | re.M)
        basePropRe = re.compile("\s*(?:(\w+)(?:\s+([\w-]+)(?:\s+([\w\d\(][^\n\|}]*))?)?)?", re.S)
        propRe = re.compile("\s*\|([\w\d-]+)\s*=\s*((?:{{(?:[^}]*)}}|[^{}\|])*)", re.S)
        defs = []
        for m in defStartRe.finditer(text):
            gm = basePropRe.match(text, m.end())
            if not gm:
                logging.warning("unable to get gender,animacy,inflection for '{}'".format(word))
                baseProps = (None, None, None)
            else:
                baseProps = gm.groups()
                if None in baseProps:
                    logging.warning("unable to get some of props for '{}': {}".format(word, baseProps))
		    # do some magic for человек
                    if baseProps[2] is None:
                        if baseProps[1] and baseProps[1].strip() == 'a-люди':
                            baseProps = (baseProps[0], None, baseProps[1])
   
            pos = gm.end()
            props = {}
            pm = propRe.match(text, gm.end())
            while pm:
                props[pm.group(1)] = pm.group(2).strip()
                pos = pm.end()
                pm = propRe.match(text, pm.end())

            if not text[pos:].lstrip().startswith("}}"):
                logging.warning("Some unparsed data in '{}' for {}".format(text[m.start():pos+10], word))
            defs.append(NounDef(word, baseProps[0], baseProps[1], baseProps[2], props))
        return defs
    
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
    defs = NounDef.findall(title, text[0].text)
    if not defs:
        return True # no Russian nouns found
    for d in defs:
        print ("{0}, {1}, {2}, {3}".format(
            d.word, d.gender or '-', d.getAnimacyRepr(d.animacy), d.inflection or '-'
        )) 
        logging.warning("processing forms for {}".format(d))
        getWordForms(d.word, d.gender, d.animacy, d.inflection, **d.props)
    return True

out = open('titles.xml', 'w')
context = etree.iterparse('ruwiktionary-latest-pages-articles.xml', events=('end',))

fast_iter(context, extract_page)
