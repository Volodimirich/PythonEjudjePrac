#Вводится кортеж пар натуральных чисел. Это координаты отрезков на прямой.
#Рассмотрим объединение этих отрезков и найдём длину этого объединения
#(т. е. совокупную длину всех «закрашенных» нашими отрезками отрезков на прямой)

Data=eval(input())
SortData=sorted(Data)
flag = True
Sum=i=0
Leng=len(SortData)-1
while flag:
    if Leng>0:
        if SortData[i][1]>SortData[i+1][0]:
            if SortData[i][1]<SortData[i+1][1]:
                SortData.insert(i,(SortData[i][0],SortData[i+1][1]))
                SortData.pop(i+1)
            SortData.pop(i+1)
            calc=0
            Leng-=1
        else:
            i+=1
            Leng-=1
    else:
        flag=False
for Interval in SortData:
    Sum+=Interval[1]-Interval[0]
print(Sum)
