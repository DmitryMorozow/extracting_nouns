m_funcs = {}

def q_m_1a(animacy, **b):
    # ветеринар, завод
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа'] + 'ов')
    inf[1].add(b['основа'] + 'ам')
    if animacy:
        inf[1].add(b['основа'] + 'ов')
    else:
        inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа'] + 'ами')
    inf[1].add(b['основа'] + 'ах')
    # end pl
m_funcs['1a'] = q_m_1a

def q_m_1aV(animacy, **b):
    # брат, брус
    inf = [[], []]
    if animacy:
        inf[0].add(b['основа'])
        inf[0].add(b['основа'] + 'а')
        inf[0].add(b['основа'] + 'у')
        inf[0].add(b['основа'] + 'а')
        inf[0].add(b['основа'] + 'ом')
        inf[0].add(b['основа'] + 'е')
        # end sg
        inf[1].add(b['основа'] + 'и')
        inf[1].add(b['основа'] + 'ей')
        inf[1].add(b['основа'] + 'ям')
        inf[1].add(b['основа'] + 'ей')
        inf[1].add(b['основа'] + 'ями')
        inf[1].add(b['основа'] + 'ях')
        # end pl
    else:
        inf[0].add(b['основа'])
        inf[0].add(b['основа'] + 'а')
        inf[0].add(b['основа'] + 'у')
        inf[0].add(b['основа'])
        inf[0].add(b['основа'] + 'ом')
        inf[0].add(b['основа'] + 'е')
        # end sg
        inf[1].add(b['основа'] + 'ья')
        inf[1].add(b['основа'] + 'ьев')
        inf[1].add(b['основа'] + 'ьям')
        inf[1].add(b['основа'] + 'ья')
        inf[1].add(b['основа'] + 'ьями')
        inf[1].add(b['основа'] + 'ьях')
        # end pl
m_funcs['1a^'] = q_m_1aV

def q_m_1aV_q(animacy, **b):
    # animacy unused
    # Animacy == True
    # брат??
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'ья')
    inf[1].add(b['основа'] + 'ьев')
    inf[1].add(b['основа'] + 'ьям')
    inf[1].add(b['основа'] + 'ья')
    inf[1].add(b['основа'] + 'ьями')
    inf[1].add(b['основа'] + 'ьях')
    # end pl
m_funcs['1a^-ь'] = q_m_1aV_q

# 1a- обрабатывается по правилам 1a

def q_m_1a_2_(animacy, **b):
    # грузин, мадьяр, алтын
    inf = [[], []]
    if animacy:
        inf[0].add(b['основа'])
        inf[0].add(b['основа'] + 'а')
        inf[0].add(b['основа'] + 'у')
        inf[0].add(b['основа'] + 'а')
        inf[0].add(b['основа'] + 'ом')
        inf[0].add(b['основа'] + 'е')
        # end sg
        inf[1].add(b['основа'] + 'ы')
        inf[1].add(b['основа'])
        inf[1].add(b['основа'] + 'ам')
        inf[1].add(b['основа'])
        inf[1].add(b['основа'] + 'ами')
        inf[1].add(b['основа'] + 'ах')
        # end pl
    else:
        inf[0].add(b['основа'])
        inf[0].add(b['основа'] + 'а')
        inf[0].add(b['основа'] + 'у')
        inf[0].add(b['основа'])
        inf[0].add(b['основа'] + 'ом')
        inf[0].add(b['основа'] + 'е')
        # end sg
        inf[1].add(b['основа'] + 'ы')
        inf[1].add(b['основа'])
        inf[1].add(b['основа'] + 'ам')
        inf[1].add(b['основа'] + 'ы')
        inf[1].add(b['основа'] + 'ами')
        inf[1].add(b['основа'] + 'ах')
        # end pl
m_funcs['1a(2)'] = q_m_1a_2_

