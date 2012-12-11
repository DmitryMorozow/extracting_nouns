f_funcs = {}

def q_f_1a( animacy, **b):
    # корова, лопата
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'ы')
    inf[0].add(b['основа'] + 'е')
    if animacy:
        inf[0].add(b['основа'] + 'у')
    else:
        inf[0].add(b['основа'] + 'у')
    inf[0].add(b['основа'] + 'ой')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа'])
    inf[1].add(b['основа'] + 'ам')
    if animacy:
        inf[1].add(b['основа'])
    else:
        inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа'] + 'ами')
    inf[1].add(b['основа'] + 'ах')
    # end pl
f_funcs['1a'] = q_f_1a
    
def q_f_2a( animacy, **b):
    # богиня, неделя
    inf = [[],[]] 
    inf[0].add(b['основа'] + 'я')
    inf[0].add(b['основа'] + 'и')
    inf[0].add(b['основа'] + 'е')
    if animacy:
        inf[0].add(b['основа'] + 'ю')
    else:
        inf[0].add(b['основа'] + 'ю')
    inf[0].add(b['основа'] + 'ей')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ь')
    inf[1].add(b['основа'] + 'ям')
    if animacy:
        inf[1].add(b['основа'] + 'ь')
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ями')
    inf[1].add(b['основа'] + 'ях')
    # end pl
f_funcs['2a'] = q_f_2a
    
def q_f_3a( animacy, **b):
    # собака, книга
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'и')
    inf[0].add(b['основа'] + 'е')
    if animacy:
        inf[0].add(b['основа'] + 'у')
    else:
        inf[0].add(b['основа'] + 'у')
    inf[0].add(b['основа'] + 'ой')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'])
    inf[1].add(b['основа'] + 'ам')
    if animacy:
        inf[1].add(b['основа'])
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ами')
    inf[1].add(b['основа'] + 'ах')
    # end pl
f_funcs['3a'] = q_f_3a
    
def q_f_4a( animacy, **b):
    # кассирша, туча
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'и')
    inf[0].add(b['основа'] + 'е')
    if animacy:
        inf[0].add(b['основа'] + 'у')
    else:
        inf[0].add(b['основа'] + 'у')
    inf[0].add(b['основа'] + 'ей')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ей')
    inf[1].add(b['основа'] + 'ам')
    if animacy:
        inf[1].add(b['основа'])
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ами')
    inf[1].add(b['основа'] + 'ах')
    # end pl
    
def q_f_5a( animacy, **b):
    # улица, проводница
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'ы')
    inf[0].add(b['основа'] + 'е')
    if animacy:
        inf[0].add(b['основа'] + 'у')
    else:
        inf[0].add(b['основа'] + 'у')
    inf[0].add(b['основа'] + 'ей')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа'])
    inf[1].add(b['основа'] + 'ам')
    if animacy:
        inf[1].add(b['основа'])
    else:
        inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа'] + 'ами')
    inf[1].add(b['основа'] + 'ах')
    # end pl
f_funcs['5a'] = q_f_5a
    
def q_f_6a( animacy, **b):
    # фея, статуя
    inf = [[],[]]
    inf[0].add(b['основа'] + 'я')
    inf[0].add(b['основа'] + 'и')
    inf[0].add(b['основа'] + 'е')
    if animacy:
        inf[0].add(b['основа'] + 'ю')
    else:
        inf[0].add(b['основа'] + 'ю')
    inf[0].add(b['основа'] + 'ей')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'й')
    inf[1].add(b['основа'] + 'ям')
    if animacy:
        inf[1].add(b['основа'] + 'й')
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ями')
    inf[1].add(b['основа'] + 'ях')
    # end pl
    
def q_f_7a( animacy, **b):
    # армия, рептилия
    inf = [[],[]]
    inf[0].add(b['основа'] + 'я')
    inf[0].add(b['основа'] + 'и')
    inf[0].add(b['основа'] + 'и')
    if animacy:
        inf[0].add(b['основа'] + 'ю')
    else:
        inf[0].add(b['основа'] + 'ю')
    inf[0].add(b['основа'] + 'ей')
    inf[0].add(b['основа'] + 'и')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'й')
    inf[1].add(b['основа'] + 'ям')
    if animacy:
        inf[1].add(b['основа'] + 'й')
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ями')
    inf[1].add(b['основа'] + 'ях')
    # end pl
