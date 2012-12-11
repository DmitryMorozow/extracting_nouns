m_funcs = {}

def q_m_1a(animacy, base, base1 = None, base2 = None):
    # ветеринар, завод
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'ы')
    inf[1].add(base + 'ов')
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base + 'ов')
    else:
        inf[1].add(base + 'ы')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
m_funcs['1a'] = q_m_1a

def q_m_1aV(animacy, base, base1 = None, base2 = None):
    # брат, брус
    inf = [[], []]
    if animacy:
        inf[0].add(base)
        inf[0].add(base + 'а')
        inf[0].add(base + 'у')
        inf[0].add(base + 'а')
        inf[0].add(base + 'ом')
        inf[0].add(base + 'е')
        # end sg
        inf[1].add(base + 'и')
        inf[1].add(base + 'ей')
        inf[1].add(base + 'ям')
        inf[1].add(base + 'ей')
        inf[1].add(base + 'ями')
        inf[1].add(base + 'ях')
        # end pl
    else:
        inf[0].add(base)
        inf[0].add(base + 'а')
        inf[0].add(base + 'у')
        inf[0].add(base)
        inf[0].add(base + 'ом')
        inf[0].add(base + 'е')
        # end sg
        inf[1].add(base + 'ья')
        inf[1].add(base + 'ьев')
        inf[1].add(base + 'ьям')
        inf[1].add(base + 'ья')
        inf[1].add(base + 'ьями')
        inf[1].add(base + 'ьях')
        # end pl
m_funcs['1a^'] = q_m_1aV

def q_m_1aV_q(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # Animacy == True
    # брат??
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'а')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'ья')
    inf[1].add(base + 'ьев')
    inf[1].add(base + 'ьям')
    inf[1].add(base + 'ья')
    inf[1].add(base + 'ьями')
    inf[1].add(base + 'ьях')
    # end pl
m_funcs['1a^-ь'] = q_m_1aV_q

# 1a- обрабатывается по правилам 1a

def q_m_1a_2_(animacy, base, base1 = None, base2 = None):
    # грузин, мадьяр, алтын
    inf = [[], []]
    if animacy:
        inf[0].add(base)
        inf[0].add(base + 'а')
        inf[0].add(base + 'у')
        inf[0].add(base + 'а')
        inf[0].add(base + 'ом')
        inf[0].add(base + 'е')
        # end sg
        inf[1].add(base + 'ы')
        inf[1].add(base)
        inf[1].add(base + 'ам')
        inf[1].add(base)
        inf[1].add(base + 'ами')
        inf[1].add(base + 'ах')
        # end pl
    else:
        inf[0].add(base)
        inf[0].add(base + 'а')
        inf[0].add(base + 'у')
        inf[0].add(base)
        inf[0].add(base + 'ом')
        inf[0].add(base + 'е')
        # end sg
        inf[1].add(base + 'ы')
        inf[1].add(base)
        inf[1].add(base + 'ам')
        inf[1].add(base + 'ы')
        inf[1].add(base + 'ами')
        inf[1].add(base + 'ах')
        # end pl
m_funcs['1a(2)'] = q_m_1a_2_

def q_m_1a__2__(animacy, base, base1 = None, base2 = None):
    # баклажан, басурман
    inf = [[], []]
    if animacy:
        inf[0].add(base)
        inf[0].add(base + 'а')
        inf[0].add(base + 'у')
        inf[0].add(base + 'а')
        inf[0].add(base + 'ом')
        inf[0].add(base + 'е')
        # end sg
        inf[1].add(base + 'ы')
        inf[1].add(base)
        inf[1].add(base + 'ам')
        inf[1].add(base)
        inf[1].add(base + 'ами')
        inf[1].add(base + 'ах')
        # end pl
    else:
        inf[0].add(base)
        inf[0].add(base + 'а')
        inf[0].add(base + 'у')
        inf[0].add(base)  # http://ru.wiktionary.org/wiki/Шаблон:сущ_ru_m_ina_1a((2)) is probably broken!
        inf[0].add(base + 'ом')
        inf[0].add(base + 'е')
        # end sg
        inf[1].add(base + 'ы')
        inf[1].add(base)
        inf[1].add(base + 'ам')
        inf[1].add(base + 'ы')
        inf[1].add(base + 'ами')
        inf[1].add(base + 'ах')
        # end pl
m_funcs['1a((2))'] = q_m_1a__2__

def q_m_1a_2_V(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # Animacy == True
    # цыган
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'а')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'е')
    inf[1].add(base)
    inf[1].add(base + 'ам')
    inf[1].add(base)
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl
m_funcs['1a(2)^'] = q_m_1a_2_V

def q_m_1as(animacy, base, base1 = None, base2 = None):
    # бубен, свёкор
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а')
    inf[0].add(base1 + 'у')
    if animacy:
        inf[0].add(base1 + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'ом')
    inf[0].add(base1 + 'е')
    # end sg
    inf[1].add(base1 + 'ы')
    inf[1].add(base1 + 'ов')
    inf[1].add(base1 + 'ам')
    if animacy:
        inf[1].add(base1 + 'ов')
    else:
        inf[1].add(base1 + 'ы')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl
m_funcs['1*a'] = q_m_1as

def q_m_1asV(animacy, base, base1 = None, base2 = None):
    # animacy unused
    # заём
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а')
    inf[0].add(base1 + 'у')
    inf[0].add(base)
    inf[0].add(base1 + 'ом')
    inf[0].add(base1 + 'е')
    # end sg
    inf[1].add(base1 + 'ы')
    inf[1].add(base1 + 'ов')
    inf[1].add(base1 + 'ам')
    inf[1].add(base1 + 'ы')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl
m_funcs['1*a^'] = q_m_1asV

def q_m_1ar(animacy, base, base1 = None, base2 = None):
    # гражданин, римлянин
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'е')
    inf[1].add(base1)
    inf[1].add(base1 + 'ам')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base1 + 'е')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl
m_funcs['1°a'] = q_m_1ar

