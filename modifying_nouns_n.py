n_funcs = {}

def q_n_1a(animacy, **b):
    # чадо, болото
    inf = [[], []]
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'ом')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'])
    inf[1].append(b['основа'] + 'ам')
    if animacy:
        inf[1].append(b['основа'])
    else:
        inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'] + 'ами')
    inf[1].append(b['основа'] + 'ах')
    # end pl
    return inf
n_funcs['1a'] = q_n_1a

# skip 1a-

def q_n_1aV(animacy, **b):
    # animacy unused
    # полено
    inf = [[], []]
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'ом')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа1'] + 'я')
    inf[1].append(b['основа1'] + 'ев')
    inf[1].append(b['основа1'] + 'ям')
    inf[1].append(b['основа1'] + 'я')
    inf[1].append(b['основа1'] + 'ями')
    inf[1].append(b['основа1'] + 'ях')
    # end pl
    return inf
n_funcs['1a^'] = q_n_1aV

def q_n_1aVi(animacy, **b):
    # animacy unused
    # колено. Единственное слово. Запредельная ненависть
    inf = [[], []]
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'ом')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа'] + 'и')
    inf[1].append(b['основа'] + 'ей')
    inf[1].append(b['основа'] + 'ям')
    inf[1].append(b['основа'] + 'и')
    inf[1].append(b['основа'] + 'ями')
    inf[1].append(b['основа'] + 'ях')
    # end pl
    return inf
n_funcs['1a^-и'] = q_n_1aVi

def q_n_1aVr(animacy, **b):
    # animacy unused
    # озеро. Единственное слово. Запредельная ненависть
    inf = [[], []]
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'ом')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа1'] + 'а')
    inf[1].append(b['основа1'])
    inf[1].append(b['основа1'] + 'ам')
    inf[1].append(b['основа1'] + 'а')
    inf[1].append(b['основа1'] + 'ами')
    inf[1].append(b['основа1'] + 'ах')
    # end pl
    return inf
n_funcs['1a^-р'] = q_n_1aVr

def q_n_1aV1(animacy, **b):
    # animacy unused
    # утро. Единственное слово. Неоднозначность ударения. Запредельная, зашкаливающая ненависть
    inf = [[], []]
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'ом')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'])
    inf[1].append(b['основа'] + 'ам')
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'] + 'ами')
    inf[1].append(b['основа'] + 'ах')
    # end pl
    return inf
n_funcs['1a^-1'] = q_n_1aV1

def q_n_1as(animacy, **b):
    # animacy unused
    # коромысло
    inf = [[], []]
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'ом')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа1'])
    inf[1].append(b['основа'] + 'ам')
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'] + 'ами')
    inf[1].append(b['основа'] + 'ах')
    # end pl
    return inf
n_funcs['1*a'] = q_n_1as

def q_n__1a_(animacy, **b):
    # animacy unused
    # коромысло
    inf = [[], []]
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    # end sg
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'])
    inf[1].append(b['основа'] + 'ам')
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'] + 'ами')
    inf[1].append(b['основа'] + 'ах')
    # end pl
    return inf
n_funcs['(1a)'] = q_n__1a_

def q_n__1aV_(animacy, **b):
    # animacy unused
    # Озёры. Одно слово. Ненависть.
    inf = [[], []]
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    # end sg
    inf[1].append(b['основа'] + 'ы')
    inf[1].append(b['основа'])
    inf[1].append(b['основа'] + 'ам')
    inf[1].append(b['основа'] + 'ы')
    inf[1].append(b['основа'] + 'ами')
    inf[1].append(b['основа'] + 'ах')
    # end pl
    return inf
n_funcs['(1a^)'] = q_n__1aV_

def q_n_1b(animacy, **b):
    # божество, вещество
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа'] + 'а́')
    inf[1].append(b['основа1'])
    inf[1].append(b['основа'] + 'а́м')
    if animacy:
        inf[1].append(b['основа1'])
    else:
        inf[1].append(b['основа'] + 'а́')
    inf[1].append(b['основа'] + 'а́ми')
    inf[1].append(b['основа'] + 'а́х')
    # end pl
    return inf
n_funcs['1b'] = q_n_1b

def q_n_1bV(animacy, **b):
    # animacy unused
    # мудо. Хм. К тому же, неоднозначность склонения.
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа1'] + 'и')
    inf[1].append(b['основа'] + 'е́й')
    inf[1].append(b['основа'] + 'я́м')
    inf[1].append(b['основа1'] + 'и')
    inf[1].append(b['основа'] + 'я́ми')
    inf[1].append(b['основа'] + 'я́х')
    # end pl
    return inf
n_funcs['1b^'] = q_n_1bV

# 1b- обрабатывается штатно

