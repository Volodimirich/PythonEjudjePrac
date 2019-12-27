#Написать функцию maxfun(), которая принимает переменное число параметров — числовую последовательность S, функцию F1 и,
#возможно, ещё несколько функций F2 … Fn. Возвращает она ту из функций Fi, сумма значений которой на всех элементах S наибольшая.
#Если таких функций больше одной, возвращается Fi с наибольшим i.

def maxfun(Interval, *Data):
    flag=False
    NumFunc=Sum=SumTemp=0
    for counter,DataElem in enumerate(Data):
        for i in Interval:
            SumTemp=SumTemp+DataElem(i)
        if SumTemp>=Sum or not flag:
            flag=True
            Sum=SumTemp
            NumFunc=counter
        SumTemp=0;
    return(Data[NumFunc])