f_funcs['6a'] = q_f_6a

def q_f_1b(animacy, **b):
    # гюрза, похвала
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'ы́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'у́')
    else:
        inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа'] + 'ы́')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа'] + 'ы́')
    inf[1].add(b['основа'] + 'а́ми')
    inf[1].add(b['основа'] + 'а́х')
    # end pl
f_funcs['1b'] = q_f_1b
    
def q_f_2b(animacy, **b):
    # тля, стезя
    inf = [[],[]]
    inf[0].add(b['основа'] + 'я́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'ю́')
    else:
        inf[0].add(b['основа'] + 'ю́')
    inf[0].add(b['основа'] + 'ёй')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа'] + 'и́')
    inf[1].add(b['основа'] + 'е́й')
    inf[1].add(b['основа'] + 'я́м')
    if animacy:
        inf[1].add(b['основа'] + 'е́й')
    else:
        inf[1].add(b['основа'] + 'и́')
    inf[1].add(b['основа'] + 'я́ми')
    inf[1].add(b['основа'] + 'я́х')
    # end pl
f_funcs['2b'] = q_f_2b
    
def q_f_3b(animacy, **b):
    # карга, острога
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'у́')
    else:
        inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа'] + 'и́')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа'] + 'и́')
    inf[1].add(b['основа'] + 'а́ми')
    inf[1].add(b['основа'] + 'а́х')
    # end pl
f_funcs['3b'] = q_f_3b
    
def q_f_4b(animacy, **b):
    # ханжа, каланча
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'у́')
    else:
        inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа'] + 'и́')
    inf[1].add(b['основа'] + 'е́й')
    inf[1].add(b['основа'] + 'а́м')
    if animacy:
        inf[1].add(b['основа'] + 'е́й')
    else:
        inf[1].add(b['основа'] + 'и́')
    inf[1].add(b['основа'] + 'а́ми')
    inf[1].add(b['основа'] + 'а́х')
    # end pl
f_funcs['4b'] = q_f_4b
    
def q_f_6b(animacy, **b):
    # швея, колея
    inf = [[],[]]
    inf[0].add(b['основа'] + 'я́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'ю́')
    else:
        inf[0].add(b['основа'] + 'ю́')
    inf[0].add(b['основа'] + 'ёй')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа'] + 'и́')
    inf[1].add(b['основа1'] + 'й')
    inf[1].add(b['основа'] + 'я́м')
    if animacy:
        inf[1].add(b['основа1'] + 'й')
    else:
        inf[1].add(b['основа'] + 'и́')
    inf[1].add(b['основа'] + 'я́ми')
    inf[1].add(b['основа'] + 'я́х')
    # end pl
f_funcs['6b'] = q_f_6b
    
def q_f_7b( animacy, **b):
    # судия, лития
    inf = [[],[]]
    if animacy:
        inf[0].add(b['основа'] + 'ия́')
    else:
        inf[0].add(b['основа'] + 'я́')
    if animacy:
        inf[0].add(b['основа'] + 'ии́')
    else:
        inf[0].add(b['основа'] + 'и́')
    if animacy:
        inf[0].add(b['основа'] + 'ии́')
    else:
        inf[0].add(b['основа'] + 'и́')
    if animacy:
        inf[0].add(b['основа'] + 'и́ю')
    else:
        inf[0].add(b['основа'] + 'и́ю')
    if animacy:
        inf[0].add(b['основа'] + 'иёю')
    else:
        inf[0].add(b['основа'] + 'е́ю')
    if animacy:
        inf[0].add(b['основа'] + 'ии́')
    else:
        inf[0].add(b['основа'] + 'и')
    # end sg
    if animacy:
        inf[0].add(b['основа'] + 'ии́')
    else:
        inf[0].add(b['основа'] + 'и́')
    if animacy:
        inf[0].add(b['основа'] + 'и́й')
    else:
        inf[0].add(b['основа1'] + 'й')
    if animacy:
        inf[0].add(b['основа'] + 'ия́м')
    else:
        inf[0].add(b['основа'] + 'я́м')
    if animacy:
        inf[0].add(b['основа'] + 'ии́')
    else:
        inf[0].add(b['основа'] + 'и́')
    if animacy:
        inf[0].add(b['основа'] + 'ия́ми')
    else:
        inf[0].add(b['основа'] + 'я́ми')
    if animacy:
        inf[0].add(b['основа'] + 'ия́х')
    else:
        inf[0].add(b['основа'] + 'я́х')
    # end pl
f_funcs['7b'] = q_f_7b
    
def q_f_1d( animacy, **b):
    # красота, сирота
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'ы́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'у́')
    else:
        inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа1'] + 'ам')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
f_funcs['1d'] = q_f_1d
    
def q_f_2d( animacy, **b):
    # заря
    inf = [[],[]] 
    inf[0].add(b['основа'] + 'я́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е')
    if animacy:
        inf[0].add(b['основа'] + 'ю́')
    else:
        inf[0].add(b['основа'] + 'ю́')
    inf[0].add(b['основа'] + 'ёй')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ь')
    inf[1].add(b['основа1'] + 'ям')
    if animacy:
        inf[1].add(b['основа1'] + 'ь')
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ями')
    inf[1].add(b['основа1'] + 'ях')
    # end pl
f_funcs['2d'] = q_f_2d
    
def q_f_3d( animacy, **b):
    # слуга, дуга
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'у́')
    else:
        inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа1'] + 'ам')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
