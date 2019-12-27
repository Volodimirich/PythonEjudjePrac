#Ввести целые M и N, вывести последовательность 0 1 2 3 4 5 6 7 8 9 0 1 2 3 …в виде спирально
#(по часовой стрелке, из верхнего левого угла) заполненной таблицы N×M (N строк, M столбцов).
#Не забываем про то, что M и N могут быть чётными, нечётными и неизвестно, какое больше.


Column,Line=eval(input())
a=[[0]*Column for i in range(Line)]
Amount=Line*Column
LineS=Line
ColumnS=Column
Op=i=offL=offC=0
while Op < Amount:
    for j in range(offC,Column):
        a[i][j]=Op%10
        Op+=1
    offL+=1
    for i in range(offL,Line):
        if Op < Amount:
            a[i][j]=Op%10
            Op+=1
    Column-=1
    for j in range(Column-1,offC-1,-1):
        if Op < Amount:
            a[i][j]=Op%10
            Op+=1
    Line-=1
    for i in range(Line-1,offL-1,-1):
        if Op < Amount:
            a[i][j]=Op%10
            Op+=1
    offC+=1

for i in range(LineS):
    for j in range (ColumnS):
        print(a[i][j],end=" ")
    print()
