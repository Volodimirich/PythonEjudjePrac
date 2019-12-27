#Ввести два натуральных числа через запятую: N и M. Вывести таблицу умножения от 1 до N включительно в формате,представленном ниже.
#Количество столбцов в выводе должно быть наибольшим, но общая ширина строки не должна превышать M
#(предполагается, что M достаточно велико, чтобы вместить один столбец).
#Ширина колонок под сомножители и произведения должна соответствовать максимальной ширине соответствующего значения
#(даже если в данной колонке данного столбца эта ширина не достигается, см. пример).
#Таким образом все столбцы должны быть одинаковой ширины, без учёта пробелов в конце строк, которых быть не должно.
#Разделители вида "===…===" должны быть ширины M.

Number,Leng=eval(input())
Min=1
Offset=len(str(Number))
Lastarg=len(str(Number*Number))
OutForm=""
Form="{:{}d} * {:<{}d}= {:<{}d}"
ColLeng=len(Form.format(1,Offset,1,Offset+1,1,Lastarg))
SpaceStr=""
OutStr=""
SpaceStr=SpaceStr.ljust(Leng,"=")
while True:
    print(SpaceStr)
    for j in range(1,Number+1):
        TempLen=Leng
        Sec=Min
        EndFlag=True
        while TempLen>ColLeng:
            OutForm=Form.format(Sec,Offset,j,Offset+1,j*Sec,Lastarg)
            TempLen-=ColLeng
            if TempLen-3>ColLeng and Sec<Number:
                OutStr+=OutForm+" | "
                TempLen-=3
            else:
                OutStr+=OutForm
                print(OutStr)
                OutStr=""
                TempLen=0
            Sec+=1
            if Sec>Number:
                break
    Min=Sec
    if Sec>Number:
        break
print(SpaceStr)