f_funcs['3d'] = q_f_3d
    
def q_f_4d( animacy, **b):
    # межа
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'у́')
    else:
        inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ей')
    inf[1].add(b['основа1'] + 'ам')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
f_funcs['4d'] = q_f_4d
    
def q_f_6d (animacy, **b):
    # змея
    inf = [[],[]]
    inf[0].add(b['основа'] + 'я́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'ю́')
    else:
        inf[0].add(b['основа'] + 'ю́')
    inf[0].add(b['основа'] + 'ёй')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'й')
    inf[1].add(b['основа1'] + 'ям')
    if animacy:
        inf[1].add(b['основа1'] + 'й')
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ями')
    inf[1].add(b['основа1'] + 'ях')
    # end pl
f_funcs['6d'] = q_f_6d
    
def q_f_1dt( animacy, **b):
    # спина, зима
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'ы́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа1'] + 'у')
    else:
        inf[0].add(b['основа1'] + 'у')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа1'] + 'ам')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
f_funcs["1d'"] = q_f_1dt
    
def q_f_3dt( animacy, **b):
    # река
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа1'] + 'у')
    else:
        inf[0].add(b['основа1'] + 'у')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа1'] + 'ам')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
f_funcs["3d'"] = q_f_3dt
    
def q_f_4dt( animacy, **b):
    # душа
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа1'] + 'у')
    else:
        inf[0].add(b['основа1'] + 'у')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ей')
    inf[1].add(b['основа1'] + 'ам')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
f_funcs["4d'"] = q_f_4dt
    
def q_f_2e( animacy, **b):
    # доля
    inf = [[],[]] 
    inf[0].add(b['основа'] + 'я')
    inf[0].add(b['основа'] + 'и')
    inf[0].add(b['основа'] + 'е')
    if animacy:
        inf[0].add(b['основа'] + 'ю')
    else:
        inf[0].add(b['основа'] + 'ю')
    inf[0].add(b['основа'] + 'ей')
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
f_funcs['2e'] = q_f_2e
    
def q_f_1f( animacy, **b):
    # губа
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'ы́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'у́')
    else:
        inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа'] + 'а́ми')
    inf[1].add(b['основа'] + 'а́х')
    # end pl
f_funcs['1f'] = q_f_1f
    
