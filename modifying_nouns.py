import logging

from modifying_nouns_m import m_funcs
from modifying_nouns_f import f_funcs
from modifying_nouns_n import n_funcs

funcs = {
         'm': m_funcs,
         'f': f_funcs,
         'n': n_funcs
    }

def q_0(animacy, **b):
    inf = [[], []]
    inf[0].append(b['основа'])
    inf[0].append(b['основа'])
    inf[0].append(b['основа'])
    inf[0].append(b['основа'])
    inf[0].append(b['основа'])
    inf[0].append(b['основа'])
    inf[1].append(b['основа'])
    inf[1].append(b['основа'])
    inf[1].append(b['основа'])
    inf[1].append(b['основа'])
    inf[1].append(b['основа'])
    inf[1].append(b['основа'])
    return inf

funcs['m']['0'] = q_0
funcs['f']['0'] = q_0
funcs['n']['0'] = q_0

class FailCollector(object):
    def __init__(self):
        self.fails = {}
    def append(self, fail):
        if fail in self.fails:
            self.fails[fail] += 1
        else:
            self.fails[fail] = 1

    def get(self, descending = True):
        return self.fails.items()

    def getSorted(self, descending = True):
        return sorted(self.fails.items(), key = lambda x: x[1], reverse = descending)

failCollector = FailCollector()

def safeRun(word, f, *args, **kwargs):
    try:
        return f(*args, **kwargs)
    except KeyError:
        logging.error("not enough arguments to generate forms for {}: args={}, kwargs={}".format(word, args, kwargs))
        return None

def getWordForms(word, gender, animacy, inflection, **b):
    if gender in funcs:
        if inflection in funcs[gender]:
            # whoo-hoo!
            return safeRun(word, funcs[gender][inflection], animacy, **b)
        elif inflection and inflection.endswith('-') and inflection[:-1] in funcs[gender]:
            inf = safeRun(word, funcs[gender][inflection[:-1]], animacy, **b)
            if inf:
                inf[1] = [None, None, None, None, None, None]
            return inf
        elif inflection and inflection.startswith('(') and inflection.endswith(')') and inflection[1:-1] in funcs[gender]:
            inf = safeRun(word, funcs[gender][inflection[1:-1]], animacy, **b)
            if inf:
                inf[0] = [None, None, None, None, None, None]
            return inf
        else:
            failCollector.append((gender, animacy, inflection))
            logging.error("no function for {}: [{},{},{}]".format(word, gender, animacy, inflection))
            return None
    else:
        failCollector.append((gender, animacy, inflection))
        logging.error("bad gender for {}: [{},{},{}]".format(word, gender, animacy, inflection))
        return None