def q_n_1bs_(animacy, **b):
    # animacy unused
    # дно
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(None)  # *{{{основа}}}а́
    inf[1].append(None)  # *{{{основа1}}}
    inf[1].append(None)  # *{{{основа}}}а́м
    inf[1].append(None)  # *{{{основа}}}а́
    inf[1].append(None)  # *{{{основа}}}а́ми
    inf[1].append(None)  # *{{{основа}}}а́х
    # end pl
    return inf
n_funcs['1*b-'] = q_n_1bs_

def q_n_1bsV(animacy, **b):
    # animacy unused
    # зло. единственный пример в среднем роде
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(None)  # *{{{основа}}}а́
    inf[1].append(b['основа1'])
    inf[1].append(None)  # *{{{основа}}}а́м
    inf[1].append(None)  # *{{{основа}}}а́
    inf[1].append(None)  # *{{{основа}}}а́ми
    inf[1].append(None)  # *{{{основа}}}а́х
    # end pl
    return inf
n_funcs['1*b^'] = q_n_1bsV

def q_n__1b_(animacy, **b):
    # небеса
    inf = [[], []]
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    # end sg
    inf[1].append(b['основа'] + 'а́')
    inf[1].append(b['основа1'])
    inf[1].append(b['основа'] + 'а́м')
    if animacy:
        inf[1].append(b['основа1'])
    else:
        inf[1].append(b['основа'] + 'а́')
    inf[1].append(b['основа'] + 'а́ми')
    inf[1].append(b['основа'] + 'а́х')
    # end pl
    return inf
n_funcs['(1b)'] = q_n__1b_

def q_n_1c(animacy, **b):
    # animacy unused
    # место
    inf = [[], []]
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'ом')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа1'] + 'а́')
    inf[1].append(b['основа'])
    inf[1].append(b['основа1'] + 'а́м')
    inf[1].append(b['основа'] + 'а́')
    inf[1].append(b['основа'] + 'а́ми')
    inf[1].append(b['основа'] + 'а́х')
    # end pl
    return inf
n_funcs['1c'] = q_n_1c

def q_n_1cV(animacy, **b):
    # animacy unused
    # древо
    inf = [[], []]
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'ом')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа1'] + 'а́')
    inf[1].append(b['основа2'])
    inf[1].append(b['основа1'] + 'а́м')
    inf[1].append(b['основа1'] + 'а́')
    inf[1].append(b['основа1'] + 'а́ми')
    inf[1].append(b['основа1'] + 'а́х')
    # end pl
    return inf
n_funcs['1c^'] = q_n_1cV

# 1c- обрабатывается штатно

def q_n_1csV(animacy, **b):
    # animacy unused
    # масло. единственный пример в среднем роде
    inf = [[], []]
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'ом')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа1'] + 'а́')
    inf[1].append(b['основа2'])
    inf[1].append(b['основа1'] + 'а́м')
    inf[1].append(b['основа1'] + 'а́')
    inf[1].append(b['основа1'] + 'а́ми')
    inf[1].append(b['основа1'] + 'а́х')
    # end pl
    return inf
n_funcs['1*c^'] = q_n_1csV

def q_n_1d(animacy, **b):
    # animacy unused
    # вино
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа1'] + 'а')
    inf[1].append(b['основа1'])
    inf[1].append(b['основа1'] + 'ам')
    inf[1].append(b['основа1'] + 'а')
    inf[1].append(b['основа1'] + 'ами')
    inf[1].append(b['основа1'] + 'ах')
    # end pl
    return inf
n_funcs['1d'] = q_n_1d

def q_n_1dV(animacy, **b):
    # animacy unused
    # крыло
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа1'] + 'я')
    inf[1].append(b['основа1'] + 'ев')
    inf[1].append(b['основа1'] + 'ям')
    inf[1].append(b['основа1'] + 'я')
    inf[1].append(b['основа1'] + 'ями')
    inf[1].append(b['основа1'] + 'ях')
    # end pl
    return inf
n_funcs['1d^'] = q_n_1dV

# 1d- обрабатывается штатно

def q_n_1ds(animacy, **b):
    # animacy unused
    # колесо, гумно
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа1'] + 'а')
    inf[1].append(b['основа2'])
    inf[1].append(b['основа1'] + 'ам')
    inf[1].append(b['основа1'] + 'а')
    inf[1].append(b['основа1'] + 'ами')
    inf[1].append(b['основа1'] + 'ах')
    # end pl
    return inf
n_funcs['1*d'] = q_n_1ds
# гумно может склоняться по 1*d^, при этом правила те же, что и для 1*d, но другая основа2
q_b_1dsV = q_n_1ds

def q_n_1dsVS(animacy, **b):
    # animacy unused
    # дно/донья (в смысле, много днов 8-0. Запредельный уровень ненависти
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа1'] + 'ья')
    inf[1].append(b['основа1'] + 'ьев')
    inf[1].append(b['основа1'] + 'ьям')
    inf[1].append(b['основа1'] + 'ья')
    inf[1].append(b['основа1'] + 'ьями')
    inf[1].append(b['основа1'] + 'ьях')
    # end pl
    return inf
