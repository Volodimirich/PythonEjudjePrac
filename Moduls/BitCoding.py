#Написать модуль, в котором будет 4 функции. Первые две: shex(n), которая переводит число n в 64-ричное представление,
#и xehs(s), которая переводит строку с 64-ричным числом в число. 64-ричная система счисления пользуется «цифрами» с ASCII-кодом
#от 32 до 32+63=95 (т. е. от пробела до подчёркивания) включительно.
#Функция encode(txt) упаковывает строку txt, состоящую из символов диапазона " "…"_" по следующим правилам.
#Символы, встретившиеся в тексте, упорядочиваются по убыванию частоты их появления в тексте (вторичный ключ — сам символ).
#Самому частому (и с наибольшим ASCII-кодом, если таковых несколько) ставится в соответствие бит "0",
#следующему — последовательность битов "10", следующему — "110", и т. д.
#Биты записываются единой строкой, строка дополняется нулями, если это необходимо, и превращается в 64-ричное число.
#Функция encode(txt) возвращает кортеж (длина txt, строка упорядоченных символов, закодированная строка).
#Четвёртая функция, decode(length, chars, code), раскодирует строку code, используя описанное выше сопоставление chars битам,
#и возвращает раскодированную строку длиной length

from collections import *
from operator import itemgetter
from math import ceil

def shex(n):
    FinStr=""
    Numb=str(bin(n))[2:]
    Rem=6-len(Numb)%6 if len(Numb)%6 else 0
    Numb="0"*Rem+Numb
    for i in range (len(Numb)//6):
        Str=Numb[6*i:6*(i+1)]
        Str="0b"+Str
        FinStr+=(chr(32+int(Str,2)))
    return FinStr

def xehs(Str):
    Numb=0
    i=0
    for elem in Str[-1::-1]:
        Numb+=(ord(elem)-32)*(64**i)
        i+=1
    return Numb

def encode(Str):
    CodMes,FinStr,CodeStr="","",""
    Dict=defaultdict(int)
    for Value in Str:
        Dict[Value]+=1
    SorDic=sorted(list(Dict.items()),key=itemgetter(1,0),reverse=True)
    for elem in SorDic:
        CodMes+=elem[0]
    for let in Str:
        CodeStr+="1"*CodMes.find(let)+"0"
    Rem=6-len(CodeStr)%6 if len(CodeStr)%6 else 6
    CodeStr+="0"*Rem
    return (len(Str),CodMes,shex(int(CodeStr,2)))


def decode(*data):
    Str=bin(xehs(data[2]))[2:]
    Coun=0
    Leng=data[0]
    Mes=''
    for let in Str:
        if let=='1':
            Coun+=1
        else:
            Mes+=data[1][Coun]
            Leng-=1
            Coun=0
        if not Leng:
            break
    return str(Mes)
