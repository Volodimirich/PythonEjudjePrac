#Ввести построчно четвёрки вида «число число число слово», где первые три числа — это координаты галактики по имени «слово»
#(некоторые галактики могут называться одинаково, но координаты у всех разные).
#Последняя строка ввода не содержит пробелов и не учитывается.
#Вывести в алфавитном порядке имена любых двух наиболее удалённых друг от друга галактик.

from itertools import *

def GetDistance(FirPoint,SecPoint):
    return (FirPoint[0]-SecPoint[0])**2+(FirPoint[1]-SecPoint[1])**2+(FirPoint[2]-SecPoint[2])**2

Data=[]
MaxLen=-1
Galaxy=input().split()
while (Galaxy[0]!='.'):
    Data.append((float(Galaxy[0]),float(Galaxy[1]),float(Galaxy[2]),Galaxy[3]))
    Galaxy=input().split()
for Elems in combinations(Data,2):
    StepLen=GetDistance(Elems[0],Elems[1])
    if MaxLen<StepLen:
        MaxLen=StepLen
        FirName=Elems[0][3]
        SecName=Elems[1][3]

if FirName>SecName:
    print(SecName,FirName)
else:
    print(FirName,SecName)
