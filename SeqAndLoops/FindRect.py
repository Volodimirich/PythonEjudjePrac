#Ввести несколько строк одинаковой длины, состоящих из символов '#' и '.'.
#Первый и последний символ каждой строки — '.', а первая и последняя строки состоят целиком из '-'. Известно (проверять не надо),
#что на получившемся поле изображены только прямоугольника, причём они не соприкасаются даже углами.
#Вывести количество этих прямоугольников.

GlCounter=FirPos=Counter=0
String=str(input())
Del=[]
Fin=[]
Step=[]
Leng=len(String)
Glflag=flag=False
while Glflag==False:
    String=str(input())
    for char in String:
        if char=='-':
            Glflag=True
        if char=='#':
            if not flag:
                FirPos=Counter
                flag=True
        if char=='.':
            if flag:
                Step.append((FirPos,Counter-1))
                flag=False
        Counter+=1
    if flag:
        Step.append((FirPos,Leng))
        print(FirPos,Leng)
        flag=False
    for elem in Fin:
        if elem not in Step:
            GlCounter+=1
            Del.append(elem)
    for elem in Del:
        Fin.remove(elem)
    for elem in Step:
        if elem not in Fin:
            Fin.append(elem)
    Step.clear()
    Del.clear()
    Counter=0
for elem in Fin:
    GlCounter+=1
    Fin.remove(elem)
print(GlCounter)