n_funcs['1*d^-ь'] = q_n_1dsVS

def q_n_1f(animacy, **b):
    # animacy unused
    # тавро
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа1'] + 'а')
    inf[1].append(b['основа1'])
    inf[1].append(b['основа'] + 'а́м')
    inf[1].append(b['основа1'] + 'а')
    inf[1].append(b['основа'] + 'а́ми')
    inf[1].append(b['основа'] + 'а́х')
    # end pl
    return inf
n_funcs['1f'] = q_n_1f

def q_n_2a(animacy, **b):
    # animacy unused
    # горе
    inf = [[], []]
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'я')
    inf[0].append(b['основа'] + 'ю')
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'ем')
    inf[0].append(b['основа'] + 'е')
    # end sg
    # likely, unused
    inf[1].append(b['основа'] + 'я')
    inf[1].append(b['основа'] + 'ь')
    inf[1].append(b['основа'] + 'ям')
    inf[1].append(b['основа'] + 'я')
    inf[1].append(b['основа'] + 'ями')
    inf[1].append(b['основа'] + 'ях')
    # end pl
    return inf
n_funcs['2a'] = q_n_2a

# 2a- обрабатывается штатно

def q_n_2c(animacy, **b):
    # animacy unused
    # поле
    inf = [[], []]
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'я')
    inf[0].append(b['основа'] + 'ю')
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'ем')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа1'] + 'я́')
    inf[1].append(b['основа1'] + 'е́й')
    inf[1].append(b['основа1'] + 'я́м')
    inf[1].append(b['основа1'] + 'я́')
    inf[1].append(b['основа1'] + 'я́ми')
    inf[1].append(b['основа1'] + 'я́х')
    # end pl
    return inf
n_funcs['2c'] = q_n_2c

# 2c- обрабатывается штатно

def q_n_3a(animacy, **b):
    # animacy unused
    # благо
    inf = [[], []]
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'ом')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'])
    inf[1].append(b['основа'] + 'ам')
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'] + 'ами')
    inf[1].append(b['основа'] + 'ах')
    # end pl
    return inf
n_funcs['3a'] = q_n_3a

# 3a(1), брюхо, полностью совпадает с q_n_3a
n_funcs['3a(1)'] = q_n_3a

# 3a(1)(2), колёсико, полностью совпадает с q_n_3a

n_funcs['3a(1)(2)'] = q_n_3a

def q_n_3as_1_(animacy, **b):
    # донышко
    inf = [[], []]
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'ом')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа'] + 'и')
    inf[1].append(b['основа1'])
    inf[1].append(b['основа'] + 'ам')
    if animacy:
        inf[1].append(b['основа1'])
    else:
        inf[1].append(b['основа'] + 'и')
    inf[1].append(b['основа'] + 'ами')
    inf[1].append(b['основа'] + 'ах')
    # end pl
    return inf
n_funcs['3*a(1)'] = q_n_3as_1_

def q_n_3as_1__2_(animacy, **b):
    # animacy unused
    # древко. Возможны различные ударения :/
    inf = [[], []]
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'ом')  # вариант b['основа1'] + 'о́м'
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа'] + 'и')
    inf[1].append(b['основа'] + 'ов')  # вариант b['основа1'] + 'о́в'
    inf[1].append(b['основа'] + 'ам')  # вариант b['основа1'] + 'а́м'
    inf[1].append(b['основа'] + 'и')
    inf[1].append(b['основа'] + 'ами')
    inf[1].append(b['основа'] + 'ах')
    # end pl
    return inf
n_funcs['3*a(1)(2)'] = q_n_3as_1__2_

def q_n_3bs_1__2_(animacy, **b):
    # animacy unused
    # ушко
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа'] + 'и́')
    inf[1].append(b['основа'] + 'о́в')  # вариант b['основа1'] + 'о́в'
    inf[1].append(b['основа'] + 'а́м')  # вариант b['основа1'] + 'а́м'
    inf[1].append(b['основа'] + 'и́')
    inf[1].append(b['основа'] + 'а́ми')
    inf[1].append(b['основа'] + 'а́х')
    # end pl
    return inf
n_funcs['3*b(1)(2)'] = q_n_3bs_1__2_

def q_n_3c(animacy, **b):
    # animacy unused
    # войско
    inf = [[], []]
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'ом')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа1'] + 'а́')
    inf[1].append(b['основа'])
    inf[1].append(b['основа1'] + 'а́м')
    inf[1].append(b['основа1'] + 'а́')
    inf[1].append(b['основа1'] + 'а́ми')
    inf[1].append(b['основа1'] + 'а́х')
    # end pl
    return inf
n_funcs['3c'] = q_n_3c

