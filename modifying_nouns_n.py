n_funcs = {}

def q_n_1a(animacy, base, base1 = None, base2 = None):
    # чадо, болото
    inf = [[], []]
    inf[0].add(base + 'о')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'о')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'а')
    inf[1].add(base)
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base)
    else:
        inf[1].add(base + 'а')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
n_funcs['1a'] = q_n_1a

# skip 1a-

def q_n_1aV(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # полено
    inf = [[], []]
    inf[0].add(base + 'о')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'о')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'я')
    inf[1].add(base1 + 'ев')
    inf[1].add(base1 + 'ям')
    inf[1].add(base1 + 'я')
    inf[1].add(base1 + 'ями')
    inf[1].add(base1 + 'ях')
    # end pl
n_funcs['1a^'] = q_n_1aV

def q_n_1aVi(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # колено. Единственное слово. Запредельная ненависть
    inf = [[], []]
    inf[0].add(base + 'о')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'о')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base + 'ей')
    inf[1].add(base + 'ям')
    inf[1].add(base + 'и')
    inf[1].add(base + 'ями')
    inf[1].add(base + 'ях')
    # end pl
n_funcs['1a^-и'] = q_n_1aVi

def q_n_1aVr(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # озеро. Единственное слово. Запредельная ненависть
    inf = [[], []]
    inf[0].add(base + 'о')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'о')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'а')
    inf[1].add(base1)
    inf[1].add(base1 + 'ам')
    inf[1].add(base1 + 'а')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl
n_funcs['1a^-р'] = q_n_1aVr

def q_n_1aV1(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # утро. Единственное слово. Неоднозначность ударения. Запредельная, зашкаливающая ненависть
    inf = [[], []]
    inf[0].add(base + 'о')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'о')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'а')
    inf[1].add(base)
    inf[1].add(base + 'ам')
    inf[1].add(base + 'а')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
n_funcs['1a^-1'] = q_n_1aV1

def q_n_1as(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # коромысло
    inf = [[], []]
    inf[0].add(base + 'о')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'о')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'а')
    inf[1].add(base1)
    inf[1].add(base + 'ам')
    inf[1].add(base + 'а')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
n_funcs['1*a'] = q_n_1as

def q_n__1a_(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # коромысло
    inf = [[], []]
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    # end sg
    inf[1].add(base + 'а')
    inf[1].add(base)
    inf[1].add(base + 'ам')
    inf[1].add(base + 'а')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
n_funcs['(1a)'] = q_n__1a_

def q_n__1aV_(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # Озёры. Одно слово. Ненависть.
    inf = [[], []]
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    # end sg
    inf[1].add(base + 'ы')
    inf[1].add(base)
    inf[1].add(base + 'ам')
    inf[1].add(base + 'ы')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
n_funcs['(1a^)'] = q_n__1aV_

def q_n_1b(animacy, base, base1 = None, base2 = None):
    # божество, вещество
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base + 'а́')
    inf[1].add(base1)
    inf[1].add(base + 'а́м')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base + 'а́')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl
n_funcs['1b'] = q_n_1b

def q_n_1bV(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # мудо. Хм. К тому же, неоднозначность склонения.
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base + 'е́й')
    inf[1].add(base + 'я́м')
    inf[1].add(base1 + 'и')
    inf[1].add(base + 'я́ми')
    inf[1].add(base + 'я́х')
    # end pl
n_funcs['1b^'] = q_n_1bV

# 1b- обрабатывается штатно