def q_m_1a__2__(animacy, **b):
    # баклажан, басурман
    inf = [[], []]
    if animacy:
        inf[0].add(b['основа'])
        inf[0].add(b['основа'] + 'а')
        inf[0].add(b['основа'] + 'у')
        inf[0].add(b['основа'] + 'а')
        inf[0].add(b['основа'] + 'ом')
        inf[0].add(b['основа'] + 'е')
        # end sg
        inf[1].add(b['основа'] + 'ы')
        inf[1].add(b['основа'])
        inf[1].add(b['основа'] + 'ам')
        inf[1].add(b['основа'])
        inf[1].add(b['основа'] + 'ами')
        inf[1].add(b['основа'] + 'ах')
        # end pl
    else:
        inf[0].add(b['основа'])
        inf[0].add(b['основа'] + 'а')
        inf[0].add(b['основа'] + 'у')
        inf[0].add(b['основа'])  # http://ru.wiktionary.org/wiki/Шаблон:сущ_ru_m_ina_1a((2)) is probably broken!
        inf[0].add(b['основа'] + 'ом')
        inf[0].add(b['основа'] + 'е')
        # end sg
        inf[1].add(b['основа'] + 'ы')
        inf[1].add(b['основа'])
        inf[1].add(b['основа'] + 'ам')
        inf[1].add(b['основа'] + 'ы')
        inf[1].add(b['основа'] + 'ами')
        inf[1].add(b['основа'] + 'ах')
        # end pl
m_funcs['1a((2))'] = q_m_1a__2__

def q_m_1a_2_V(animacy, **b):
    # animacy unused
    # Animacy == True
    # цыган
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'е')
    inf[1].add(b['основа'])
    inf[1].add(b['основа'] + 'ам')
    inf[1].add(b['основа'])
    inf[1].add(b['основа'] + 'ами')
    inf[1].add(b['основа'] + 'ах')
    # end pl
m_funcs['1a(2)^'] = q_m_1a_2_V

def q_m_1as(animacy, **b):
    # бубен, свёкор
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а')
    inf[0].add(b['основа1'] + 'у')
    if animacy:
        inf[0].add(b['основа1'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'ом')
    inf[0].add(b['основа1'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа1'] + 'ов')
    inf[1].add(b['основа1'] + 'ам')
    if animacy:
        inf[1].add(b['основа1'] + 'ов')
    else:
        inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
m_funcs['1*a'] = q_m_1as

def q_m_1asV(animacy, **b):
    # animacy unused
    # заём
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а')
    inf[0].add(b['основа1'] + 'у')
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'ом')
    inf[0].add(b['основа1'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа1'] + 'ов')
    inf[1].add(b['основа1'] + 'ам')
    inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
m_funcs['1*a^'] = q_m_1asV

def q_m_1ar(animacy, **b):
    # гражданин, римлянин
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'е')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа1'] + 'ам')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа1'] + 'е')
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
m_funcs['1°a'] = q_m_1ar

def q_m_1arV(animacy, **b):
    assert animacy == True
    # барин
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа1'] + 'ам')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
m_funcs['1°a^'] = q_m_1arV

def q_m__1a_(animacy, **b):
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
    inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа'] + 'ов')
    inf[1].add(b['основа'] + 'ам')
    inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа'] + 'ами')
    inf[1].add(b['основа'] + 'ам')
    # end pl
m_funcs['(1a)'] = q_m__1a_

def q_m__1aV_(animacy, **b):
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
    inf[1].add(b['основа'] + 'ья')
    inf[1].add(b['основа'] + 'ьев')
    inf[1].add(b['основа'] + 'ьям')
    inf[1].add(b['основа'] + 'ья')
    inf[1].add(b['основа'] + 'ьями')
    inf[1].add(b['основа'] + 'ьях')
    # end pl
m_funcs['(1aV)'] = q_m__1aV_

def q_m_1b(animacy, **b):
    # бегун, топор
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а́')
    inf[0].add(b['основа1'] + 'у́')
    if animacy:
        inf[0].add(b['основа1'] + 'а́')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'о́м')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'ы́')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'о́в')
    else:
        inf[1].add(b['основа1'] + 'ы́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['1b'] = q_m_1b

# 1b- обрабатывается правилами 1b

def q_m_1bV(animacy, **b):
    assert animacy == True
    # христос
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а́')
    inf[0].add(b['основа1'] + 'у́')
    inf[0].add(b['основа1'] + 'а́')
    inf[0].add(b['основа1'] + 'о́м')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'ы́')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́м')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['1bV'] = q_m_1bV