def q_n_3c_2_(animacy, **b):
    # animacy unused
    # облако. 1 слово. Ненависть.
    inf = [[], []]
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'ом')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа1'] + 'а́')
    inf[1].append(b['основа1'] + 'о́в')
    inf[1].append(b['основа1'] + 'а́м')
    inf[1].append(b['основа1'] + 'а́')
    inf[1].append(b['основа1'] + 'а́ми')
    inf[1].append(b['основа1'] + 'а́х')
    # end pl
    return inf
n_funcs['3c(2)'] = q_n_3c_2_

# 3*с(2) - облачко. 1 слово. Ненависть. Полностью совпадает с 3с(2)
n_funcs['3*c(2)'] = q_n_3c_2_

def q_n__3c_(animacy, **b):
    # animacy unused
    # войска. 1 слово. Ненависть.
    inf = [[], []]
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    # end sg
    inf[1].append(b['основа1'] + 'а́')
    inf[1].append(b['основа'])
    inf[1].append(b['основа1'] + 'а́м')
    inf[1].append(b['основа1'] + 'а́')
    inf[1].append(b['основа1'] + 'а́ми')
    inf[1].append(b['основа1'] + 'а́х')
    # end pl
    return inf
n_funcs['(3c)'] = q_n__3c_

def q_n_3d_1__(animacy, **b):
    # animacy unused
    # молоко. 1 слово. Ненависть.
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(None)
    inf[1].append(None)
    inf[1].append(None)
    inf[1].append(None)
    inf[1].append(None)
    inf[1].append(None)
    # end pl
    return inf
n_funcs['3d(1)-'] = q_n_3d_1__

def q_n_3eV(animacy, **b):
    # animacy unused
    # ухо
    inf = [[], []]
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'о')
    inf[0].append(b['основа'] + 'ом')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа1'] + 'и')
    inf[1].append(b['основа2'] + 'е́й')
    inf[1].append(b['основа2'] + 'а́м')
    inf[1].append(b['основа1'] + 'и')
    inf[1].append(b['основа2'] + 'а́ми')
    inf[1].append(b['основа2'] + 'а́х')
    # end pl

def q_n_4a(animacy, **b):
    # чудовище, жилище
    inf = [[], []]
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'ем')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'])
    inf[1].append(b['основа'] + 'ам')
    if animacy:
        inf[1].append(b['основа'])
    else:
        inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'] + 'ами')
    inf[1].append(b['основа'] + 'ах')
    # end pl
    return inf
n_funcs['4a'] = q_n_4a

def q_n_4aV(animacy, **b):
    # animacy unused
    # вече, неоднозначность в р.п. мн.ч.
    inf = [[], []]
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'ем')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'] + 'ей')  # вариант: b['основа']
    inf[1].append(b['основа'] + 'ам')
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'] + 'ами')
    inf[1].append(b['основа'] + 'ах')
    # end pl
    return inf
n_funcs['4a^'] = q_n_4aV

def q_n_4f_1_(animacy, **b):
    # animacy unused
    # плечо, 1 слово. Ненависть
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа1'] + 'и')
    inf[1].append(b['основа1'])
    inf[1].append(b['основа'] + 'а́м')
    inf[1].append(b['основа1'] + 'и')
    inf[1].append(b['основа'] + 'а́ми')
    inf[1].append(b['основа'] + 'а́х')
    # end pl
    return inf
n_funcs['4f(1)'] = q_n_4f_1_

def q_n__5q_(animacy, **b):
    # animacy unused
    # дровец, щец
    inf = [[], []]
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    inf[0].append(None)
    # end sg
    inf[1].append(None)
    inf[1].append(b['основа'])
    inf[1].append(None)
    inf[1].append(None)
    inf[1].append(None)
    inf[1].append(None)
    # end pl
    return inf
n_funcs['(5?)'] = q_n__5q_

def q_n_5a(animacy, **b):
    # солнце
    inf = [[], []]
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'ем')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'])
    inf[1].append(b['основа'] + 'ам')
    if animacy:
        inf[1].append(b['основа'])
    else:
        inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'] + 'ами')
    inf[1].append(b['основа'] + 'ах')
    # end pl
    return inf
n_funcs['5a'] = q_n_5a

def q_n_5as(animacy, **b):
    #
    inf = [[], []]
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'ем')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа1'])
    inf[1].append(b['основа'] + 'ам')
    if animacy:
        inf[1].append(b['основа1'])
    else:
        inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'] + 'ами')
    inf[1].append(b['основа'] + 'ах')
    # end pl
    return inf
n_funcs['5*a'] = q_n_5as

def q_n_5as_2_(animacy, **b):
    # болотце
    inf = [[], []]
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'ем')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'] + 'ев')
    inf[1].append(b['основа'] + 'ам')
    if animacy:
        inf[1].append(b['основа'] + 'ев')
    else:
        inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'] + 'ами')
    inf[1].append(b['основа'] + 'ах')
    # end pl
    return inf