def q_n_1bs_(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # дно
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(None)  # *{{{основа}}}а́
    inf[1].add(None)  # *{{{основа1}}}
    inf[1].add(None)  # *{{{основа}}}а́м
    inf[1].add(None)  # *{{{основа}}}а́
    inf[1].add(None)  # *{{{основа}}}а́ми
    inf[1].add(None)  # *{{{основа}}}а́х
    # end pl
n_funcs['1*b-'] = q_n_1bs_

def q_n_1bsV(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # зло. единственный пример в среднем роде
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(None)  # *{{{основа}}}а́
    inf[1].add(base1)
    inf[1].add(None)  # *{{{основа}}}а́м
    inf[1].add(None)  # *{{{основа}}}а́
    inf[1].add(None)  # *{{{основа}}}а́ми
    inf[1].add(None)  # *{{{основа}}}а́х
    # end pl
n_funcs['1*b^'] = q_n_1bsV

def q_n__1b_(animacy, base, base1 = None, base2 = None):
    # небеса
    inf = [[], []]
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    # end sg
    inf[1].add(base + 'а́')
    inf[1].add(base1)
    inf[1].add(base + 'а́м')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base + 'а́')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl
n_funcs['(1b)'] = q_n__1b_

def q_n_1c(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # место
    inf = [[], []]
    inf[0].add(base + 'о')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'о')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'а́')
    inf[1].add(base)
    inf[1].add(base1 + 'а́м')
    inf[1].add(base + 'а́')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl
n_funcs['1c'] = q_n_1c

def q_n_1cV(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # древо
    inf = [[], []]
    inf[0].add(base + 'о')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'о')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'а́')
    inf[1].add(base2)
    inf[1].add(base1 + 'а́м')
    inf[1].add(base1 + 'а́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
n_funcs['1c^'] = q_n_1cV

# 1c- обрабатывается штатно

def q_n_1csV(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # масло. единственный пример в среднем роде
    inf = [[], []]
    inf[0].add(base + 'о')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'о')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'а́')
    inf[1].add(base2)
    inf[1].add(base1 + 'а́м')
    inf[1].add(base1 + 'а́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
n_funcs['1*c^'] = q_n_1csV

def q_n_1d(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # вино
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'а')
    inf[1].add(base1)
    inf[1].add(base1 + 'ам')
    inf[1].add(base1 + 'а')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl
n_funcs['1d'] = q_n_1d

def q_n_1dV(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # крыло
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'я')
    inf[1].add(base1) + 'ев'
    inf[1].add(base1 + 'ям')
    inf[1].add(base1 + 'я')
    inf[1].add(base1 + 'ями')
    inf[1].add(base1 + 'ях')
    # end pl
n_funcs['1d^'] = q_n_1dV

# 1d- обрабатывается штатно

def q_n_1ds(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # колесо, гумно
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'а')
    inf[1].add(base2)
    inf[1].add(base1 + 'ам')
    inf[1].add(base1 + 'а')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl
n_funcs['1*d'] = q_n_1ds
# гумно может склоняться по 1*d^, при этом правила те же, что и для 1*d, но другая основа2
q_b_1dsV = q_n_1ds

def q_n_1dsVS(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # дно/донья (в смысле, много днов 8-0. Запредельный уровень ненависти
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'ья')
    inf[1].add(base1 + 'ьев')
    inf[1].add(base1 + 'ьям')
    inf[1].add(base1 + 'ья')
    inf[1].add(base1 + 'ьями')
    inf[1].add(base1 + 'ьях')
    # end pl
n_funcs['1*d^-ь'] = q_n_1dsVS

def q_n_1f(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # тавро
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'а')
    inf[1].add(base1)
    inf[1].add(base + 'а́м')
    inf[1].add(base1 + 'а')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl
n_funcs['1f'] = q_n_1f

def q_n_2a(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # горе
    inf = [[], []]
    inf[0].add(base + 'е')
    inf[0].add(base + 'я')
    inf[0].add(base + 'ю')
    inf[0].add(base + 'е')
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    # likely, unused
    inf[1].add(base + 'я')
    inf[1].add(base + 'ь')
    inf[1].add(base + 'ям')
    inf[1].add(base + 'я')
    inf[1].add(base + 'ями')
    inf[1].add(base + 'ях')
    # end pl
n_funcs['2a'] = q_n_2a

# 2a- обрабатывается штатно

def q_n_2c(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # поле
    inf = [[], []]
    inf[0].add(base + 'е')
    inf[0].add(base + 'я')
    inf[0].add(base + 'ю')
    inf[0].add(base + 'е')
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'я́')
    inf[1].add(base1 + 'е́й')
    inf[1].add(base1 + 'я́м')
    inf[1].add(base1 + 'я́')
    inf[1].add(base1 + 'я́ми')
    inf[1].add(base1 + 'я́х')
    # end pl
n_funcs['2c'] = q_n_2c

# 2c- обрабатывается штатно

def q_n_3a(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # благо
    inf = [[], []]
    inf[0].add(base + 'о')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'о')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'а')
    inf[1].add(base)
    inf[1].add(base + 'ам')
    inf[1].add(base + 'а')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
n_funcs['3a'] = q_n_3a

# 3a(1), брюхо, полностью совпадает с q_n_3a
n_funcs['3a(1)'] = q_n_3a

# 3a(1)(2), колёсико, полностью совпадает с q_n_3a
n_funcs['3a(1)(2)'] = q_n_3a

def q_n_3as_1_(animacy, base, base1 = None, base2 = None):
    # донышко
    inf = [[], []]
    inf[0].add(base + 'о')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'о')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base1)
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
n_funcs['3*a(1)'] = q_n_3as_1_

