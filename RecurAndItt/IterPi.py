#Пользуясь формулой Лейбница для вычисления числа Пи, написать бесконечный генератор pigen(),
#возвращающий последовательно 4, 4-4/3, 4-4/3+4/5, 4-4/3+4/5-4/7…;Data=eval(input())

from itertools import count

def pigen():
    Pi=4
    for n in count():
        if n>0:
            Pi=Pi+((-1)**(n)) * 4/(2*n+1)
        yield Pi