n_funcs['5*a(2)'] = q_n_5as_2_

def q_n_5as__2__(animacy, **b):
    # ведёрце
    inf = [[], []]
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'ем')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа1'])  #  b['основа'] + 'ев'
    inf[1].append(b['основа'] + 'ам')
    if animacy:
        inf[1].append(b['основа1'])  # b['основа'] + 'ев'
    else:
        inf[1].append(b['основа'] + 'а')
    inf[1].append(b['основа'] + 'ами')
    inf[1].append(b['основа'] + 'ах')
    # end pl
    return inf
n_funcs['5*a((2))'] = q_n_5as__2__

def q_n_5b(animacy, **b):
    # animacy unused
    # ружьецо
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа'] + 'а́')
    inf[1].append(b['основа1'])
    inf[1].append(b['основа'] + 'а́м')
    inf[1].append(b['основа'] + 'а́')
    inf[1].append(b['основа'] + 'а́ми')
    inf[1].append(b['основа'] + 'а́х')
    # end pl
    return inf
n_funcs['5b'] = q_n_5b

def q_n_5bs(animacy, **b):
    # деревцо, долотцо
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа'] + 'а́')
    inf[1].append(b['основа'] + 'е́ц')
    inf[1].append(b['основа'] + 'а́м')
    if animacy:
        inf[1].append(b['основа'] + 'е́ц')
    else:
        inf[1].append(b['основа'] + 'а́')
    inf[1].append(b['основа'] + 'а́ми')
    inf[1].append(b['основа'] + 'а́х')
    # end pl
    return inf
n_funcs['5*b'] = q_n_5bs

def q_n_5bs_2_(animacy, **b):
    # animacy unused
    # деревцо. Как, опять?? Ненависть
    inf = [[], []]
    inf[0].append(b['основа'] + 'цо́')
    inf[0].append(b['основа'] + 'ца́')
    inf[0].append(b['основа'] + 'цу́')
    inf[0].append(b['основа'] + 'цо́')
    inf[0].append(b['основа'] + 'цо́м')
    inf[0].append(b['основа'] + 'це́')
    # end sg
    inf[1].append(b['основа'] + 'ца́')
    inf[1].append(b['основа'] + 'цо́в')
    inf[1].append(b['основа'] + 'ца́м')
    inf[1].append(b['основа'] + 'ца́')
    inf[1].append(b['основа'] + 'ца́ми')
    inf[1].append(b['основа'] + 'ца́х')
    # end pl
    return inf
n_funcs['5*b(2)'] = q_n_5bs_2_

# 5*b- дрянцо?! - обрабатывается штатно

def q_n_5cs(animacy, **b):
    # animacy unused
    # сердце
    inf = [[], []]
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'а')
    inf[0].append(b['основа'] + 'у')
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'ем')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа1'] + 'а́')
    inf[1].append(b['основа2'])
    inf[1].append(b['основа1'] + 'а́м')
    if animacy:
        inf[1].append(b['основа2'])
    else:
        inf[1].append(b['основа1'] + 'а́')
    inf[1].append(b['основа1'] + 'а́ми')
    inf[1].append(b['основа1'] + 'а́х')
    # end pl
    return inf
n_funcs['5*с'] = q_n_5cs

# completely matches q_n_1d. What is it for?
def q_n_5d(animacy, **b):
    # лицо
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа1'] + 'а')
    inf[1].append(b['основа1'])
    inf[1].append(b['основа1'] + 'ам')
    if animacy:
        inf[1].append(b['основа1'])
    else:
        inf[1].append(b['основа1'] + 'а')
    inf[1].append(b['основа1'] + 'ами')
    inf[1].append(b['основа1'] + 'ах')
    # end pl
    return inf
n_funcs['5d'] = q_n_5d

def q_n_5ds(animacy, **b):
    # animacy unused
    # озерцо. Опять??
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа1'] + 'а')
    inf[1].append(b['основа2'])
    inf[1].append(b['основа1'] + 'ам')
    inf[1].append(b['основа1'] + 'а')
    inf[1].append(b['основа1'] + 'ами')
    inf[1].append(b['основа1'] + 'ах')
    # end pl
    return inf
n_funcs['5*d'] = q_n_5ds

# 5*d^ - яйцо - полностью совпадает с 5*d
n_funcs['5*d^'] = q_n_5ds

def q_n_5fs(animacy, **b):
    # animacy unused
    # крыльцо.
    inf = [[], []]
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'а́')
    inf[0].append(b['основа'] + 'у́')
    inf[0].append(b['основа'] + 'о́')
    inf[0].append(b['основа'] + 'о́м')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа1'] + 'а')
    inf[1].append(b['основа2'])
    inf[1].append(b['основа'] + 'а́м')
    inf[1].append(b['основа1'] + 'а')
    inf[1].append(b['основа'] + 'а́ми')
    inf[1].append(b['основа'] + 'а́х')
    # end pl
    return inf