def q_m_1bq(animacy, **b):
    assert animacy == True
    # мулла
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ы́')
    inf[0].add(b['основа'] + 'е́')
    inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')  # вариант b['основа1'] + 'о́ю'
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа'] + 'ы́')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа'] + 'а́м')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа'] + 'а́ми')
    inf[1].add(b['основа'] + 'а́х')
    # end pl
m_funcs['1b?'] = q_m_1bq

def q_m_1bs(animacy, **b):
    # узел
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а́')
    inf[0].add(b['основа1'] + 'у́')
    if animacy:
        inf[0].add(b['основа1'] + 'а́')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'о́м')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'ы́')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'о́в')
    else:
        inf[1].add(b['основа1'] + 'ы́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['1*b'] = q_m_1bs

def q_m__1b_(animacy, **b):
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
    inf[1].add(b['основа1'] + 'ы́')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́м')
    inf[1].add(b['основа1'] + 'ы́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['(1b)'] = q_m__1b_

def q_m_1c(animacy, **b):
    # дар
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'ы́')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'о́в')
    else:
        inf[1].add(b['основа1'] + 'ы́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['1c'] = q_m_1c

def q_m_1cV(animacy, **b):
    assert animacy == True
    # граф
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'ья́')
    inf[1].add(b['основа2'])
    inf[1].add(b['основа1'] + 'ья́м')
    inf[1].add(b['основа2'])
    inf[1].add(b['основа1'] + 'ья́ми')
    inf[1].add(b['основа1'] + 'ья́х')
    # end pl
m_funcs['1c^'] = q_m_1cV

def q_m_1c_1_(animacy, **b):
    # борт, боцман
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'а́')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'о́в')
    else:
        inf[1].add(b['основа1'] + 'а́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['1c(1)'] = q_m_1c_1_

def q_m_1c_1_V(animacy, **b):
    assert animacy == False
    # год, перёд
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а')
    inf[0].add(b['основа1'] + 'у')
    inf[0].add(b['основа'])  # http://ru.wiktionary.org/wiki/Шаблон:сущ_ru_m_ina_1c(1)^ has an error
    inf[0].add(b['основа1'] + 'ом')
    inf[0].add(b['основа1'] + 'е')
    # end sg
    inf[1].add(b['основа2'] + 'а́')
    inf[1].add(b['основа3'])
    inf[1].add(b['основа2'] + 'а́м')
    inf[1].add(b['основа2'] + 'а́')
    inf[1].add(b['основа2'] + 'а́ми')
    inf[1].add(b['основа2'] + 'а́х')
    # end pl
m_funcs['1c(1)^'] = q_m_1c_1_V

def q_m_1c_2_(animacy, **b):
    assert animacy == False
    # раз
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'ы́')
    inf[1].add(b['основа'])
    inf[1].add(b['основа1'] + 'а́м')
    inf[1].add(b['основа1'] + 'ы́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['1c(2)'] = q_m_1c_2_

def q_m_1c_1__2_(animacy, **b):
    assert animacy == False
    # глаз, глаза
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'а́')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа1'] + 'а́м')
    inf[1].add(b['основа1'] + 'а́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['1c(1)(2)'] = q_m_1c_1__2_

def q_m_1cs_1_(animacy, **b):
    assert animacy == False
    # ветер
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а')
    inf[0].add(b['основа1'] + 'у')
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'ом')
    inf[0].add(b['основа1'] + 'е')
    # end sg
    inf[1].add(b['основа2'] + 'а́')
    inf[1].add(b['основа2'] + 'о́в')
    inf[1].add(b['основа2'] + 'а́м')
    inf[1].add(b['основа2'] + 'а́')
    inf[1].add(b['основа2'] + 'а́ми')
    inf[1].add(b['основа2'] + 'а́х')
    # end pl
