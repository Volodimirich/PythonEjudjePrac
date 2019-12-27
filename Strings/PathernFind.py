#Ввести строку, содержащую произвольные символы (кроме символа «@»). Затем ввести строку-шаблон,
#которая может содержать символы '@'. Проверить, содержится ли в исходной строке подстрока, совпадающая со строкой-шаблоном везде,
#кроме символов '@'; на месте '@' в исходной строке должен стоять ровно один произвольный символ.
#Вывести наименьшую позицию в строке, с которой начинается эта подстрока, или '-1', если её там нет.
#Использовать регулярные выражения нельзя!

InputData=str(input())
Data=str(input())
Incounter=counter=0
StartPos=len(InputData)+1
Pattern=Data.split(',')
for PatElm in Pattern:
    while Incounter < len(InputData):
        if counter==0:
            while counter<len(PatElm) and PatElm[counter]=='@':
                counter+=1
            if counter>len(InputData):
                break
            if counter==len(PatElm):
                if StartPos>Incounter-len(PatElm)+1:
                    StartPos=0;
                    Incounter=0
                break
        if PatElm[counter]==InputData[Incounter] or PatElm[counter]=='@':
            counter+=1
        else:
            counter=0
            DogOffset=0
        if counter==len(PatElm):
            if StartPos>Incounter-len(PatElm)+1:
                StartPos=Incounter-len(PatElm)+1;
                Incounter=0
            break
        Incounter+=1
    counter=DogOffset=Position=0        
if StartPos==len(InputData)+1:
    StartPos=-1
print(StartPos)