def q_m_1arV(animacy, base, base1 = None, base2 = None):
    assert animacy == True
    # барин
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'а')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'ы')
    inf[1].add(base1)
    inf[1].add(base1 + 'ам')
    inf[1].add(base1)
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl
m_funcs['1°a^'] = q_m_1arV

def q_m__1a_(animacy, base, base1 = None, base2 = None):
    assert animacy == False
    # газы
    inf = [[], []]
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    # end sg
    inf[1].add(base + 'ы')
    inf[1].add(base + 'ов')
    inf[1].add(base + 'ам')
    inf[1].add(base + 'ы')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ам')
    # end pl
m_funcs['(1a)'] = q_m__1a_

def q_m__1aV_(animacy, base, base1 = None, base2 = None):
    assert animacy == False
    # брусья
    inf = [[], []]
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    # end sg
    inf[1].add(base + 'ья')
    inf[1].add(base + 'ьев')
    inf[1].add(base + 'ьям')
    inf[1].add(base + 'ья')
    inf[1].add(base + 'ьями')
    inf[1].add(base + 'ьях')
    # end pl
m_funcs['(1aV)'] = q_m__1aV_

def q_m_1b(animacy, base, base1 = None, base2 = None):
    # бегун, топор
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а́')
    inf[0].add(base1 + 'у́')
    if animacy:
        inf[0].add(base1 + 'а́')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'о́м')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base1 + 'ы́')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'о́в')
    else:
        inf[1].add(base1 + 'ы́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
m_funcs['1b'] = q_m_1b

# 1b- обрабатывается правилами 1b

def q_m_1bV(animacy, base, base1 = None, base2 = None):
    assert animacy == True
    # христос
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а́')
    inf[0].add(base1 + 'у́')
    inf[0].add(base1 + 'а́')
    inf[0].add(base1 + 'о́м')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base1 + 'ы́')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
m_funcs['1bV'] = q_m_1bV

def q_m_1bq(animacy, base, base1 = None, base2 = None):
    assert animacy == True
    # мулла
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'ы́')
    inf[0].add(base + 'е́')
    inf[0].add(base + 'у́')
    inf[0].add(base + 'о́й')  # вариант base1 + 'о́ю'
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base + 'ы́')
    inf[1].add(base1)
    inf[1].add(base + 'а́м')
    inf[1].add(base1)
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl
m_funcs['1b?'] = q_m_1bq

def q_m_1bs(animacy, base, base1 = None, base2 = None):
    # узел
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а́')
    inf[0].add(base1 + 'у́')
    if animacy:
        inf[0].add(base1 + 'а́')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'о́м')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base1 + 'ы́')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'о́в')
    else:
        inf[1].add(base1 + 'ы́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
m_funcs['1*b'] = q_m_1bs

def q_m__1b_(animacy, base, base1 = None, base2 = None):
    assert animacy == False
    # дрова
    inf = [[], []]
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    inf[0].add(None)
    # end sg
    inf[1].add(base1 + 'ы́')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    inf[1].add(base1 + 'ы́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
m_funcs['(1b)'] = q_m__1b_

def q_m_1c(animacy, base, base1 = None, base2 = None):
    # дар
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'ы́')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'о́в')
    else:
        inf[1].add(base1 + 'ы́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
m_funcs['1c'] = q_m_1c

def q_m_1cV(animacy, base, base1 = None, base2 = None):
    assert animacy == True
    # граф
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'а')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'ья́')
    inf[1].add(base2)
    inf[1].add(base1 + 'ья́м')
    inf[1].add(base2)
    inf[1].add(base1 + 'ья́ми')
    inf[1].add(base1 + 'ья́х')
    # end pl
m_funcs['1c^'] = q_m_1cV

def q_m_1c_1_(animacy, base, base1 = None, base2 = None):
    # борт, боцман
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'а́')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'о́в')
    else:
        inf[1].add(base1 + 'а́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
m_funcs['1c(1)'] = q_m_1c_1_

def q_m_1c_1_V(animacy, base, base1 = None, base2 = None):
    assert animacy == False
    # год, перёд
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а')
    inf[0].add(base1 + 'у')
    inf[0].add(base)  # http://ru.wiktionary.org/wiki/Шаблон:сущ_ru_m_ina_1c(1)^ has an error
    inf[0].add(base1 + 'ом')
    inf[0].add(base1 + 'е')
    # end sg
    inf[1].add(base2 + 'а́')
    inf[1].add(base3)
    inf[1].add(base2 + 'а́м')
    inf[1].add(base2 + 'а́')
    inf[1].add(base2 + 'а́ми')
    inf[1].add(base2 + 'а́х')
    # end pl
m_funcs['1c(1)^'] = q_m_1c_1_V

def q_m_1c_2_(animacy, base, base1 = None, base2 = None):
    assert animacy == False
    # раз
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base)
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'ы́')
    inf[1].add(base)
    inf[1].add(base1 + 'а́м')
    inf[1].add(base1 + 'ы́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
m_funcs['1c(2)'] = q_m_1c_2_

def q_m_1c_1__2_(animacy, base, base1 = None, base2 = None):
    assert animacy == False
    # глаз, глаза
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base)
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'а́')
    inf[1].add(base1)
    inf[1].add(base1 + 'а́м')
    inf[1].add(base1 + 'а́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
m_funcs['1c(1)(2)'] = q_m_1c_1__2_

def q_m_1cs_1_(animacy, base, base1 = None, base2 = None):
    assert animacy == False
    # ветер
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а')
    inf[0].add(base1 + 'у')
    inf[0].add(base)
    inf[0].add(base1 + 'ом')
    inf[0].add(base1 + 'е')
    # end sg
    inf[1].add(base2 + 'а́')
    inf[1].add(base2 + 'о́в')
    inf[1].add(base2 + 'а́м')
    inf[1].add(base2 + 'а́')
    inf[1].add(base2 + 'а́ми')
    inf[1].add(base2 + 'а́х')
    # end pl
m_funcs['1*c(1)'] = q_m_1cs_1_

def q_m_1cr1(animacy, base, base1 = None, base2 = None):
    assert animacy == True
    # господин
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    inf[0].add(base + 'а')
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'а́')
    inf[1].add(base2)
    inf[1].add(base1 + 'а́м')
    inf[1].add(base1)
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
m_funcs['1°c(1)'] = q_m_1cr1