m_funcs['1*c(1)'] = q_m_1cs_1_

def q_m_1cr1(animacy, **b):
    assert animacy == True
    # господин
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'а́')
    inf[1].add(b['основа2'])
    inf[1].add(b['основа1'] + 'а́м')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['1°c(1)'] = q_m_1cr1

def q_m_1dV(animacy, **b):
    assert animacy == False
    # кол
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а́')
    inf[0].add(b['основа1'] + 'у́')
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'о́м')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа'] + 'ья')
    inf[1].add(b['основа'] + 'ьев')
    inf[1].add(b['основа'] + 'ьям')
    inf[1].add(b['основа'] + 'ья')
    inf[1].add(b['основа'] + 'ьями')
    inf[1].add(b['основа'] + 'ьях')
    # end pl
m_funcs['1d^'] = q_m_1dV

def q_m_1e(animacy, **b):
    # зуб
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'о́в')
    else:
        inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['1e'] = q_m_1e

def q_m_1es(animacy, **b):
    # ветер
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а')
    inf[0].add(b['основа1'] + 'у')
    if animacy:
        inf[0].add(b['основа1'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'ом')
    inf[0].add(b['основа1'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа2'] + 'о́в')
    inf[1].add(b['основа2'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'о́в')
    else:
        inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа2'] + 'а́ми')
    inf[1].add(b['основа2'] + 'а́х')
    # end pl
m_funcs['1*e'] = q_m_1es

def q_m_1e_2_(animacy, **b):
    # волос
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа2'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа2'] + 'а́ми')
    inf[1].add(b['основа2'] + 'а́х')
    # end pl
m_funcs['1e(2)'] = q_m_1e_2_

def q_m_2a(animacy, **b):
    # портфель, житель
    inf = [[], []]
    inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа'] + 'я')
    inf[0].add(b['основа'] + 'ю')
    if animacy:
        inf[0].add(b['основа'] + 'я')
    else:
        inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа'] + 'ем')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ей')
    inf[1].add(b['основа'] + 'ям')
    if animacy:
        inf[1].add(b['основа'] + 'ей')
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ями')
    inf[1].add(b['основа'] + 'ях')
    # end pl
m_funcs['2a'] = q_m_2a

def q_m_2as(animacy, **b):
    # увалень, ливень
    inf = [[], []]
    inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа1'] + 'я')
    inf[0].add(b['основа1'] + 'ю')
    if animacy:
        inf[0].add(b['основа1'] + 'я')
    else:
        inf[0].add(b['основа1'] + 'ь')
    inf[0].add(b['основа1'] + 'ем')
    inf[0].add(b['основа1'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ей')
    inf[1].add(b['основа1'] + 'ям')
    if animacy:
        inf[1].add(b['основа1'] + 'ей')
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ями')
    inf[1].add(b['основа1'] + 'ях')
    # end pl
m_funcs['2*a'] = q_m_2as

def q_m_2b(animacy, **b):
    # карась, словарь
    inf = [[], []]
    inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа1'] + 'я́')
    inf[0].add(b['основа1'] + 'ю́')
    if animacy:
        inf[0].add(b['основа1'] + 'я́')
    else:
        inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа1'] + 'ём')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'е́й')
    inf[1].add(b['основа1'] + 'я́м')
    if animacy:
        inf[1].add(b['основа1'] + 'е́й')
    else:
        inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'я́ми')
    inf[1].add(b['основа1'] + 'я́х')
    # end pl
m_funcs['2b'] = q_m_2b

def q_m_2bs(animacy, **b):
    # угорь, огонь
    inf = [[], []]
    inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа1'] + 'я́')
    inf[0].add(b['основа1'] + 'ю́')
    if animacy:
        inf[0].add(b['основа1'] + 'я́')
    else:
        inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа1'] + 'ём')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'е́й')
    inf[1].add(b['основа1'] + 'я́м')
    if animacy:
        inf[1].add(b['основа1'] + 'е́й')
    else:
        inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'я́ми')
    inf[1].add(b['основа1'] + 'я́х')
    # end pl
m_funcs['2*b'] = q_m_2bs

def q_m_2e(animacy, **b):
    # голубь
    inf = [[], []]
    inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа'] + 'я')
    inf[0].add(b['основа'] + 'ю')
    if animacy:
        inf[0].add(b['основа'] + 'я')
    else:
        inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа'] + 'ем')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа1'] + 'е́й')
    inf[1].add(b['основа1'] + 'я́м')
    if animacy:
        inf[1].add(b['основа1'] + 'е́й')
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа1'] + 'я́ми')
    inf[1].add(b['основа1'] + 'я́х')
    # end pl