n_funcs['5*f'] = q_n_5fs

def q_n_6as(animacy, **b):
    # animacy unused
    # ёрничанье
    inf = [[], []]
    inf[0].append(b['основа'] + 'ье')
    inf[0].append(b['основа'] + 'ья')
    inf[0].append(b['основа'] + 'ью')
    inf[0].append(b['основа'] + 'ье')
    inf[0].append(b['основа'] + 'ьем')
    inf[0].append(b['основа'] + 'ье')
    # end sg
    inf[1].append(b['основа'] + 'ья')
    inf[1].append(b['основа'] + 'ий')
    inf[1].append(b['основа'] + 'ьям')
    inf[1].append(b['основа'] + 'ья')
    inf[1].append(b['основа'] + 'ьями')
    inf[1].append(b['основа'] + 'ьях')
    # end pl
    return inf
n_funcs['6*a'] = q_n_6as

# 6*a- здоровье - обрабатывается через 6*a

def q_n_6as_2_(animacy, **b):
    # animacy unused
    # низовье
    inf = [[], []]
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'я')
    inf[0].append(b['основа'] + 'ю')
    inf[0].append(b['основа'] + 'е')
    inf[0].append(b['основа'] + 'ем')
    inf[0].append(b['основа'] + 'е')
    # end sg
    inf[1].append(b['основа'] + 'я')
    inf[1].append(b['основа'] + 'ев')
    inf[1].append(b['основа'] + 'ям')
    inf[1].append(b['основа'] + 'я')
    inf[1].append(b['основа'] + 'ями')
    inf[1].append(b['основа'] + 'ях')
    # end pl
    return inf
n_funcs['6*a(2)'] = q_n_6as_2_

def q_n_6b_(animacy, **b):
    # animacy unused
    # дитё. Единственное слово. Единственное число. Ненависть.
    inf = [[], []]
    inf[0].append(b['основа'] + 'ё')
    inf[0].append(b['основа'] + 'я́')
    inf[0].append(b['основа'] + 'ю́')
    inf[0].append(b['основа'] + 'ё')
    inf[0].append(b['основа'] + 'ём')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(None)
    inf[1].append(None)
    inf[1].append(None)
    inf[1].append(None)
    inf[1].append(None)
    inf[1].append(None)
    # end pl
    return inf
n_funcs['6b-'] = q_n_6b_

def q_n_6bs(animacy, **b):
    # animacy unused
    # ковыльё
    inf = [[], []]
    inf[0].append(b['основа'] + 'ьё')
    inf[0].append(b['основа'] + 'ья́')
    inf[0].append(b['основа'] + 'ью́')
    inf[0].append(b['основа'] + 'ьё')
    inf[0].append(b['основа'] + 'ьём')
    inf[0].append(b['основа'] + 'ье́')
    # end sg
    inf[1].append(b['основа'] + 'ья́')
    inf[0].append(b['основа'] + 'е́й')
    inf[0].append(b['основа'] + 'ья́м')
    inf[0].append(b['основа'] + 'ья́')
    inf[0].append(b['основа'] + 'ья́ми')
    inf[0].append(b['основа'] + 'ья́х')
    # end pl
    return inf
n_funcs['6*b'] = q_n_6bs

# 6*b- - бабьё - обрабатывается обычным образом

def q_n_6bs_2_(animacy, **b):
    # animacy unused
    # жнивьё. Единственное слово. Единственное число. Ненависть.
    inf = [[], []]
    inf[0].append(b['основа'] + 'ьё')
    inf[0].append(b['основа'] + 'ья́')
    inf[0].append(b['основа'] + 'ью́')
    inf[0].append(b['основа'] + 'ьё')
    inf[0].append(b['основа'] + 'ьём')
    inf[0].append(b['основа'] + 'ье́')
    # end sg
    inf[1].append(b['основа'] + 'ья́')
    inf[0].append(b['основа'] + 'ьёв')
    inf[0].append(b['основа'] + 'ья́м')
    inf[0].append(b['основа'] + 'ья́')
    inf[0].append(b['основа'] + 'ья́ми')
    inf[0].append(b['основа'] + 'ья́х')
    # end pl
    return inf
n_funcs['6*b(2)'] = q_n_6bs_2_

def q_n_6ds(animacy, **b):
    # animacy unused
    # копьё, жнивьё. Хм, опять жнивьё?
    inf = [[], []]
    inf[0].append(b['основа'] + 'ё')
    inf[0].append(b['основа'] + 'я́')
    inf[0].append(b['основа'] + 'ю́')
    inf[0].append(b['основа'] + 'ё')
    inf[0].append(b['основа'] + 'ём')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа1'] + 'я')
    inf[0].append(b['основа2'])
    inf[0].append(b['основа1'] + 'ям')
    inf[0].append(b['основа1'] + 'я')
    inf[0].append(b['основа1'] + 'ями')
    inf[0].append(b['основа1'] + 'ях')
    # end pl
    return inf