def q_m_1dV(animacy, base, base1 = None, base2 = None):
    assert animacy == False
    # кол
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а́')
    inf[0].add(base1 + 'у́')
    inf[0].add(base)
    inf[0].add(base1 + 'о́м')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base + 'ья')
    inf[1].add(base + 'ьев')
    inf[1].add(base + 'ьям')
    inf[1].add(base + 'ья')
    inf[1].add(base + 'ьями')
    inf[1].add(base + 'ьях')
    # end pl
m_funcs['1d^'] = q_m_1dV

def q_m_2a(animacy, base, base1 = None, base2 = None):
    # портфель, житель
    inf = [[], []]
    inf[0].add(base + 'ь')
    inf[0].add(base + 'я')
    inf[0].add(base + 'ю')
    if animacy:
        inf[0].add(base + 'я')
    else:
        inf[0].add(base + 'ь')
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base + 'ей')
    inf[1].add(base + 'ям')
    if animacy:
        inf[1].add(base + 'ей')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ями')
    inf[1].add(base + 'ях')
    # end pl

def q_m_3a(animacy, base, base1 = None, base2 = None):
    # бульдог, чайник
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base + 'ов')
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base + 'ов')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl

def q_m_4a(animacy, base, base1 = None, base2 = None):
    # товарищ, марш
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base + 'ей')
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base + 'ей')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl

def q_m_5a(animacy, base, base1 = None, base2 = None):
    # принц, месяц
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'ы')
    inf[1].add(base + 'ев')
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base + 'ев')
    else:
        inf[1].add(base + 'ы')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl

def q_m_6a(animacy, base, base1 = None, base2 = None):
    # герой, случай
    inf = [[], []]
    inf[0].add(base + 'й')
    inf[0].add(base + 'я')
    inf[0].add(base + 'ю')
    if animacy:
        inf[0].add(base + 'я')
    else:
        inf[0].add(base + 'й')
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base + 'ев')
    inf[1].add(base + 'ям')
    if animacy:
        inf[1].add(base + 'ев')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ями')
    inf[1].add(base + 'ях')
    # end pl

def q_m_7a(animacy, base, base1 = None, base2 = None):
    # викарий, гербарий
    inf = [[], []]
    inf[0].add(base + 'й')
    inf[0].add(base + 'я')
    inf[0].add(base + 'ю')
    if animacy:
        inf[0].add(base + 'я')
    else:
        inf[0].add(base + 'й')
    inf[0].add(base + 'ем')
    inf[0].add(base + 'и')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base + 'ев')
    inf[1].add(base + 'ям')
    if animacy:
        inf[1].add(base + 'ев')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ями')
    inf[1].add(base + 'ях')
    # end pl

def q_m_2b(animacy, base, base1 = None, base2 = None):
    # карась, словарь
    inf = [[], []]
    inf[0].add(base + 'ь')
    inf[0].add(base1 + 'я́')
    inf[0].add(base1 + 'ю́')
    if animacy:
        inf[0].add(base1 + 'я́')
    else:
        inf[0].add(base + 'ь')
    inf[0].add(base1 + 'ём')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'е́й')
    inf[1].add(base1 + 'я́м')
    if animacy:
        inf[1].add(base1 + 'е́й')
    else:
        inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'я́ми')
    inf[1].add(base1 + 'я́х')
    # end pl

def q_m_3b(animacy, base, base1 = None, base2 = None):
    # рыбак, пирог
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а́')
    inf[0].add(base1 + 'у́')
    if animacy:
        inf[0].add(base1 + 'а́')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'о́м')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'о́в')
    else:
        inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

def q_m_4b(animacy, base, base1 = None, base2 = None):
    # нож, богач
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а́')
    inf[0].add(base1 + 'у́')
    if animacy:
        inf[0].add(base1 + 'а́')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'о́м')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'е́й')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'е́й')
    else:
        inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

def q_m_5b(animacy, base, base1 = None, base2 = None):
    # кузнец, кострец
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а́')
    inf[0].add(base1 + 'у́')
    if animacy:
        inf[0].add(base1 + 'а́')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'о́м')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base1 + 'ы́')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'о́в')
    else:
        inf[1].add(base1 + 'ы́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

def q_m_6b(animacy, base, base1 = None, base2 = None):
    # холуй, лишай
    inf = [[], []]
    inf[0].add(base + 'й')
    inf[0].add(base1 + 'я́')
    inf[0].add(base1 + 'ю́')
    if animacy:
        inf[0].add(base1 + 'я́')
    else:
        inf[0].add(base + 'й')
    inf[0].add(base1 + 'ём')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'ёв')
    inf[1].add(base1 + 'я́м')
    if animacy:
        inf[1].add(base1 + 'ёв')
    else:
        inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'я́ми')
    inf[1].add(base1 + 'я́х')
    # end pl

def q_m_7b(animacy, base, base1 = None, base2 = None):
    # кий
    inf = [[], []]
    inf[0].add(base + 'й')
    inf[0].add(base1 + 'я́')
    inf[0].add(base1 + 'ю́')
    if animacy:
        inf[0].add(base1 + 'я́')
    else:
        inf[0].add(base + 'й')
    inf[0].add(base1 + 'ём')
    inf[0].add(base1 + 'и́')
    # end sg
    inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'ёв')
    inf[1].add(base1 + 'я́м')
    if animacy:
        inf[1].add(base1 + 'ёв')
    else:
        inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'я́ми')
    inf[1].add(base1 + 'я́х')
    # end pl

def q_m_3c(animacy, base, base1 = None, base2 = None):
    # плуг
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'о́в')
    else:
        inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

def q_m_4c(animacy, base, base1 = None, base2 = None):
    # харч
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'е́й')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'е́й')
    else:
        inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

def q_m_6c(animacy, base, base1 = None, base2 = None):
    # буй
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'ёв')
    inf[1].add(base1 + 'я́м')
    if animacy:
        inf[1].add(base1 + 'ёв')
    else:
        inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'я́ми')
    inf[1].add(base1 + 'я́х')
    # end pl