def q_f_2f( animacy, **b):
    # ноздря, простыня
    inf = [[],[]] 
    inf[0].add(b['основа'] + 'я́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'ю́')
    else:
        inf[0].add(b['основа'] + 'ю́')
    inf[0].add(b['основа'] + 'ёй')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа'] + 'е́й')
    inf[1].add(b['основа'] + 'я́м')
    if animacy:
        inf[1].add(b['основа'] + 'е́й')
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа'] + 'я́ми')
    inf[1].add(b['основа'] + 'я́х')
    # end pl
f_funcs['2f'] = q_f_2f
    
def q_f_3f( animacy, **b):
    # слега
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'у́')
    else:
        inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа2'])
    inf[1].add(b['основа'] + 'а́м')
    if animacy:
        inf[1].add(b['основа2'])
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа'] + 'а́ми')
    inf[1].add(b['основа'] + 'а́х')
    # end pl
f_funcs['3f'] = q_f_3f
    
def q_f_4f( animacy, **b):
    # вожжа
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'у́')
    else:
        inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа'] + 'е́й')
    inf[1].add(b['основа'] + 'а́м')
    if animacy:
        inf[1].add(b['основа'])
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа'] + 'а́ми')
    inf[1].add(b['основа'] + 'а́х')
    # end pl
f_funcs['4f'] = q_f_4f
    
def q_f_1ft( animacy, **b):
    # борода
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'ы́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа1'] + 'у')
    else:
        inf[0].add(b['основа1'] + 'у')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа'] + 'а́ми')
    inf[1].add(b['основа'] + 'а́х')
    # end pl
f_funcs["1f'"] = q_f_1ft    
    
def q_f_3ft( animacy, **b):
    # щека, рука
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа1'] + 'у')
    else:
        inf[0].add(b['основа1'] + 'у')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа'] + 'а́ми')
    inf[1].add(b['основа'] + 'а́х')
    # end pl
f_funcs["3f'"] = q_f_3ft
    
def q_f_8a( animacy, **b):
    # лань, тетрадь
    inf = [[],[]]
    inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа'] + 'и')
    inf[0].add(b['основа'] + 'и')
    if animacy:
        inf[0].add(b['основа'] + 'ь')
    else:
        inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа'] + 'ью')
    inf[0].add(b['основа'] + 'и')
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
f_funcs['8a'] = q_f_8a
    
def q_f_8e( animacy, **b):
    # стерлядь, площадь
    inf = [[],[]]
    inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа'] + 'и')
    inf[0].add(b['основа'] + 'и')
    if animacy:
        inf[0].add(b['основа'] + 'ь')
    else:
        inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа'] + 'ью')
    inf[0].add(b['основа'] + 'и')
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
f_funcs['8e'] = q_f_8e
    
def q_f_8a_sh( animacy, **b):
    # пустошь
    inf = [[],[]]
    inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа'] + 'и')
    inf[0].add(b['основа'] + 'и')
    if animacy:
        inf[0].add(b['основа'] + 'ь')
    else:
        inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа'] + 'ью')
    inf[0].add(b['основа'] + 'и')
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
f_funcs['8a-ш'] = q_f_8a_sh
    
def q_f_8e_sh( animacy, **b):
    # мышь, ночь
    inf = [[],[]]
    inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа'] + 'и')
    inf[0].add(b['основа'] + 'и')
    if animacy:
        inf[0].add(b['основа'] + 'ь')
    else:
        inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа'] + 'ью')
    inf[0].add(b['основа'] + 'и')
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
f_funcs['8e-ш'] = q_f_8e_sh
    
def q_f_8ft( animacy, **b):
    # грудь
    inf = [[],[]]
    inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа1'] + 'и́')
    inf[0].add(b['основа1'] + 'и́')
    if animacy:
        inf[0].add(b['основа'] + 'ь')
    else:
        inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа'] + 'ью')
    inf[0].add(b['основа1'] + 'и́')
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
f_funcs["8f'"] = q_f_8ft

def q_f_1as( animacy, **b):
    # царевна, свадьба
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'ы')
    inf[0].add(b['основа'] + 'е')
    if animacy:
        inf[0].add(b['основа'] + 'у')
    else:
        inf[0].add(b['основа'] + 'у')
    inf[0].add(b['основа'] + 'ой')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа'] + 'ам')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа'] + 'ами')
    inf[1].add(b['основа'] + 'ах')
    # end pl
f_funcs['1*a'] = q_f_1as
    