def q_n_3as_1__2_(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # древко. Возможны различные ударения :/
    inf = [[], []]
    inf[0].add(base + 'о')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'о')
    inf[0].add(base + 'ом')  # вариант base1 + 'о́м'
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base + 'ов')  # вариант base1 + 'о́в'
    inf[1].add(base + 'ам')  # вариант base1 + 'а́м'
    inf[1].add(base + 'и')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
n_funcs['3*a(1)(2)'] = q_n_3as_1__2_

def q_n_3bs_1__2_(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # ушко
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base + 'и́')
    inf[1].add(base + 'о́в')  # вариант base1 + 'о́в'
    inf[1].add(base + 'а́м')  # вариант base1 + 'а́м'
    inf[1].add(base + 'и́')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl
n_funcs['3*b(1)(2)'] = q_n_3bs_1__2_

def q_n_3c(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # войско
    inf = [[], []]
    inf[0].add(base + 'о')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'о')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'а́')
    inf[1].add(base)
    inf[1].add(base1 + 'а́м')
    inf[1].add(base1 + 'а́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
n_funcs['3c'] = q_n_3c

def q_n_3c_2_(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # облако. 1 слово. Ненависть.
    inf = [[], []]
    inf[0].add(base + 'о')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'о')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'а́')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    inf[1].add(base1 + 'а́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
n_funcs['3c(2)'] = q_n_3c_2_

# 3*с(2) - облачко. 1 слово. Ненависть. Полностью совпадает с 3с(2)
n_funcs['3*c(2)'] = q_n_3c_2_

def q_n__3c_(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # войска. 1 слово. Ненависть.
    inf = [[], []]
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    # end sg
    inf[1].add(base1 + 'а́')
    inf[1].add(base)
    inf[1].add(base1 + 'а́м')
    inf[1].add(base1 + 'а́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
n_funcs['(3c)'] = q_n__3c_

def q_n_3d_1__(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # молоко. 1 слово. Ненависть.
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(None)
    inf[1].add(None)
    inf[1].add(None)
    inf[1].add(None)
    inf[1].add(None)
    inf[1].add(None)
    # end pl
n_funcs['3d(1)-'] = q_n_3d_1__

def q_n_3eV(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # ухо
    inf = [[], []]
    inf[0].add(base + 'о')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'о')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base2 + 'е́й')
    inf[1].add(base2 + 'а́м')
    inf[1].add(base1 + 'и')
    inf[1].add(base2 + 'а́ми')
    inf[1].add(base2 + 'а́х')
    # end pl

def q_n_4a(animacy, base, base1 = None, base2 = None):
    # чудовище, жилище
    inf = [[], []]
    inf[0].add(base + 'е')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'е')
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'а')
    inf[1].add(base)
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base)
    else:
        inf[1].add(base + 'а')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
n_funcs['4a'] = q_n_4a