def q_m_7c(animacy, base, base1 = None, base2 = None):
    # кий
    inf = [[], []]
    inf[0].add(base + 'й')
    inf[0].add(base + 'я')
    inf[0].add(base + 'ю')
    if animacy:
        inf[0].add(base + 'я')
    else:
        inf[0].add(base + 'й')
    inf[0].add(base + 'ем')
    inf[0].add(base + 'и')
    # end sg
    inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'ёв')
    inf[1].add(base1 + 'я́м')
    if animacy:
        inf[1].add(base1 + 'ёв')
    else:
        inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'я́ми')
    inf[1].add(base1 + 'я́х')
    # end pl

def q_m_3d(animacy, base, base1 = None, base2 = None):
    # казак
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а́')
    inf[0].add(base1 + 'у́')
    if animacy:
        inf[0].add(base1 + 'а́')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'о́м')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base + 'ов')
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base + 'ов')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl

def q_m_1e(animacy, base, base1 = None, base2 = None):
    # зуб
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'ы')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'о́в')
    else:
        inf[1].add(base + 'ы')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

def q_m_2e(animacy, base, base1 = None, base2 = None):
    # голубь
    inf = [[], []]
    inf[0].add(base + 'ь')
    inf[0].add(base + 'я')
    inf[0].add(base + 'ю')
    if animacy:
        inf[0].add(base + 'я')
    else:
        inf[0].add(base + 'ь')
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base1 + 'е́й')
    inf[1].add(base1 + 'я́м')
    if animacy:
        inf[1].add(base1 + 'е́й')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base1 + 'я́ми')
    inf[1].add(base1 + 'я́х')
    # end pl

def q_m_3e(animacy, base, base1 = None, base2 = None):
    # волк, слог
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'о́в')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

def q_m_4e(animacy, base, base1 = None, base2 = None):
    # обруч
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base1 + 'е́й')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'е́й')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

def q_m_2f(animacy, base, base1 = None, base2 = None):
    # конь
    inf = [[], []]
    inf[0].add(base + 'ь')
    inf[0].add(base1 + 'я́')
    inf[0].add(base1 + 'ю́')
    if animacy:
        inf[0].add(base1 + 'я́')
    else:
        inf[0].add(base + 'ь')
    inf[0].add(base1 + 'ём')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base1 + 'е́й')
    inf[1].add(base1 + 'я́м')
    if animacy:
        inf[1].add(base1 + 'е́й')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base1 + 'я́ми')
    inf[1].add(base1 + 'я́х')
    # end pl

def q_m_1es(animacy, base, base1 = None, base2 = None):
    # ветер
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а')
    inf[0].add(base1 + 'у')
    if animacy:
        inf[0].add(base1 + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'ом')
    inf[0].add(base1 + 'е')
    # end sg
    inf[1].add(base1 + 'ы')
    inf[1].add(base2 + 'о́в')
    inf[1].add(base2 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'о́в')
    else:
        inf[1].add(base1 + 'ы')
    inf[1].add(base2 + 'а́ми')
    inf[1].add(base2 + 'а́х')
    # end pl

def q_m_2as(animacy, base, base1 = None, base2 = None):
    # увалень, ливень
    inf = [[], []]
    inf[0].add(base + 'ь')
    inf[0].add(base1 + 'я')
    inf[0].add(base1 + 'ю')
    if animacy:
        inf[0].add(base1 + 'я')
    else:
        inf[0].add(base1 + 'ь')
    inf[0].add(base1 + 'ем')
    inf[0].add(base1 + 'е')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ей')
    inf[1].add(base1 + 'ям')
    if animacy:
        inf[1].add(base1 + 'ей')
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ями')
    inf[1].add(base1 + 'ях')
    # end pl

def q_m_2bs(animacy, base, base1 = None, base2 = None):
    # угорь, огонь
    inf = [[], []]
    inf[0].add(base + 'ь')
    inf[0].add(base1 + 'я́')
    inf[0].add(base1 + 'ю́')
    if animacy:
        inf[0].add(base1 + 'я́')
    else:
        inf[0].add(base + 'ь')
    inf[0].add(base1 + 'ём')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'е́й')
    inf[1].add(base1 + 'я́м')
    if animacy:
        inf[1].add(base1 + 'е́й')
    else:
        inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'я́ми')
    inf[1].add(base1 + 'я́х')
    # end pl

def q_m_2es(animacy, base, base1 = None, base2 = None):
    # ноготь
    inf = [[], []]
    inf[0].add(base + 'ь')
    inf[0].add(base1 + 'я')
    inf[0].add(base1 + 'ю')
    if animacy:
        inf[0].add(base1 + 'я')
    else:
        inf[0].add(base + 'ь')
    inf[0].add(base1 + 'ем')
    inf[0].add(base1 + 'е')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base2 + 'е́й')
    inf[1].add(base2 + 'я́м')
    if animacy:
        inf[1].add(base2 + 'е́й')
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base2 + 'я́ми')
    inf[1].add(base2 + 'я́х')
    # end pl

def q_m_3as(animacy, base, base1 = None, base2 = None):
    # перешеек
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а')
    inf[0].add(base1 + 'у')
    if animacy:
        inf[0].add(base1 + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'ом')
    inf[0].add(base1 + 'е')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ов')
    inf[1].add(base1 + 'ам')
    if animacy:
        inf[1].add(base1 + 'ов')
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl

def q_m_3bs(animacy, base, base1 = None, base2 = None):
    # хорёк, кусок
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а́')
    inf[0].add(base1 + 'у́')
    if animacy:
        inf[0].add(base1 + 'а́')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'о́м')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'о́в')
    else:
        inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

def q_m_5as(animacy, base, base1 = None, base2 = None):
    # немец, палец
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а')
    inf[0].add(base1 + 'у')
    if animacy:
        inf[0].add(base1 + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'ем')
    inf[0].add(base1 + 'е')
    # end sg
    inf[1].add(base1 + 'ы')
    inf[1].add(base1 + 'ев')
    inf[1].add(base1 + 'ам')
    if animacy:
        inf[1].add(base1 + 'ев')
    else:
        inf[1].add(base1 + 'ы')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl

def q_m_5bs(animacy, base, base1 = None, base2 = None):
    # жилец, конец
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а́')
    inf[0].add(base1 + 'у́')
    if animacy:
        inf[0].add(base1 + 'а́')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'о́м')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base1 + 'ы́')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'о́в')
    else:
        inf[1].add(base1 + 'ы́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

def q_m_6as(animacy, base, base1 = None, base2 = None):
    # улей
    inf = [[], []]
    inf[0].add(base + 'й')
    inf[0].add(base1 + 'я')
    inf[0].add(base1 + 'ю')
    if animacy:
        inf[0].add(base1 + 'я')
    else:
        inf[0].add(base + 'й')
    inf[0].add(base1 + 'ем')
    inf[0].add(base1 + 'е')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ев')
    inf[1].add(base1 + 'ям')
    if animacy:
        inf[1].add(base1 + 'ев')
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ями')
    inf[1].add(base1 + 'ях')
    # end pl

def q_m_6bs(animacy, base, base1 = None, base2 = None):
    # муравей
    inf = [[], []]
    inf[0].add(base + 'й')
    inf[0].add(base1 + 'я́')
    inf[0].add(base1 + 'ю́')
    if animacy:
        inf[0].add(base1 + 'я́')
    else:
        inf[0].add(base + 'й')
    inf[0].add(base1 + 'ём')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'ёв')
    inf[1].add(base1 + 'я́м')
    if animacy:
        inf[1].add(base1 + 'ёв')
    else:
        inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'я́ми')
    inf[1].add(base1 + 'я́х')
    # end pl

def q_m_3ar(animacy, base, base1 = None, base2 = None):
    # цыплёнок
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base2 + 'а')
    inf[0].add(base2 + 'у')
    if animacy:
        inf[0].add(base2 + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base2 + 'ом')
    inf[0].add(base2 + 'е')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ов')
    inf[1].add(base1 + 'ам')
    if animacy:
        inf[1].add(base1 + 'ов')
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl

def q_m_3br(animacy, base, base1 = None, base2 = None):
    # щенок
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а́')
    inf[0].add(base1 + 'у́')
    if animacy:
        inf[0].add(base1 + 'а́')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'о́м')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base2 + 'а')
    inf[1].add(base2)
    inf[1].add(base2 + 'ам')
    if animacy:
        inf[1].add(base2)
    else:
        inf[1].add(base2 + 'а')
    inf[1].add(base2 + 'ами')
    inf[1].add(base2 + 'ах')
    # second option
    inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'о́в')
    else:
        inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

def q_m_3c1(animacy, base, base1 = None, base2 = None):
    # снег, округ
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base1 + 'а́')
    inf[1].add(base1 + 'о́в')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'о́в')
    else:
        inf[1].add(base1 + 'а́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

def q_m_1e2(animacy, base, base1 = None, base2 = None):
    # волос
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ом')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'ы')
    inf[1].add(base1)
    inf[1].add(base2 + 'а́м')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base + 'ы')
    inf[1].add(base2 + 'а́ми')
    inf[1].add(base2 + 'а́х')
    # end pl

def q_m_3b2(animacy, base, base1 = None, base2 = None):
    # сапог
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а́')
    inf[0].add(base1 + 'у́')
    if animacy:
        inf[0].add(base1 + 'а́')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'о́м')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base1 + 'и́')
    inf[1].add(base)
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base)
    else:
        inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

def q_m_5a2(animacy, base, base1 = None, base2 = None):
    # герц
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base + 'ем')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'ы')
    inf[1].add(base)
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base + 'ев')
    else:
        inf[1].add(base + 'ы')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl

def q_m_3as2(animacy, base, base1 = None, base2 = None):
    # черевичек
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а')
    inf[0].add(base1 + 'у')
    if animacy:
        inf[0].add(base1 + 'а')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'ом')
    inf[0].add(base1 + 'е')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base)
    inf[1].add(base1 + 'ам')
    if animacy:
        inf[1].add(base)
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl

def q_m_3bs2(animacy, base, base1 = None, base2 = None):
    # чулок
    inf = [[], []]
    inf[0].add(base)
    inf[0].add(base1 + 'а́')
    inf[0].add(base1 + 'у́')
    if animacy:
        inf[0].add(base1 + 'а́')
    else:
        inf[0].add(base)
    inf[0].add(base1 + 'о́м')
    inf[0].add(base1 + 'е́')
    # end sg
    inf[1].add(base1 + 'и́')
    inf[1].add(base)
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base)
    else:
        inf[1].add(base1 + 'и́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################

def q_f_1a(animacy, base, base1 = None, base2 = None):
    # корова, лопата
    inf = [[], []]
    inf[0].add(base + 'а')
    inf[0].add(base + 'ы')
    inf[0].add(base + 'е')
    if animacy:
        inf[0].add(base + 'у')
    else:
        inf[0].add(base + 'у')
    inf[0].add(base + 'ой')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'ы')
    inf[1].add(base)
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base)
    else:
        inf[1].add(base + 'ы')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl

def q_f_2a(animacy, base, base1 = None, base2 = None):
    # богиня, неделя
    inf = [[], []]
    inf[0].add(base + 'я')
    inf[0].add(base + 'и')
    inf[0].add(base + 'е')
    if animacy:
        inf[0].add(base + 'ю')
    else:
        inf[0].add(base + 'ю')
    inf[0].add(base + 'ей')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base + 'ь')
    inf[1].add(base + 'ям')
    if animacy:
        inf[1].add(base + 'ь')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ями')
    inf[1].add(base + 'ях')
    # end pl

def q_f_3a(animacy, base, base1 = None, base2 = None):
    # собака, книга
    inf = [[], []]
    inf[0].add(base + 'а')
    inf[0].add(base + 'и')
    inf[0].add(base + 'е')
    if animacy:
        inf[0].add(base + 'у')
    else:
        inf[0].add(base + 'у')
    inf[0].add(base + 'ой')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base)
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base)
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl

def q_f_4a(animacy, base, base1 = None, base2 = None):
    # кассирша, туча
    inf = [[], []]
    inf[0].add(base + 'а')
    inf[0].add(base + 'и')
    inf[0].add(base + 'е')
    if animacy:
        inf[0].add(base + 'у')
    else:
        inf[0].add(base + 'у')
    inf[0].add(base + 'ей')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base + 'ей')
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base)
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl

def q_f_5a(animacy, base, base1 = None, base2 = None):
    # улица, проводница
    inf = [[], []]
    inf[0].add(base + 'а')
    inf[0].add(base + 'ы')
    inf[0].add(base + 'е')
    if animacy:
        inf[0].add(base + 'у')
    else:
        inf[0].add(base + 'у')
    inf[0].add(base + 'ей')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'ы')
    inf[1].add(base)
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base)
    else:
        inf[1].add(base + 'ы')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl

def q_f_6a(animacy, base, base1 = None, base2 = None):
    # фея, статуя
    inf = [[], []]
    inf[0].add(base + 'я')
    inf[0].add(base + 'и')
    inf[0].add(base + 'е')
    if animacy:
        inf[0].add(base + 'ю')
    else:
        inf[0].add(base + 'ю')
    inf[0].add(base + 'ей')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base + 'й')
    inf[1].add(base + 'ям')
    if animacy:
        inf[1].add(base + 'й')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ями')
    inf[1].add(base + 'ях')
    # end pl

def q_f_7a(animacy, base, base1 = None, base2 = None):
    # армия, рептилия
    inf = [[], []]
    inf[0].add(base + 'я')
    inf[0].add(base + 'и')
    inf[0].add(base + 'и')
    if animacy:
        inf[0].add(base + 'ю')
    else:
        inf[0].add(base + 'ю')
    inf[0].add(base + 'ей')
    inf[0].add(base + 'и')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base + 'й')
    inf[1].add(base + 'ям')
    if animacy:
        inf[1].add(base + 'й')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ями')
    inf[1].add(base + 'ях')
    # end pl

def q_f_1b(animacy, base, base1 = None, base2 = None):
    # гюрза, похвала
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'ы́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'у́')
    else:
        inf[0].add(base + 'у́')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base + 'ы́')
    inf[1].add(base1)
    inf[1].add(base + 'а́м')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base + 'ы́')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl

def q_f_2b(animacy, base, base1 = None, base2 = None):
    # тля, стезя
    inf = [[], []]
    inf[0].add(base + 'я́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'ю́')
    else:
        inf[0].add(base + 'ю́')
    inf[0].add(base + 'ёй')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base + 'и́')
    inf[1].add(base + 'е́й')
    inf[1].add(base + 'я́м')
    if animacy:
        inf[1].add(base + 'е́й')
    else:
        inf[1].add(base + 'и́')
    inf[1].add(base + 'я́ми')
    inf[1].add(base + 'я́х')
    # end pl

def q_f_3b(animacy, base, base1 = None, base2 = None):
    # карга, острога
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'у́')
    else:
        inf[0].add(base + 'у́')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base + 'и́')
    inf[1].add(base1)
    inf[1].add(base + 'а́м')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base + 'и́')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl

def q_f_4b(animacy, base, base1 = None, base2 = None):
    # ханжа, каланча
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'у́')
    else:
        inf[0].add(base + 'у́')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base + 'и́')
    inf[1].add(base + 'е́й')
    inf[1].add(base + 'а́м')
    if animacy:
        inf[1].add(base + 'е́й')
    else:
        inf[1].add(base + 'и́')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl

def q_f_6b(animacy, base, base1 = None, base2 = None):
    # швея, колея
    inf = [[], []]
    inf[0].add(base + 'я́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'ю́')
    else:
        inf[0].add(base + 'ю́')
    inf[0].add(base + 'ёй')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base + 'и́')
    inf[1].add(base1 + 'й')
    inf[1].add(base + 'я́м')
    if animacy:
        inf[1].add(base1 + 'й')
    else:
        inf[1].add(base + 'и́')
    inf[1].add(base + 'я́ми')
    inf[1].add(base + 'я́х')
    # end pl

def q_f_7b(animacy, base, base1 = None, base2 = None):
    # судия, лития
    inf = [[], []]
    if animacy:
        inf[0].add(base + 'ия́')
    else:
        inf[0].add(base + 'я́')
    if animacy:
        inf[0].add(base + 'ии́')
    else:
        inf[0].add(base + 'и́')
    if animacy:
        inf[0].add(base + 'ии́')
    else:
        inf[0].add(base + 'и́')
    if animacy:
        inf[0].add(base + 'и́ю')
    else:
        inf[0].add(base + 'и́ю')
    if animacy:
        inf[0].add(base + 'иёю')
    else:
        inf[0].add(base + 'е́ю')
    if animacy:
        inf[0].add(base + 'ии́')
    else:
        inf[0].add(base + 'и')
    # end sg
    if animacy:
        inf[0].add(base + 'ии́')
    else:
        inf[0].add(base + 'и́')
    if animacy:
        inf[0].add(base + 'и́й')
    else:
        inf[0].add(base1 + 'й')
    if animacy:
        inf[0].add(base + 'ия́м')
    else:
        inf[0].add(base + 'я́м')
    if animacy:
        inf[0].add(base + 'ии́')
    else:
        inf[0].add(base + 'и́')
    if animacy:
        inf[0].add(base + 'ия́ми')
    else:
        inf[0].add(base + 'я́ми')
    if animacy:
        inf[0].add(base + 'ия́х')
    else:
        inf[0].add(base + 'я́х')
    # end pl

def q_f_1d(animacy, base, base1 = None, base2 = None):
    # красота, сирота
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'ы́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'у́')
    else:
        inf[0].add(base + 'у́')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'ы')
    inf[1].add(base1)
    inf[1].add(base1 + 'ам')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base1 + 'ы')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl

