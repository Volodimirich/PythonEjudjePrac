#Написать функцию moar(a, b, n) от трёх параметров — целочисленных кортежей a и b, и натурального числа n.
#Функция возвращает True, если в a больше чисел, кратных n, чем в b, и False в противном случае.

def moar(Data1,Data2,number):
    counter=0
    for elem in Data1:
        if elem%number==0:
            counter+=1
    for elem in Data2:
        if elem%number==0:
            counter-=1
    if counter>0:
        return True
    else:
        return False