n_funcs['6*d'] = q_n_6ds

def q_n_6dsV(animacy, **b):
    # animacy unused
    # ружьё. Было же уже.
    inf = [[], []]
    inf[0].append(b['основа'] + 'ьё')
    inf[0].append(b['основа'] + 'ья́')
    inf[0].append(b['основа'] + 'ью́')
    inf[0].append(b['основа'] + 'ьё')
    inf[0].append(b['основа'] + 'ьём')
    inf[0].append(b['основа'] + 'ье́')
    # end sg
    inf[1].append(b['основа1'] + 'ья')
    inf[0].append(b['основа2'] + 'ей')
    inf[0].append(b['основа1'] + 'ьям')
    inf[0].append(b['основа1'] + 'ья')
    inf[0].append(b['основа1'] + 'ьями')
    inf[0].append(b['основа1'] + 'ьях')
    # end pl
    return inf
n_funcs['6*dV'] = q_n_6dsV

def q_n_6ds_2_(animacy, **b):
    # animacy unused
    # жнивьё. Хм, опять жнивьё?? Зашкаливающая ненависть!
    inf = [[], []]
    inf[0].append(b['основа'] + 'ё')
    inf[0].append(b['основа'] + 'я́')
    inf[0].append(b['основа'] + 'ю́')
    inf[0].append(b['основа'] + 'ё')
    inf[0].append(b['основа'] + 'ём')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа1'] + 'я')
    inf[0].append(b['основа1'] + 'ев')
    inf[0].append(b['основа1'] + 'ям')
    inf[0].append(b['основа1'] + 'я')
    inf[0].append(b['основа1'] + 'ями')
    inf[0].append(b['основа1'] + 'ях')
    # end pl
    return inf
n_funcs['6*d(2)'] = q_n_6ds_2_

def q_n_7a(animacy, **b):
    # здание
    inf = [[], []]
    inf[0].append(b['основа'] + 'ие')
    inf[0].append(b['основа'] + 'ия')
    inf[0].append(b['основа'] + 'ию')
    inf[0].append(b['основа'] + 'ие')
    inf[0].append(b['основа'] + 'ием')
    inf[0].append(b['основа'] + 'ии')
    # end sg
    inf[1].append(b['основа'] + 'ия')
    inf[1].append(b['основа'] + 'ий')
    inf[1].append(b['основа'] + 'иям')
    if animacy:
        inf[1].append(b['основа'] + 'ий')
    else:
        inf[1].append(b['основа'] + 'ия')
    inf[1].append(b['основа'] + 'иями')
    inf[1].append(b['основа'] + 'иях')
    # end pl
    return inf
n_funcs['7a'] = q_n_7a

# 7a- - благорастворение - обрабатывается штатно через 7a

def q_n_7b(animacy, **b):
    # animacy unused
    # мумиё
    inf = [[], []]
    inf[0].append(b['основа'] + 'иё́')
    inf[0].append(b['основа'] + 'ия́')
    inf[0].append(b['основа'] + 'ию́')
    inf[0].append(b['основа'] + 'иё́')
    inf[0].append(b['основа'] + 'иём')
    inf[0].append(b['основа'] + 'ие́')
    # end sg
    inf[1].append(b['основа'] + 'ия́')
    inf[1].append(b['основа'] + 'и́й')
    inf[1].append(b['основа'] + 'ия́м')
    inf[1].append(b['основа'] + 'ия́')
    inf[1].append(b['основа'] + 'ия́ми')
    inf[1].append(b['основа'] + 'ия́х')
    # end pl
    return inf
n_funcs['7b'] = q_n_7b

def q_n_7bV(animacy, **b):
    # animacy unused
    # житие
    inf = [[], []]
    inf[0].append(b['основа'] + 'е́')
    inf[0].append(b['основа'] + 'я́')
    inf[0].append(b['основа'] + 'ю́')
    inf[0].append(b['основа'] + 'е́')
    inf[0].append(b['основа'] + 'е́м')
    inf[0].append(b['основа'] + 'и́')
    # end sg
    inf[1].append(b['основа'] + 'я́')
    inf[1].append(b['основа1'])
    inf[1].append(b['основа'] + 'я́м')
    inf[1].append(b['основа'] + 'я́')
    inf[1].append(b['основа'] + 'я́ми')
    inf[1].append(b['основа'] + 'я́х')
    # end pl
    return inf
n_funcs['7b^'] = q_n_7bV