m_funcs['2e'] = q_m_2e

def q_m_2es(animacy, **b):
    # ноготь
    inf = [[], []]
    inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа1'] + 'я')
    inf[0].add(b['основа1'] + 'ю')
    if animacy:
        inf[0].add(b['основа1'] + 'я')
    else:
        inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа1'] + 'ем')
    inf[0].add(b['основа1'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа2'] + 'е́й')
    inf[1].add(b['основа2'] + 'я́м')
    if animacy:
        inf[1].add(b['основа2'] + 'е́й')
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа2'] + 'я́ми')
    inf[1].add(b['основа2'] + 'я́х')
    # end pl
m_funcs['2*e'] = q_m_2es

def q_m_2f(animacy, **b):
    # конь
    inf = [[], []]
    inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа1'] + 'я́')
    inf[0].add(b['основа1'] + 'ю́')
    if animacy:
        inf[0].add(b['основа1'] + 'я́')
    else:
        inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа1'] + 'ём')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа1'] + 'е́й')
    inf[1].add(b['основа1'] + 'я́м')
    if animacy:
        inf[1].add(b['основа1'] + 'е́й')
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа1'] + 'я́ми')
    inf[1].add(b['основа1'] + 'я́х')
    # end pl
m_funcs['2f'] = q_m_2f

def q_m_3a(animacy, **b):
    # бульдог, чайник
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ов')
    inf[1].add(b['основа'] + 'ам')
    if animacy:
        inf[1].add(b['основа'] + 'ов')
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ами')
    inf[1].add(b['основа'] + 'ах')
    # end pl
m_funcs['3a'] = q_m_3a

