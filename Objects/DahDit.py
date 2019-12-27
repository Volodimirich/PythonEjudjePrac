#Написать класс morse("строка"), экземпляр которого переводит арифметические выражения в морзянку!
#Параметр «строка» бывает разных видов, более подробно описан в подсказках, желающие могут догадаться о его компонентах
#по примеру (пример почти полный). «+» — точка, «-» — тире, «~» — промежуток между буквами
#(бывает только между буквами и только один, проверять не надо).

from collections import deque
class morse:
    alpha={"+":"di","-":"dah","~":","}
    end="."
    last_char={"+":"dit","-":"dah"}
    sep=" "
    #buffer=""
    def __init__(self,Str_arg=""):
        self.buffer = deque()
        Str=Str_arg.split(" ")
        if len(Str)==1:
            if len(Str[0])>=2:
                self.sep=""
                self.end=""
                self.alpha["+"]=Str[0][0]
                self.alpha["-"]=Str[0][1]
                self.alpha["~"]=" "
                self.last_char["+"]=self.alpha["+"]
                self.last_char["-"]=self.alpha["-"]
            if len(Str[0])>=3:
                self.alpha["-"]=Str[0][2]
                self.last_char["+"]=Str[0][1]
                self.last_char["-"]=self.alpha["-"]
                self.alpha["~"]=" "
            if len(Str[0])==4:
                self.end=Str[0][3]
        elif len(Str)>=2:
            self.sep = ""
            self.alpha["-"]=Str[1]
            self.alpha["+"]=Str[0]
            self.alpha["~"]=" "
            self.last_char["+"]=self.alpha["+"]
            self.last_char["-"]=self.alpha["-"]
            if len(Str)>=3:
                self.sep=" "
                self.alpha["~"]=","
                self.last_char["+"]=Str[1]
                self.alpha["-"]=Str[2]
                self.last_char["-"]=self.alpha["-"]
            if len(Str)==4:
                self.end=Str[3]

    def __str__(self):
        Fin = ""
        if len(self.buffer) ==0:
            return self.end
        for i in range(len(self.buffer)):
            elem = self.buffer[i]
            next_elem=self.buffer[i+1] if i < len(self.buffer) - 1 else None
            loc_sep=self.sep if next_elem is not None and next_elem!="~" else ""
            Fin +=self.dec(elem,next_elem) + loc_sep
        return Fin.lstrip()
            
    def dec(self,elem,next_elem=None):
        if next_elem:
            if elem == "~":
                return self.alpha[elem]
            if next_elem == "~":
                return self.last_char[elem]
            else:
                return self.alpha[elem]
        else:
            return self.last_char[elem]+self.end

    
    def __pos__(self):
        self.buffer.appendleft("+")
        return self

    def __neg__(self):
        self.buffer.appendleft("-")
        return self

    def __invert__(self):
        self.buffer.appendleft("~")
        return self