def q_n_7b_(animacy, **b):
    # animacy unused
    # житиё
    inf = [[], []]
    inf[0].append(b['основа'] + 'иё')
    inf[0].append(b['основа'] + 'ия́')
    inf[0].append(b['основа'] + 'ию́')
    inf[0].append(b['основа'] + 'иё')
    inf[0].append(b['основа'] + 'ие́м')
    inf[0].append(b['основа'] + 'ие́')
    # end sg
    inf[1].append(None)  # {{{основа}}ия́
    inf[1].append(None)  # {{{основа}}и́й
    inf[1].append(None)  # {{{основа}}ия́м
    inf[1].append(None)  # {{{основа}}ия́
    inf[1].append(None)
    inf[1].append(None)
    # end pl
    return inf
n_funcs['7b-'] = q_n_7b_

def q_n_7b_V(animacy, **b):
    # animacy unused
    # житие. Опять??
    inf = [[], []]
    inf[0].append(b['основа'] + 'е́')
    inf[0].append(b['основа'] + 'я́')
    inf[0].append(b['основа'] + 'ю́')
    inf[0].append(b['основа'] + 'е́')
    inf[0].append(b['основа'] + 'е́м')
    inf[0].append(b['основа'] + 'и́')
    # end sg
    inf[1].append(None)
    inf[1].append(None)
    inf[1].append(None)
    inf[1].append(None)
    inf[1].append(None)
    inf[1].append(None)
    # end pl
    return inf
n_funcs['7b-^'] = q_n_7b_V

def q_n_7b2(animacy, **b):
    # animacy unused
    # остриё
    inf = [[], []]
    inf[0].append(b['основа'] + 'ё')
    inf[0].append(b['основа'] + 'я́')
    inf[0].append(b['основа'] + 'ю́')
    inf[0].append(b['основа'] + 'ё')
    inf[0].append(b['основа'] + 'ём')
    inf[0].append(b['основа'] + 'е́')
    # end sg
    inf[1].append(b['основа'] + 'я́')
    inf[1].append(b['основа'] + 'ёв')
    inf[1].append(b['основа'] + 'я́м')
    inf[1].append(b['основа'] + 'я́')
    inf[1].append(b['основа'] + 'я́ми')
    inf[1].append(b['основа'] + 'я́х')
    # end pl
    return inf
n_funcs['7b(2)'] = q_n_7b2

def q_n_8ar(animacy, **b):
    # animacy unused
    # знамя
    inf = [[], []]
    inf[0].append(b['основа'] + 'я')
    inf[0].append(b['основа'] + 'ени')
    inf[0].append(b['основа'] + 'ени')
    inf[0].append(b['основа'] + 'я')
    inf[0].append(b['основа'] + 'енем')
    inf[0].append(b['основа'] + 'ени')
    # end sg
    inf[1].append(b['основа'] + 'ёна')
    inf[1].append(b['основа'] + 'ён')
    inf[1].append(b['основа'] + 'ёнам')
    inf[1].append(b['основа'] + 'ёна')
    inf[1].append(b['основа'] + 'ёнами')
    inf[1].append(b['основа'] + 'ёнах')
    # end pl
    return inf
n_funcs['8°a'] = q_n_8ar

def q_n_8cr(animacy, **b):
    # animacy unused
    # племя
    inf = [[], []]
    inf[0].append(b['основа'] + 'я')
    inf[0].append(b['основа'] + 'ени')
    inf[0].append(b['основа'] + 'ени')
    inf[0].append(b['основа'] + 'я')
    inf[0].append(b['основа'] + 'енем')
    inf[0].append(b['основа'] + 'ени')
    # end sg
    inf[1].append(b['основа1'] + 'ена́')
    inf[1].append(b['основа2'])
    inf[1].append(b['основа1'] + 'ена́м')
    inf[1].append(b['основа1'] + 'ена́')
    inf[1].append(b['основа1'] + 'ена́ми')
    inf[1].append(b['основа1'] + 'ена́х')
    # end pl
    return inf
n_funcs['8°c'] = q_n_8cr

def q_n_8crV(animacy, **b):
    # animacy unused
    # племя
    inf = [[], []]
    inf[0].append(b['основа'] + 'я')
    inf[0].append(b['основа'] + 'ени')
    inf[0].append(b['основа'] + 'ени')
    inf[0].append(b['основа'] + 'я')
    inf[0].append(b['основа'] + 'енем')
    inf[0].append(b['основа'] + 'ени')
    # end sg
    inf[1].append(b['основа1'] + 'ена́')
    inf[1].append(b['основа1'] + 'я́н')
    inf[1].append(b['основа1'] + 'ена́м')
    inf[1].append(b['основа1'] + 'ена́')
    inf[1].append(b['основа1'] + 'ена́ми')
    inf[1].append(b['основа1'] + 'ена́х')
    # end pl
    return inf
n_funcs['8°c^'] = q_n_8crV

# 8°c- - бремя - обрабатывается обычным способом, через 8°c
