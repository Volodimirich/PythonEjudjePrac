#Написать программу — калькулятор с переменными и обработкой ошибок Команда, начинающаяся на '#' — комментарий
#Команда вида Переменная=выражение задаёт переменную Команда вида выражение выводит значение выражения.
#Если команда содержит знак "=", но не является присваиванием, выводится диагностика "invalid assignment" (см. пример)
#Если слева от "=" находится не идентификатор, выводится диагностика "invalid identifier (см. пример)"
#В случае любых других ошибок выводится текст ошибки.
#«Выражение» — это произвольное выражение Python3, в котором вдобавок можно использовать уже определённые переменные
#(и только их). Пробелов в командах нет. Пустая команда означает конец вычислений.
#Калькулятор вводит и исполняет команды по одной, тут же выводя диагностику, но в тестах это выглядит как ввод
#последовательности строк и вывод последовательности строк.

StrIn=str(input())
Space={}
Space['__builtins__']=dir(__builtins__)
GlSpace={}
while StrIn!="." and StrIn!="":
    try:
        print((eval(StrIn, GlSpace, Space)))
    except BaseException as e:
        if "=" in StrIn and "==" not in StrIn:
            Pos=StrIn.find("=")
            if Pos != 0 and Pos<len(StrIn) and not (StrIn[0]>="0" and StrIn[0]<="9"):
                Space[StrIn[0:Pos]]=eval(StrIn[Pos+1:],GlSpace, Space)
            elif (StrIn[0]>="0" and StrIn[0]<="9"):
                print("invalid identifier","'"+StrIn[0:StrIn.find("=")]+"'")
            else:
                print(e)
        elif "==" in StrIn:
            print("invalid assignment","'"+StrIn+"'")
        elif StrIn[0] != "#":
            print(e)
    StrIn=str(input())