def q_m_3as(animacy, **b):
    # перешеек
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а')
    inf[0].add(b['основа1'] + 'у')
    if animacy:
        inf[0].add(b['основа1'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'ом')
    inf[0].add(b['основа1'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ов')
    inf[1].add(b['основа1'] + 'ам')
    if animacy:
        inf[1].add(b['основа1'] + 'ов')
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
m_funcs['3*a'] = q_m_3as

def q_m_3as_2_(animacy, **b):
    # черевичек
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а')
    inf[0].add(b['основа1'] + 'у')
    if animacy:
        inf[0].add(b['основа1'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'ом')
    inf[0].add(b['основа1'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа'])
    inf[1].add(b['основа1'] + 'ам')
    if animacy:
        inf[1].add(b['основа'])
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
m_funcs['3*a(2)'] = q_m_3as_2_

def q_m_3ar(animacy, **b):
    # цыплёнок
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа2'] + 'а')
    inf[0].add(b['основа2'] + 'у')
    if animacy:
        inf[0].add(b['основа2'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа2'] + 'ом')
    inf[0].add(b['основа2'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ов')
    inf[1].add(b['основа1'] + 'ам')
    if animacy:
        inf[1].add(b['основа1'] + 'ов')
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
m_funcs['3°a'] = q_m_3ar

def q_m_3b(animacy, **b):
    # рыбак, пирог
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а́')
    inf[0].add(b['основа1'] + 'у́')
    if animacy:
        inf[0].add(b['основа1'] + 'а́')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'о́м')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'о́в')
    else:
        inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['3b'] = q_m_3b

def q_m_3br(animacy, **b):
    # щенок
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а́')
    inf[0].add(b['основа1'] + 'у́')
    if animacy:
        inf[0].add(b['основа1'] + 'а́')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'о́м')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа2'] + 'а')
    inf[1].add(b['основа2'])
    inf[1].add(b['основа2'] + 'ам')
    if animacy:
        inf[1].add(b['основа2'])
    else:
        inf[1].add(b['основа2'] + 'а')
    inf[1].add(b['основа2'] + 'ами')
    inf[1].add(b['основа2'] + 'ах')
    # second option
    inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'о́в')
    else:
        inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['3°b'] = q_m_3br

def q_m_3b_2_(animacy, **b):
    # сапог
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а́')
    inf[0].add(b['основа1'] + 'у́')
    if animacy:
        inf[0].add(b['основа1'] + 'а́')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'о́м')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа'])
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа'])
    else:
        inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['3b(2)'] = q_m_3b_2_

def q_m_3bs(animacy, **b):
    # хорёк, кусок
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а́')
    inf[0].add(b['основа1'] + 'у́')
    if animacy:
        inf[0].add(b['основа1'] + 'а́')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'о́м')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'о́в')
    else:
        inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['3*b'] = q_m_3bs

def q_m_3bs_2_(animacy, **b):
    # чулок
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а́')
    inf[0].add(b['основа1'] + 'у́')
    if animacy:
        inf[0].add(b['основа1'] + 'а́')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'о́м')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа'])
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа'])
    else:
        inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['3*b(2)'] = q_m_3bs_2_

def q_m_3c(animacy, **b):
    # плуг
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'о́в')
    else:
        inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['3c'] = q_m_3c

def q_m_3c_1_(animacy, **b):
    # снег, округ
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'а́')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'о́в')
    else:
        inf[1].add(b['основа1'] + 'а́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['3c(1)'] = q_m_3c_1_

def q_m_3d(animacy, **b):
    # казак
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а́')
    inf[0].add(b['основа1'] + 'у́')
    if animacy:
        inf[0].add(b['основа1'] + 'а́')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'о́м')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ов')
    inf[1].add(b['основа'] + 'ам')
    if animacy:
        inf[1].add(b['основа'] + 'ов')
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ами')
    inf[1].add(b['основа'] + 'ах')
    # end pl
m_funcs['3d'] = q_m_3d

def q_m_3e(animacy, **b):
    # волк, слог
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ом')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'о́в')
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['3e'] = q_m_3e

def q_m_4a(animacy, **b):
    # товарищ, марш
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ем')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ей')
    inf[1].add(b['основа'] + 'ам')
    if animacy:
        inf[1].add(b['основа'] + 'ей')
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ами')
    inf[1].add(b['основа'] + 'ах')
    # end pl
m_funcs['4a'] = q_m_4a

def q_m_4b(animacy, **b):
    # нож, богач
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а́')
    inf[0].add(b['основа1'] + 'у́')
    if animacy:
        inf[0].add(b['основа1'] + 'а́')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'о́м')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'е́й')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'е́й')
    else:
        inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['4b'] = q_m_4b

def q_m_4c(animacy, **b):
    # харч
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ем')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'е́й')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'е́й')
    else:
        inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['4c'] = q_m_4c

def q_m_4e(animacy, **b):
    # обруч
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ем')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа1'] + 'е́й')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'е́й')
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['4e'] = q_m_4e