def q_n_4aV(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # вече, неоднозначность в р.п. мн.ч.
    inf = [[], []]
    inf[0].add(base + 'е')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'е')
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'а')
    inf[1].add(base + 'ей')  # вариант: base
    inf[1].add(base + 'ам')
    inf[1].add(base + 'а')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
n_funcs['4a^'] = q_n_4aV

def q_n_4f_1_(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # плечо, 1 слово. Ненависть
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base1)
    inf[1].add(base + 'а́м')
    inf[1].add(base1 + 'и')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl
n_funcs['4f(1)'] = q_n_4f_1_

def q_n__5q_(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # дровец, щец
    inf = [[], []]
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    # end sg
    inf[1].add(None)
    inf[1].add(base)
    inf[1].add(None)
    inf[1].add(None)
    inf[1].add(None)
    inf[1].add(None)
    # end pl
n_funcs['(5?)'] = q_n__5q_

def q_n_5a(animacy, base, base1 = None, base2 = None):
    # солнце
    inf = [[], []]
    inf[0].add(base + 'е')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'е')
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'а')
    inf[1].add(base)
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base)
    else:
        inf[1].add(base + 'а')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
n_funcs['5a'] = q_n_5a

def q_n_5as(animacy, base, base1 = None, base2 = None):
    #
    inf = [[], []]
    inf[0].add(base + 'е')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'е')
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'а')
    inf[1].add(base1)
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base + 'а')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
n_funcs['5*a'] = q_n_5as

def q_n_5as_2_(animacy, base, base1 = None, base2 = None):
    # болотце
    inf = [[], []]
    inf[0].add(base + 'е')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'е')
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'а')
    inf[1].add(base + 'ев')
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base + 'ев')
    else:
        inf[1].add(base + 'а')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
n_funcs['5*a(2)'] = q_n_5as_2_

def q_n_5as__2__(animacy, base, base1 = None, base2 = None):
    # ведёрце
    inf = [[], []]
    inf[0].add(base + 'е')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'е')
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'а')
    inf[1].add(base1)  #  base + 'ев'
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base1)  # base + 'ев'
    else:
        inf[1].add(base + 'а')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
n_funcs['5*a((2))'] = q_n_5as__2__

def q_n_5b(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # ружьецо
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base + 'а́')
    inf[1].add(base1)
    inf[1].add(base + 'а́м')
    inf[1].add(base + 'а́')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl
n_funcs['5b'] = q_n_5b

def q_n_5bs(animacy, base, base1 = None, base2 = None):
    # деревцо, долотцо
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base + 'а́')
    inf[1].add(base + 'е́ц')
    inf[1].add(base + 'а́м')
    if animacy:
        inf[1].add(base + 'е́ц')
    else:
        inf[1].add(base + 'а́')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl
n_funcs['5*b'] = q_n_5bs

def q_n_5bs_2_(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # деревцо. Как, опять?? Ненависть
    inf = [[], []]
    inf[0].add(base + 'цо́')
    inf[0].add(base + 'ца́')
    inf[0].add(base + 'цу́')
    inf[0].add(base + 'цо́')
    inf[0].add(base + 'цо́м')
    inf[0].add(base + 'це́')
    # end sg
    inf[1].add(base + 'ца́')
    inf[1].add(base + 'цо́в')
    inf[1].add(base + 'ца́м')
    inf[1].add(base + 'ца́')
    inf[1].add(base + 'ца́ми')
    inf[1].add(base + 'ца́х')
    # end pl
n_funcs['5*b(2)'] = q_n_5bs_2_

# 5*b- дрянцо?! - обрабатывается штатно

def q_n_5cs(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # сердце
    inf = [[], []]
    inf[0].add(base + 'е')
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'е')
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'а́')
    inf[1].add(base2)
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base2)
    else:
        inf[1].add(base1 + 'а́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
n_funcs['5*с'] = q_n_5cs

# completely matches q_n_1d. What is it for?
def q_n_5d(animacy, base, base1 = None, base2 = None):
    # лицо
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'а')
    inf[1].add(base1)
    inf[1].add(base1 + 'ам')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base1 + 'а')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl
n_funcs['5d'] = q_n_5d

def q_n_5ds(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # озерцо. Опять??
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'а')
    inf[1].add(base2)
    inf[1].add(base1 + 'ам')
    inf[1].add(base1 + 'а')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl
n_funcs['5*d'] = q_n_5ds

# 5*d^ - яйцо - полностью совпадает с 5*d
n_funcs['5*d^'] = q_n_5ds

def q_n_5fs(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # крыльцо.
    inf = [[], []]
    inf[0].add(base + 'о́')
    inf[0].add(base + 'а́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́')
    inf[0].add(base + 'о́м')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'а')
    inf[1].add(base2)
    inf[1].add(base + 'а́м')
    inf[1].add(base1 + 'а')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl
n_funcs['5*f'] = q_n_5fs

def q_n_6as(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # ёрничанье
    inf = [[], []]
    inf[0].add(base + 'ье')
    inf[0].add(base + 'ья')
    inf[0].add(base + 'ью')
    inf[0].add(base + 'ье')
    inf[0].add(base + 'ьем')
    inf[0].add(base + 'ье')
    # end sg
    inf[1].add(base + 'ья')
    inf[1].add(base + 'ий')
    inf[1].add(base + 'ьям')
    inf[1].add(base + 'ья')
    inf[1].add(base + 'ьями')
    inf[1].add(base + 'ьях')
    # end pl
n_funcs['6*a'] = q_n_6as

# 6*a- здоровье - обрабатывается через 6*a

def q_n_6as_2_(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # низовье
    inf = [[], []]
    inf[0].add(base + 'е')
    inf[0].add(base + 'я')
    inf[0].add(base + 'ю')
    inf[0].add(base + 'е')
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'я')
    inf[1].add(base + 'ев')
    inf[1].add(base + 'ям')
    inf[1].add(base + 'я')
    inf[1].add(base + 'ями')
    inf[1].add(base + 'ях')
    # end pl
n_funcs['6*a(2)'] = q_n_6as_2_

def q_n_6b_(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # дитё. Единственное слово. Единственное число. Ненависть.
    inf = [[], []]
    inf[0].add(base + 'ё')
    inf[0].add(base + 'я́')
    inf[0].add(base + 'ю́')
    inf[0].add(base + 'ё')
    inf[0].add(base + 'ём')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(None)
    inf[1].add(None)
    inf[1].add(None)
    inf[1].add(None)
    inf[1].add(None)
    inf[1].add(None)
    # end pl
n_funcs['6b-'] = q_n_6b_

def q_n_6bs(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # ковыльё
    inf = [[], []]
    inf[0].add(base + 'ьё')
    inf[0].add(base + 'ья́')
    inf[0].add(base + 'ью́')
    inf[0].add(base + 'ьё')
    inf[0].add(base + 'ьём')
    inf[0].add(base + 'ье́')
    # end sg
    inf[1].add(base + 'ья́')
    inf[0].add(base + 'е́й')
    inf[0].add(base + 'ья́м')
    inf[0].add(base + 'ья́')
    inf[0].add(base + 'ья́ми')
    inf[0].add(base + 'ья́х')
    # end pl
n_funcs['6*b'] = q_n_6bs

# 6*b- - бабьё - обрабатывается обычным образом

def q_n_6bs_2_(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # жнивьё. Единственное слово. Единственное число. Ненависть.
    inf = [[], []]
    inf[0].add(base + 'ьё')
    inf[0].add(base + 'ья́')
    inf[0].add(base + 'ью́')
    inf[0].add(base + 'ьё')
    inf[0].add(base + 'ьём')
    inf[0].add(base + 'ье́')
    # end sg
    inf[1].add(base + 'ья́')
    inf[0].add(base + 'ьёв')
    inf[0].add(base + 'ья́м')
    inf[0].add(base + 'ья́')
    inf[0].add(base + 'ья́ми')
    inf[0].add(base + 'ья́х')
    # end pl
n_funcs['6*b(2)'] = q_n_6bs_2_

def q_n_6ds(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # копьё, жнивьё. Хм, опять жнивьё?
    inf = [[], []]
    inf[0].add(base + 'ё')
    inf[0].add(base + 'я́')
    inf[0].add(base + 'ю́')
    inf[0].add(base + 'ё')
    inf[0].add(base + 'ём')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'я')
    inf[0].add(base2)
    inf[0].add(base1 + 'ям')
    inf[0].add(base1 + 'я')
    inf[0].add(base1 + 'ями')
    inf[0].add(base1 + 'ях')
    # end pl
n_funcs['6*d'] = q_n_6ds

def q_n_6dsV(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # ружьё. Было же уже.
    inf = [[], []]
    inf[0].add(base + 'ьё')
    inf[0].add(base + 'ья́')
    inf[0].add(base + 'ью́')
    inf[0].add(base + 'ьё')
    inf[0].add(base + 'ьём')
    inf[0].add(base + 'ье́')
    # end sg
    inf[1].add(base1 + 'ья')
    inf[0].add(base2 + 'ей')
    inf[0].add(base1 + 'ьям')
    inf[0].add(base1 + 'ья')
    inf[0].add(base1 + 'ьями')
    inf[0].add(base1 + 'ьях')
    # end pl
n_funcs['6*dV'] = q_n_6dsV

def q_n_6ds_2_(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # жнивьё. Хм, опять жнивьё?? Зашкаливающая ненависть!
    inf = [[], []]
    inf[0].add(base + 'ё')
    inf[0].add(base + 'я́')
    inf[0].add(base + 'ю́')
    inf[0].add(base + 'ё')
    inf[0].add(base + 'ём')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'я')
    inf[0].add(base1 + 'ев')
    inf[0].add(base1 + 'ям')
    inf[0].add(base1 + 'я')
    inf[0].add(base1 + 'ями')
    inf[0].add(base1 + 'ях')
    # end pl
n_funcs['6*d(2)'] = q_n_6ds_2_

def q_n_7a(animacy, base, base1 = None, base2 = None):
    # здание
    inf = [[], []]
    inf[0].add(base + 'ие')
    inf[0].add(base + 'ия')
    inf[0].add(base + 'ию')
    inf[0].add(base + 'ие')
    inf[0].add(base + 'ием')
    inf[0].add(base + 'ии')
    # end sg
    inf[1].add(base + 'ия')
    inf[1].add(base + 'ий')
    inf[1].add(base + 'иям')
    if animacy:
        inf[1].add(base + 'ий')
    else:
        inf[1].add(base + 'ия')
    inf[1].add(base + 'иями')
    inf[1].add(base + 'иях')
    # end pl
n_funcs['7a'] = q_n_7a

# 7a- - благорастворение - обрабатывается штатно через 7a

def q_n_7b(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # мумиё
    inf = [[], []]
    inf[0].add(base + 'иё́')
    inf[0].add(base + 'ия́')
    inf[0].add(base + 'ию́')
    inf[0].add(base + 'иё́')
    inf[0].add(base + 'иём')
    inf[0].add(base + 'ие́')
    # end sg
    inf[1].add(base + 'ия́')
    inf[1].add(base + 'и́й')
    inf[1].add(base + 'ия́м')
    inf[1].add(base + 'ия́')
    inf[1].add(base + 'ия́ми')
    inf[1].add(base + 'ия́х')
    # end pl
n_funcs['7b'] = q_n_7b

def q_n_7bV(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # житие
    inf = [[], []]
    inf[0].add(base + 'е́')
    inf[0].add(base + 'я́')
    inf[0].add(base + 'ю́')
    inf[0].add(base + 'е́')
    inf[0].add(base + 'е́м')
    inf[0].add(base + 'и́')
    # end sg
    inf[1].add(base + 'я́')
    inf[1].add(base1)
    inf[1].add(base + 'я́м')
    inf[1].add(base + 'я́')
    inf[1].add(base + 'я́ми')
    inf[1].add(base + 'я́х')
    # end pl
n_funcs['7b^'] = q_n_7bV

def q_n_7b_(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # житиё
    inf = [[], []]
    inf[0].add(base + 'иё')
    inf[0].add(base + 'ия́')
    inf[0].add(base + 'ию́')
    inf[0].add(base + 'иё')
    inf[0].add(base + 'ие́м')
    inf[0].add(base + 'ие́')
    # end sg
    inf[1].add(None)  # {{{основа}}ия́
    inf[1].add(None)  # {{{основа}}и́й
    inf[1].add(None)  # {{{основа}}ия́м
    inf[1].add(None)  # {{{основа}}ия́
    inf[1].add(None)
    inf[1].add(None)
    # end pl
n_funcs['7b-'] = q_n_7b_

def q_n_7b_V(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # житие. Опять??
    inf = [[], []]
    inf[0].add(base + 'е́')
    inf[0].add(base + 'я́')
    inf[0].add(base + 'ю́')
    inf[0].add(base + 'е́')
    inf[0].add(base + 'е́м')
    inf[0].add(base + 'и́')
    # end sg
    inf[1].add(None)
    inf[1].add(None)
    inf[1].add(None)
    inf[1].add(None)
    inf[1].add(None)
    inf[1].add(None)
    # end pl
n_funcs['7b-^'] = q_n_7b_V

def q_n_7b2(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # остриё
    inf = [[], []]
    inf[0].add(base + 'ё')
    inf[0].add(base + 'я́')
    inf[0].add(base + 'ю́')
    inf[0].add(base + 'ё')
    inf[0].add(base + 'ём')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base + 'я́')
    inf[1].add(base + 'ёв')
    inf[1].add(base + 'я́м')
    inf[1].add(base + 'я́')
    inf[1].add(base + 'я́ми')
    inf[1].add(base + 'я́х')
    # end pl
n_funcs['7b(2)'] = q_n_7b2

def q_n_8ar(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # знамя
    inf = [[], []]
    inf[0].add(base + 'я')
    inf[0].add(base + 'ени')
    inf[0].add(base + 'ени')
    inf[0].add(base + 'я')
    inf[0].add(base + 'енем')
    inf[0].add(base + 'ени')
    # end sg
    inf[1].add(base + 'ёна')
    inf[1].add(base + 'ён')
    inf[1].add(base + 'ёнам')
    inf[1].add(base + 'ёна')
    inf[1].add(base + 'ёнами')
    inf[1].add(base + 'ёнах')
    # end pl
n_funcs['8°a'] = q_n_8ar

def q_n_8cr(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # племя
    inf = [[], []]
    inf[0].add(base + 'я')
    inf[0].add(base + 'ени')
    inf[0].add(base + 'ени')
    inf[0].add(base + 'я')
    inf[0].add(base + 'енем')
    inf[0].add(base + 'ени')
    # end sg
    inf[1].add(base1 + 'ена́')
    inf[1].add(base2)
    inf[1].add(base1 + 'ена́м')
    inf[1].add(base1 + 'ена́')
    inf[1].add(base1 + 'ена́ми')
    inf[1].add(base1 + 'ена́х')
    # end pl
n_funcs['8°c'] = q_n_8cr

def q_n_8crV(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # племя
    inf = [[], []]
    inf[0].add(base + 'я')
    inf[0].add(base + 'ени')
    inf[0].add(base + 'ени')
    inf[0].add(base + 'я')
    inf[0].add(base + 'енем')
    inf[0].add(base + 'ени')
    # end sg
    inf[1].add(base1 + 'ена́')
    inf[1].add(base1 + 'я́н')
    inf[1].add(base1 + 'ена́м')
    inf[1].add(base1 + 'ена́')
    inf[1].add(base1 + 'ена́ми')
    inf[1].add(base1 + 'ена́х')
    # end pl
n_funcs['8°c^'] = q_n_8crV

# 8°c- - бремя - обрабатывается обычным способом, через 8°c