def q_f_1bs(animacy, **b):
    # княжна, кайма
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'ы́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'у́')
    else:
        inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа'] + 'ы́')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа'] + 'ы́')
    inf[1].add(b['основа'] + 'а́ми')
    inf[1].add(b['основа'] + 'а́х')
    # end pl
f_funcs['1*b'] = q_f_1bs
    
def q_f_1ds( animacy, **b):
    # сестра, весна
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'ы́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'у́')
    else:
        inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа2'])
    inf[1].add(b['основа1'] + 'ам')
    if animacy:
        inf[1].add(b['основа2'])
    else:
        inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
f_funcs['1*d'] = q_f_1ds
    
def q_f_1es(animacy, **b):
    # бубна
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'ы')
    inf[0].add(b['основа'] + 'е')
    if animacy:
        inf[0].add(b['основа'] + 'у')
    else:
        inf[0].add(b['основа'] + 'у')
    inf[0].add(b['основа'] + 'ой')
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
f_funcs['1*e'] = q_f_1es
    
def q_f_1fs( animacy, **b):
    # копна
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'ы́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'у́')
    else:
        inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа2'])
    inf[1].add(b['основа1'] + 'а́м')
    if animacy:
        inf[1].add(b['основа2'])
    else:
        inf[1].add(b['основа1'] + 'ы')
    inf[1].add(b['основа1'] + 'а́ми')
    inf[1].add(b['основа1'] + 'а́х')
    # end pl
f_funcs['1*f'] = q_f_1fs
    
def q_f_2as( animacy, **b):
    # цапля, кровля
    inf = [[],[]] 
    inf[0].add(b['основа'] + 'я')
    inf[0].add(b['основа'] + 'и')
    inf[0].add(b['основа'] + 'е')
    if animacy:
        inf[0].add(b['основа'] + 'ю')
    else:
        inf[0].add(b['основа'] + 'ю')
    inf[0].add(b['основа'] + 'ей')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа1'] + 'ь')
    inf[1].add(b['основа'] + 'ям')
    if animacy:
        inf[1].add(b['основа1'] + 'ь')
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ями')
    inf[1].add(b['основа'] + 'ях')
    # end pl
f_funcs['2*a'] = q_f_2as
    
def q_f_2as_nya( animacy, **b):
    # просвирня, песня
    inf = [[],[]] 
    inf[0].add(b['основа'] + 'я')
    inf[0].add(b['основа'] + 'и')
    inf[0].add(b['основа'] + 'е')
    if animacy:
        inf[0].add(b['основа'] + 'ю')
    else:
        inf[0].add(b['основа'] + 'ю')
    inf[0].add(b['основа'] + 'ей')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа'] + 'ям')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ями')
    inf[1].add(b['основа'] + 'ях')
    # end pl
f_funcs['2*a-ня'] = q_f_2as_nya
    
def q_f_2bs(animacy, **b):
    # шестерня
    inf = [[],[]]
    inf[0].add(b['основа'] + 'я́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'ю́')
    else:
        inf[0].add(b['основа'] + 'ю́')
    inf[0].add(b['основа'] + 'ёй')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа'] + 'и́')
    inf[1].add(b['основа'] + 'е́й')
    inf[1].add(b['основа'] + 'я́м')
    if animacy:
        inf[1].add(b['основа'] + 'е́й')
    else:
        inf[1].add(b['основа'] + 'и́')
    inf[1].add(b['основа'] + 'я́ми')
    inf[1].add(b['основа'] + 'я́х')
    # end pl
f_funcs['2*s'] = q_f_2bs
    
def q_f_2ds( animacy, **b):
    # петля
    inf = [[],[]] 
    inf[0].add(b['основа'] + 'я́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е')
    if animacy:
        inf[0].add(b['основа'] + 'ю́')
    else:
        inf[0].add(b['основа'] + 'ю́')
    inf[0].add(b['основа'] + 'ёй')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа2'] + 'ь')
    inf[1].add(b['основа1'] + 'ям')
    if animacy:
        inf[1].add(b['основа2'] + 'ь')
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ями')
    inf[1].add(b['основа1'] + 'ях')
    # end pl
f_funcs['2*d'] = q_f_2ds

def q_f_3as( animacy, **b):
    # шпилька, чайка
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'и')
    inf[0].add(b['основа'] + 'е')
    if animacy:
        inf[0].add(b['основа'] + 'у')
    else:
        inf[0].add(b['основа'] + 'у')
    inf[0].add(b['основа'] + 'ой')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа'] + 'ам')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа'] + 'и')
    inf[1].add(b['основа'] + 'ами')
    inf[1].add(b['основа'] + 'ах')
    # end pl