def q_m_5a(animacy, **b):
    # принц, месяц
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ем')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа'] + 'ев')
    inf[1].add(b['основа'] + 'ам')
    if animacy:
        inf[1].add(b['основа'] + 'ев')
    else:
        inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа'] + 'ами')
    inf[1].add(b['основа'] + 'ах')
    # end pl
m_funcs['5a'] = q_m_5a

def q_m_5a_2_(animacy, **b):
    # герц
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ем')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа'])
    inf[1].add(b['основа'] + 'ам')
    if animacy:
        inf[1].add(b['основа'] + 'ев')
    else:
        inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа'] + 'ами')
    inf[1].add(b['основа'] + 'ах')
    # end pl
m_funcs['5a(2)'] = q_m_5a_2_

def q_m_5as(animacy, **b):
    # немец, палец
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а')
    inf[0].add(b['основа1'] + 'у')
    if animacy:
        inf[0].add(b['основа1'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'ем')
    inf[0].add(b['основа1'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа1'] + 'ев')
    inf[1].add(b['основа1'] + 'ам')
    if animacy:
        inf[1].add(b['основа1'] + 'ев')
    else:
        inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
m_funcs['5*a'] = q_m_5as

def q_m_5b(animacy, **b):
    # кузнец, кострец
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а́')
    inf[0].add(b['основа1'] + 'у́')
    if animacy:
        inf[0].add(b['основа1'] + 'а́')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'о́м')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'ы́')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'о́в')
    else:
        inf[1].add(b['основа1'] + 'ы́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['5b'] = q_m_5b

def q_m_5bs(animacy, **b):
    # жилец, конец
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'а́')
    inf[0].add(b['основа1'] + 'у́')
    if animacy:
        inf[0].add(b['основа1'] + 'а́')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа1'] + 'о́м')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'ы́')
    inf[1].add(b['основа1'] + 'о́в')
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'] + 'о́в')
    else:
        inf[1].add(b['основа1'] + 'ы́')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
m_funcs['5*b'] = q_m_5bs

def q_m_6a(animacy, **b):
    # герой, случай
    inf = [[], []]
    inf[0].add(b['основа'] + 'й')
    inf[0].add(b['основа'] + 'я')
    inf[0].add(b['основа'] + 'ю')
    if animacy:
        inf[0].add(b['основа'] + 'я')
    else:
        inf[0].add(b['основа'] + 'й')
    inf[0].add(b['основа'] + 'ем')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ев')
    inf[1].add(b['основа'] + 'ям')
    if animacy:
        inf[1].add(b['основа'] + 'ев')
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ями')
    inf[1].add(b['основа'] + 'ях')
    # end pl
m_funcs['6a'] = q_m_6a

def q_m_6as(animacy, **b):
    # улей
    inf = [[], []]
    inf[0].add(b['основа'] + 'й')
    inf[0].add(b['основа1'] + 'я')
    inf[0].add(b['основа1'] + 'ю')
    if animacy:
        inf[0].add(b['основа1'] + 'я')
    else:
        inf[0].add(b['основа'] + 'й')
    inf[0].add(b['основа1'] + 'ем')
    inf[0].add(b['основа1'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ев')
    inf[1].add(b['основа1'] + 'ям')
    if animacy:
        inf[1].add(b['основа1'] + 'ев')
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ями')
    inf[1].add(b['основа1'] + 'ях')
    # end pl
m_funcs['6*a'] = q_m_6as

def q_m_6b(animacy, **b):
    # холуй, лишай
    inf = [[], []]
    inf[0].add(b['основа'] + 'й')
    inf[0].add(b['основа1'] + 'я́')
    inf[0].add(b['основа1'] + 'ю́')
    if animacy:
        inf[0].add(b['основа1'] + 'я́')
    else:
        inf[0].add(b['основа'] + 'й')
    inf[0].add(b['основа1'] + 'ём')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'ёв')
    inf[1].add(b['основа1'] + 'я́м')
    if animacy:
        inf[1].add(b['основа1'] + 'ёв')
    else:
        inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'я́ми')
    inf[1].add(b['основа1'] + 'я́х')
    # end pl
