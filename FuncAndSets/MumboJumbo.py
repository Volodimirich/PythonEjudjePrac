#Ввод представляет собой строки из букв латинского алфавита. Это иероглифические письмена на языках двух племён: Mumbo и Jumbo.
#Чётные строки — предложения одного языка, нечётные — другого (какого — неизвестно). Иероглифы Mumbo и Jumbo частично одинаковые,
#3а частично разные. Предложения на каждом языке в данном корпусе текстов содержат все разрешённые в этом языке иероглифы
#(т. е. если иероглиф разрешён в языке, он встречается хотя бы в одном предложении на этом языке).
#Если строка пустая, это признак окончания ввода. Известно, что в уникальном алфавите Mumbo иероглифов больше,
#чем в уникальном алфавите Jumbo. Определить и вывести, на каком языке написано первое предложение — Mumbo или Jumbo.

Leng1=set()
Leng2=set()
Mess=str(input())
flag=1
while Mess:
    if flag:
        Leng1=Leng1|set(Mess)
    else:
        Leng2=Leng2|set(Mess)
    flag=not flag
    Mess=str(input())
print("Jumbo") if len(Leng2)>len(Leng1) else print("Mumbo")