f_funcs['3*a'] = q_f_3as

def q_f_3bs(animacy, **b):
    # кишка, кабарга
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'у́')
    else:
        inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа'] + 'и́')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа'] + 'а́м')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа'] + 'и́')
    inf[1].add(b['основа'] + 'а́ми')
    inf[1].add(b['основа'] + 'а́х')
    # end pl
f_funcs['3*b'] = q_f_3bs

def q_f_3ds( animacy, **b):
    # кирка
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'у́')
    else:
        inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа2'])
    inf[1].add(b['основа1'] + 'ам')
    if animacy:
        inf[1].add(b['основа2'])
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа1'] + 'ами')
    inf[1].add(b['основа1'] + 'ах')
    # end pl
f_funcs['3*d'] = q_f_3ds

def q_f_3fs( animacy, **b):
    # серьга
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа'] + 'у́')
    else:
        inf[0].add(b['основа'] + 'у́')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа2'])
    inf[1].add(b['основа'] + 'а́м')
    if animacy:
        inf[1].add(b['основа2'])
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа'] + 'а́ми')
    inf[1].add(b['основа'] + 'а́х')
    # end pl
f_funcs['3*f'] = q_f_3fs

def q_f_3fst( animacy, **b):
    # доска
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а́')
    inf[0].add(b['основа'] + 'и́')
    inf[0].add(b['основа'] + 'е́')
    if animacy:
        inf[0].add(b['основа1'] + 'у')
    else:
        inf[0].add(b['основа1'] + 'у')
    inf[0].add(b['основа'] + 'о́й')
    inf[0].add(b['основа'] + 'е́')
    # end sg
    inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа2'])
    inf[1].add(b['основа'] + 'а́м')
    if animacy:
        inf[1].add(b['основа2'])
    else:
        inf[1].add(b['основа1'] + 'и')
    inf[1].add(b['основа'] + 'а́ми')
    inf[1].add(b['основа'] + 'а́х')
    # end pl
f_funcs["3*f'"] = q_f_3fst

def q_f_5as( animacy, **b):
    # дверца
    inf = [[],[]]
    inf[0].add(b['основа'] + 'а')
    inf[0].add(b['основа'] + 'ы')
    inf[0].add(b['основа'] + 'е')
    if animacy:
        inf[0].add(b['основа'] + 'у')
    else:
        inf[0].add(b['основа'] + 'у')
    inf[0].add(b['основа'] + 'ей')
    inf[0].add(b['основа'] + 'е')
    # end sg
    inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа1'])
    inf[1].add(b['основа'] + 'ам')
    if animacy:
        inf[1].add(b['основа1'])
    else:
        inf[1].add(b['основа'] + 'ы')
    inf[1].add(b['основа'] + 'ами')
    inf[1].add(b['основа'] + 'ах')
    # end pl
f_funcs['5*a'] = q_f_5as

def q_f_8bst( animacy, **b):
    # любовь
    inf = [[],[]]
    inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа1'] + 'и́')
    inf[0].add(b['основа1'] + 'и́')
    if animacy:
        inf[0].add(b['основа'] + 'ь')
    else:
        inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа'] + 'ью')
    inf[0].add(b['основа1'] + 'и́')
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
f_funcs["8*b'"] = q_f_8bst

def q_f_8bstsh( animacy, **b):
    # вошь
    inf = [[],[]]
    inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа1'] + 'и́')
    inf[0].add(b['основа1'] + 'и́')
    if animacy:
        inf[0].add(b['основа'] + 'ь')
    else:
        inf[0].add(b['основа'] + 'ь')
    inf[0].add(b['основа'] + 'ью')
    inf[0].add(b['основа1'] + 'и́')
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
f_funcs["8*b'ш"] = q_f_8bstsh