m_funcs['6b'] = q_m_6b

def q_m_6bs(animacy, **b):
    # муравей
    inf = [[], []]
    inf[0].add(b['основа'] + 'й')
    inf[0].add(b['основа1'] + 'я́')
    inf[0].add(b['основа1'] + 'ю́')
    if animacy:
        inf[0].add(b['основа1'] + 'я́')
    else:
        inf[0].add(b['основа'] + 'й')
    inf[0].add(b['основа1'] + 'ём')
    inf[0].add(b['основа1'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'ёв')
    inf[1].add(b['основа1'] + 'я́м')
    if animacy:
        inf[1].add(b['основа1'] + 'ёв')
    else:
        inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'я́ми')
    inf[1].add(b['основа1'] + 'я́х')
    # end pl
m_funcs['6*b'] = q_m_6bs

def q_m_6c(animacy, **b):
    # буй
    inf = [[], []]
    inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'у')
    if animacy:
        inf[0].add(b['основа'] + 'а')
    else:
        inf[0].add(b['основа'])
    inf[0].add(b['основа'] + 'ем')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'ёв')
    inf[1].add(b['основа1'] + 'я́м')
    if animacy:
        inf[1].add(b['основа1'] + 'ёв')
    else:
        inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'я́ми')
    inf[1].add(b['основа1'] + 'я́х')
    # end pl
m_funcs['6c'] = q_m_6c

def q_m_7a(animacy, **b):
    # викарий, гербарий
    inf = [[], []]
    inf[0].add(b['основа'] + 'й')
    inf[0].add(b['основа'] + 'я')
    inf[0].add(b['основа'] + 'ю')
    if animacy:
        inf[0].add(b['основа'] + 'я')
    else:
        inf[0].add(b['основа'] + 'й')
    inf[0].add(b['основа'] + 'ем')
    inf[0].add(b['основа'] + 'и')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ев')
    inf[1].add(b['основа'] + 'ям')
    if animacy:
        inf[1].add(b['основа'] + 'ев')
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ями')
    inf[1].add(b['основа'] + 'ях')
    # end pl
m_funcs['7a'] = q_m_7a

def q_m_7b(animacy, **b):
    # кий
    inf = [[], []]
    inf[0].add(b['основа'] + 'й')
    inf[0].add(b['основа1'] + 'я́')
    inf[0].add(b['основа1'] + 'ю́')
    if animacy:
        inf[0].add(b['основа1'] + 'я́')
    else:
        inf[0].add(b['основа'] + 'й')
    inf[0].add(b['основа1'] + 'ём')
    inf[0].add(b['основа1'] + 'и́')
    # end sg
    inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'ёв')
    inf[1].add(b['основа1'] + 'я́м')
    if animacy:
        inf[1].add(b['основа1'] + 'ёв')
    else:
        inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'я́ми')
    inf[1].add(b['основа1'] + 'я́х')
    # end pl
m_funcs['7b'] = q_m_7b

def q_m_7c(animacy, **b):
    # кий
    inf = [[], []]
    inf[0].add(b['основа'] + 'й')
    inf[0].add(b['основа'] + 'я')
    inf[0].add(b['основа'] + 'ю')
    if animacy:
        inf[0].add(b['основа'] + 'я')
    else:
        inf[0].add(b['основа'] + 'й')
    inf[0].add(b['основа'] + 'ем')
    inf[0].add(b['основа'] + 'и')
    # end sg
    inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'ёв')
    inf[1].add(b['основа1'] + 'я́м')
    if animacy:
        inf[1].add(b['основа1'] + 'ёв')
    else:
        inf[1].add(b['основа1'] + 'и́')
    inf[1].add(b['основа1'] + 'я́ми')
    inf[1].add(b['основа1'] + 'я́х')
    # end pl
m_funcs['7c'] = q_m_7c
