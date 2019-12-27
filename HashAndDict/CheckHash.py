#Написать функцию checkhash(seq, f, mod), которой на вход подаётся последовательность неравных друг другу (это гарантируется)
#хешируемых объектов, хеш-функция и число mod. Функция просматривает остатки от деления на mod значения f() на всех объектах
#из seq и возвращает список из двух элементов — наибольшее и наименьшее количество произошедших коллизий.

def checkhash(seq,f,mod):
    DictHash=dict()
    for i in seq:
        NewVal=f(i)%mod
        if NewVal in DictHash:
            DictHash[NewVal]+=1
        else:
            DictHash[NewVal]=1
    return (max(DictHash.values()), min(DictHash.values()))
