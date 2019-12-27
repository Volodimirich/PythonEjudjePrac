#Вводятся строки, содержащие четыре целых числа и символ, разделённые пробелами. Код символа 32 < c < 128.
#Это абсцисса, ордината, длина и ширина прямоугольников, «нарисованных» с помощью указанных символов.
#Последняя строка начинается на четыре нуля (никаких трюков с -0 на этот раз ☺).
#Вывести наименьшую область, содержащюю все прямоугольники, нарисованные в порядке их ввода.
#Область также прямоугольна и изначально заполнена символами '.'. Координаты и размеры могут быть отрицательны или равны нулю.

XCord,YCord,XLen,YLen,symb=input().split(' ')
XCord,YCord,XLen,YLen = int(XCord),int(YCord),int(XLen),int(YLen)
LeftBorder=min(XCord,XCord+XLen)
RightBorder=max(XCord,XCord+XLen)
DownBorder=min(YCord,YCord+YLen)
UpBorder=max(YCord,YCord+YLen)
Borders=[LeftBorder,RightBorder,DownBorder,UpBorder]
Bunch=[[XCord,YCord,XLen,YLen,symb]]
while True:
    XCord,YCord,XLen,YLen,symb=input().split(' ')
    XCord,YCord,XLen,YLen = int(XCord),int(YCord),int(XLen),int(YLen)
    if (XCord==0 and YCord==0 and XLen==0 and YLen==0):
        break
    if XLen==0 or YLen==0:
        continue
    Borders[0]=min(XCord,XCord+XLen,Borders[0])
    Borders[1]=max(XCord,XCord+XLen,Borders[1])
    Borders[2]=min(YCord,YCord+YLen,Borders[2])
    Borders[3]=max(YCord,YCord+YLen,Borders[3])
    Bunch.append([XCord,YCord,XLen,YLen,symb])

FinalField=[]
SortData=[]

for i in range(Borders[3]-Borders[2]):
    FinalField.append(list('.')*(Borders[1]-Borders[0]))

for Data in Bunch:
    X=Data[0]-Borders[0]+Data[2] if Data[2]<0 else Data[0]-Borders[0] 
    Y=Data[1]-Borders[2]+Data[3] if Data[3]<0 else Data[1]-Borders[3]
    SortData.append([X,Y,abs(Data[2]),abs(Data[3]),Data[4]])

for Data in SortData:
    for YPos in range(Data[1],Data[3]+Data[1]):
        for XPos in range(Data[0],Data[2]+Data[0]):
            FinalField[YPos][XPos]=Data[4]

for string in FinalField:
    print(*string,sep='')
