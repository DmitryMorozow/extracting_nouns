def q_m_1a( animacy, base, base1 = None, base2 = None):
    # ветеринар, завод
    inf = [[],[]]
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

def q_m_2a( animacy, base, base1 = None, base2 = None):
    # портфель, житель
    inf = [[],[]] 
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
    
def q_m_3a( animacy, base, base1 = None, base2 = None):
    # бульдог, чайник
    inf = [[],[]]
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
    
def q_m_4a( animacy, base, base1 = None, base2 = None):
    # товарищ, марш
    inf = [[],[]]
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
    
def q_m_5a( animacy, base, base1 = None, base2 = None):
    # принц, месяц
    inf = [[],[]]
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
    
def q_m_6a( animacy, base, base1 = None, base2 = None):
    # герой, случай
    inf = [[],[]]
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
    
def q_m_7a( animacy, base, base1 = None, base2 = None):
    # викарий, гербарий
    inf = [[],[]]
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

def q_m_1b(animacy, base, base1 = None, base2 = None):
    # бегун, топор
    inf = [[],[]]
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
    
def q_m_2b(animacy, base, base1 = None, base2 = None):
    # карась, словарь
    inf = [[],[]]
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
    inf = [[],[]]
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
    inf = [[],[]]
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
    inf = [[],[]]
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
    inf = [[],[]]
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
    inf = [[],[]]
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
    
def q_m_1c(animacy, base, base1 = None, base2 = None):
    # дар
    inf = [[],[]]
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
    
def q_m_3c( animacy, base, base1 = None, base2 = None):
    # плуг
    inf = [[],[]]
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
    inf = [[],[]]
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
    inf = [[],[]]
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
    inf = [[],[]]
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
    
def q_m_1dV(animacy, base, base1 = None, base2 = None):
    # кол
    inf = [[],[]]
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
    inf[1].add(base + 'ья')
    inf[1].add(base + 'ьев')
    inf[1].add(base + 'ьям')
    if animacy:
        inf[1].add(base + 'ьев')
    else:
        inf[1].add(base + 'ья')
    inf[1].add(base + 'ьями')
    inf[1].add(base + 'ьях')
    # end pl
    
def q_m_3d(animacy, base, base1 = None, base2 = None):
    # казак
    inf = [[],[]]
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
    inf = [[],[]]
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
    inf = [[],[]]
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
    
def q_m_3e( animacy, base, base1 = None, base2 = None):
    # волк, слог
    inf = [[],[]]
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
    inf = [[],[]]
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
    inf = [[],[]]
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
    

    
def q_m_1as( animacy, base, base1 = None, base2 = None):
    # бубен, свёкор
    inf = [[],[]]
    inf[0].add(base)
    inf[0].add(base1 + 'а')
    inf[0].add(base1 + 'у')
    if animacy:
        inf[0].add(base1 + 'а')
    else:
        inf[0].add(base1)
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
    
def q_m_1bs(animacy, base, base1 = None, base2 = None):
    # узел
    inf = [[],[]]
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
    
def q_m_1es(animacy, base, base1 = None, base2 = None):
    # ветер
    inf = [[],[]]
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
    
def q_m_2as( animacy, base, base1 = None, base2 = None):
    # увалень, ливень
    inf = [[],[]] 
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
    inf = [[],[]]
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
    inf = [[],[]]
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
    
def q_m_3as( animacy, base, base1 = None, base2 = None):
    # перешеек
    inf = [[],[]]
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
    inf = [[],[]]
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
    
def q_m_5as( animacy, base, base1 = None, base2 = None):
    # немец, палец
    inf = [[],[]]
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
    inf = [[],[]]
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
    
def q_m_6as( animacy, base, base1 = None, base2 = None):
    # улей
    inf = [[],[]]
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
    inf = [[],[]]
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
    
def q_m_1ar( animacy, base, base1 = None, base2 = None):
    # гражданин, римлянин
    inf = [[],[]]
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
    
def q_m_1cr1(animacy, base, base1 = None, base2 = None):
    # господин
    inf = [[],[]]
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
    inf[1].add(base2)
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base1)
    else:
        inf[1].add(base1 + 'а́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
    
def q_m_3ar( animacy, base, base1 = None, base2 = None):
    # цыплёнок
    inf = [[],[]]
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
    inf = [[],[]]
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
    #second option
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
    
def q_m_1a2( animacy, base, base1 = None, base2 = None):
    # грузин, мадьяр, алтын
    inf = [[],[]]
    inf[0].add(base)
    inf[0].add(base + 'а')
    inf[0].add(base + 'у')
    if animacy:
        inf[0].add(base)
    else:
        inf[0].add(base)
    inf[0].add(base + 'ом')
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
    
def q_m_1c2(animacy, base, base1 = None, base2 = None):
    # раз
    inf = [[],[]]
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
    inf[1].add(base)
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base)
    else:
        inf[1].add(base1 + 'ы́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
    
def q_m_1c12(animacy, base, base1 = None, base2 = None):
    # раз
    inf = [[],[]]
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
    inf[1].add(base)
    inf[1].add(base1 + 'а́м')
    if animacy:
        inf[1].add(base)
    else:
        inf[1].add(base1 + 'а́')
    inf[1].add(base1 + 'а́ми')
    inf[1].add(base1 + 'а́х')
    # end pl
    
def q_m_3c1( animacy, base, base1 = None, base2 = None):
    # снег, округ
    inf = [[],[]]
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
    inf = [[],[]]
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
    inf = [[],[]]
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
    
def q_m_5a2( animacy, base, base1 = None, base2 = None):
    # герц
    inf = [[],[]]
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
    
def q_m_3as2( animacy, base, base1 = None, base2 = None):
    # черевичек
    inf = [[],[]]
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
    inf = [[],[]]
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
    
def q_f_1a( animacy, base, base1 = None, base2 = None):
    # корова, лопата
    inf = [[],[]]
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
    
def q_f_2a( animacy, base, base1 = None, base2 = None):
    # богиня, неделя
    inf = [[],[]] 
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
    
def q_f_3a( animacy, base, base1 = None, base2 = None):
    # собака, книга
    inf = [[],[]]
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
    
def q_f_4a( animacy, base, base1 = None, base2 = None):
    # кассирша, туча
    inf = [[],[]]
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
    
def q_f_5a( animacy, base, base1 = None, base2 = None):
    # улица, проводница
    inf = [[],[]]
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
    
def q_f_6a( animacy, base, base1 = None, base2 = None):
    # фея, статуя
    inf = [[],[]]
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
    
def q_f_7a( animacy, base, base1 = None, base2 = None):
    # армия, рептилия
    inf = [[],[]]
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
    inf = [[],[]]
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
    inf = [[],[]]
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
    inf = [[],[]]
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
    inf = [[],[]]
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
    inf = [[],[]]
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
    
def q_f_7b( animacy, base, base1 = None, base2 = None):
    # судия, лития
    inf = [[],[]]
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