def q_f_2d(animacy, base, base1 = None, base2 = None):
    # заря
    inf = [[], []]
    inf[0].add(base + 'я́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е')
    if animacy:
        inf[0].add(base + 'ю́')
    else:
        inf[0].add(base + 'ю́')
    inf[0].add(base + 'ёй')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ь')
    inf[1].add(base1 + 'ям')
    if animacy:
        inf[1].add(base1 + 'ь')
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ями')
    inf[1].add(base1 + 'ях')
    # end pl

def q_f_3d(animacy, base, base1 = None, base2 = None):
    # слуга, дуга
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'у́')
    else:
        inf[0].add(base + 'у́')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base1)
    inf[1].add(base1 + 'ам')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl

def q_f_4d(animacy, base, base1 = None, base2 = None):
    # межа
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'у́')
    else:
        inf[0].add(base + 'у́')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ей')
    inf[1].add(base1 + 'ам')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl

def q_f_6d (animacy, base, base1 = None, base2 = None):
    # змея
    inf = [[], []]
    inf[0].add(base + 'я́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'ю́')
    else:
        inf[0].add(base + 'ю́')
    inf[0].add(base + 'ёй')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'й')
    inf[1].add(base1 + 'ям')
    if animacy:
        inf[1].add(base1 + 'й')
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ями')
    inf[1].add(base1 + 'ях')
    # end pl

def q_f_1dt(animacy, base, base1 = None, base2 = None):
    # спина, зима
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'ы́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base1 + 'у')
    else:
        inf[0].add(base1 + 'у')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'ы')
    inf[1].add(base1)
    inf[1].add(base1 + 'ам')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base1 + 'ы')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl

def q_f_3dt(animacy, base, base1 = None, base2 = None):
    # река
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base1 + 'у')
    else:
        inf[0].add(base1 + 'у')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base1)
    inf[1].add(base1 + 'ам')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl

def q_f_4dt(animacy, base, base1 = None, base2 = None):
    # душа
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base1 + 'у')
    else:
        inf[0].add(base1 + 'у')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ей')
    inf[1].add(base1 + 'ам')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl

def q_f_2e(animacy, base, base1 = None, base2 = None):
    # доля
    inf = [[], []]
    inf[0].add(base + 'я')
    inf[0].add(base + 'и')
    inf[0].add(base + 'е')
    if animacy:
        inf[0].add(base + 'ю')
    else:
        inf[0].add(base + 'ю')
    inf[0].add(base + 'ей')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base1 + 'е́й')
    inf[1].add(base1 + 'я́м')
    if animacy:
        inf[1].add(base1 + 'е́й')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base1 + 'я́ми')
    inf[1].add(base1 + 'я́х')
    # end pl

def q_f_1f(animacy, base, base1 = None, base2 = None):
    # губа
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'ы́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'у́')
    else:
        inf[0].add(base + 'у́')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'ы')
    inf[1].add(base1)
    inf[1].add(base + 'а́м')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base1 + 'ы')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl

def q_f_2f(animacy, base, base1 = None, base2 = None):
    # ноздря, простыня
    inf = [[], []]
    inf[0].add(base + 'я́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'ю́')
    else:
        inf[0].add(base + 'ю́')
    inf[0].add(base + 'ёй')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base + 'е́й')
    inf[1].add(base + 'я́м')
    if animacy:
        inf[1].add(base + 'е́й')
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base + 'я́ми')
    inf[1].add(base + 'я́х')
    # end pl

def q_f_3f(animacy, base, base1 = None, base2 = None):
    # слега
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'у́')
    else:
        inf[0].add(base + 'у́')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base2)
    inf[1].add(base + 'а́м')
    if animacy:
        inf[1].add(base2)
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl

def q_f_4f(animacy, base, base1 = None, base2 = None):
    # вожжа
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'у́')
    else:
        inf[0].add(base + 'у́')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base + 'е́й')
    inf[1].add(base + 'а́м')
    if animacy:
        inf[1].add(base)
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl

def q_f_1ft(animacy, base, base1 = None, base2 = None):
    # борода
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'ы́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base1 + 'у')
    else:
        inf[0].add(base1 + 'у')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'ы')
    inf[1].add(base1)
    inf[1].add(base + 'а́м')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base1 + 'ы')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl

def q_f_3ft(animacy, base, base1 = None, base2 = None):
    # щека, рука
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base1 + 'у')
    else:
        inf[0].add(base1 + 'у')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base1)
    inf[1].add(base + 'а́м')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl

def q_f_8a(animacy, base, base1 = None, base2 = None):
    # лань, тетрадь
    inf = [[], []]
    inf[0].add(base + 'ь')
    inf[0].add(base + 'и')
    inf[0].add(base + 'и')
    if animacy:
        inf[0].add(base + 'ь')
    else:
        inf[0].add(base + 'ь')
    inf[0].add(base + 'ью')
    inf[0].add(base + 'и')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base + 'ей')
    inf[1].add(base + 'ям')
    if animacy:
        inf[1].add(base + 'ей')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ями')
    inf[1].add(base + 'ях')
    # end pl

def q_f_8e(animacy, base, base1 = None, base2 = None):
    # стерлядь, площадь
    inf = [[], []]
    inf[0].add(base + 'ь')
    inf[0].add(base + 'и')
    inf[0].add(base + 'и')
    if animacy:
        inf[0].add(base + 'ь')
    else:
        inf[0].add(base + 'ь')
    inf[0].add(base + 'ью')
    inf[0].add(base + 'и')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base1 + 'е́й')
    inf[1].add(base1 + 'я́м')
    if animacy:
        inf[1].add(base1 + 'е́й')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base1 + 'я́ми')
    inf[1].add(base1 + 'я́х')
    # end pl

def q_f_8a_sh(animacy, base, base1 = None, base2 = None):
    # пустошь
    inf = [[], []]
    inf[0].add(base + 'ь')
    inf[0].add(base + 'и')
    inf[0].add(base + 'и')
    if animacy:
        inf[0].add(base + 'ь')
    else:
        inf[0].add(base + 'ь')
    inf[0].add(base + 'ью')
    inf[0].add(base + 'и')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base + 'ей')
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base + 'ей')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl

def q_f_8e_sh(animacy, base, base1 = None, base2 = None):
    # мышь, ночь
    inf = [[], []]
    inf[0].add(base + 'ь')
    inf[0].add(base + 'и')
    inf[0].add(base + 'и')
    if animacy:
        inf[0].add(base + 'ь')
    else:
        inf[0].add(base + 'ь')
    inf[0].add(base + 'ью')
    inf[0].add(base + 'и')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base1 + 'е́й')
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1 + 'е́й')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

def q_f_8ft(animacy, base, base1 = None, base2 = None):
    # грудь
    inf = [[], []]
    inf[0].add(base + 'ь')
    inf[0].add(base1 + 'и́')
    inf[0].add(base1 + 'и́')
    if animacy:
        inf[0].add(base + 'ь')
    else:
        inf[0].add(base + 'ь')
    inf[0].add(base + 'ью')
    inf[0].add(base1 + 'и́')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base1 + 'е́й')
    inf[1].add(base1 + 'я́м')
    if animacy:
        inf[1].add(base1 + 'е́й')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base1 + 'я́ми')
    inf[1].add(base1 + 'я́х')
    # end pl

def q_f_1as(animacy, base, base1 = None, base2 = None):
    # царевна, свадьба
    inf = [[], []]
    inf[0].add(base + 'а')
    inf[0].add(base + 'ы')
    inf[0].add(base + 'е')
    if animacy:
        inf[0].add(base + 'у')
    else:
        inf[0].add(base + 'у')
    inf[0].add(base + 'ой')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'ы')
    inf[1].add(base1)
    inf[1].add(base + 'ам')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base + 'ы')
    inf[1].add(base + 'ами')
    inf[1].add(base + 'ах')
    # end pl

def q_f_1bs(animacy, base, base1 = None, base2 = None):
    # княжна, кайма
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'ы́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'у́')
    else:
        inf[0].add(base + 'у́')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base + 'ы́')
    inf[1].add(base1)
    inf[1].add(base + 'а́м')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base + 'ы́')
    inf[1].add(base + 'а́ми')
    inf[1].add(base + 'а́х')
    # end pl

def q_f_1ds(animacy, base, base1 = None, base2 = None):
    # сестра, весна
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'ы́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'у́')
    else:
        inf[0].add(base + 'у́')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'ы')
    inf[1].add(base2)
    inf[1].add(base1 + 'ам')
    if animacy:
        inf[1].add(base2)
    else:
        inf[1].add(base1 + 'ы')
    inf[1].add(base1 + 'ами')
    inf[1].add(base1 + 'ах')
    # end pl

def q_f_1es(animacy, base, base1 = None, base2 = None):
    # бубна
    inf = [[], []]
    inf[0].add(base + 'а')
    inf[0].add(base + 'ы')
    inf[0].add(base + 'е')
    if animacy:
        inf[0].add(base + 'у')
    else:
        inf[0].add(base + 'у')
    inf[0].add(base + 'ой')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'ы')
    inf[1].add(base1)
    inf[1].add(base2 + 'а́м')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base + 'ы')
    inf[1].add(base2 + 'а́ми')
    inf[1].add(base2 + 'а́х')
    # end pl

def q_f_1fs(animacy, base, base1 = None, base2 = None):
    # копна
    inf = [[], []]
    inf[0].add(base + 'а́')
    inf[0].add(base + 'ы́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'у́')
    else:
        inf[0].add(base + 'у́')
    inf[0].add(base + 'о́й')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'ы')
    inf[1].add(base2)
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base2)
    else:
        inf[1].add(base1 + 'ы')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl

def q_f_2as(animacy, base, base1 = None, base2 = None):
    # цапля, кровля
    inf = [[], []]
    inf[0].add(base + 'я')
    inf[0].add(base + 'и')
    inf[0].add(base + 'е')
    if animacy:
        inf[0].add(base + 'ю')
    else:
        inf[0].add(base + 'ю')
    inf[0].add(base + 'ей')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base1 + 'ь')
    inf[1].add(base + 'ям')
    if animacy:
        inf[1].add(base1 + 'ь')
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ями')
    inf[1].add(base + 'ях')
    # end pl

def q_f_2as_nya(animacy, base, base1 = None, base2 = None):
    # просвирня, песня
    inf = [[], []]
    inf[0].add(base + 'я')
    inf[0].add(base + 'и')
    inf[0].add(base + 'е')
    if animacy:
        inf[0].add(base + 'ю')
    else:
        inf[0].add(base + 'ю')
    inf[0].add(base + 'ей')
    inf[0].add(base + 'е')
    # end sg
    inf[1].add(base + 'и')
    inf[1].add(base1)
    inf[1].add(base + 'ям')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base + 'и')
    inf[1].add(base + 'ями')
    inf[1].add(base + 'ях')
    # end pl

def q_f_2bs(animacy, base, base1 = None, base2 = None):
    # шестерня
    inf = [[], []]
    inf[0].add(base + 'я́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е́')
    if animacy:
        inf[0].add(base + 'ю́')
    else:
        inf[0].add(base + 'ю́')
    inf[0].add(base + 'ёй')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base + 'и́')
    inf[1].add(base + 'е́й')
    inf[1].add(base + 'я́м')
    if animacy:
        inf[1].add(base + 'е́й')
    else:
        inf[1].add(base + 'и́')
    inf[1].add(base + 'я́ми')
    inf[1].add(base + 'я́х')
    # end pl

def q_f_2ds(animacy, base, base1 = None, base2 = None):
    # петля
    inf = [[], []]
    inf[0].add(base + 'я́')
    inf[0].add(base + 'и́')
    inf[0].add(base + 'е')
    if animacy:
        inf[0].add(base + 'ю́')
    else:
        inf[0].add(base + 'ю́')
    inf[0].add(base + 'ёй')
    inf[0].add(base + 'е́')
    # end sg
    inf[1].add(base1 + 'и')
    inf[1].add(base2 + 'ь')
    inf[1].add(base1 + 'ям')
    if animacy:
        inf[1].add(base2 + 'ь')
    else:
        inf[1].add(base1 + 'и')
    inf[1].add(base1 + 'ями')
    inf[1].add(base1 + 'ях')
    # end pl
