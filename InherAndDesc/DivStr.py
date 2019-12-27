#Написать класс DivStr(str), полностью (за исключением правых операций со строками) воспроизводящий работу str.
#Дополнительно класс должен поддерживать операцию деления «/n», где n — натуральное число, которая должна возвращать
#n-ю часть от начала строки (если не делится, округлённую в меньшую сторону, если n>len(s) — пустую строку).
#Задача в том, чтобы любое возвращаемое методами значение типа str превращалось в DivStr.
#Согласно документации, мы не можем подсунуть методы, начинающиеся на «__», прямо в __dict__, или поймать __getattr__-ом,
#или даже __getattribute__-ом, а должны задать их явно, например, с помощью def.
#С другой стороны, руками все методы перебивать не хочется.

import math
class DivStr(str):
    def __init__(self,st):
        self.string=str(st)
    def __truediv__(self,numb):
        Fract,Integ=math.modf(1/numb)
        return DivStr(self.string*int(Integ)+self.string[0:int(len(self.string)*Fract)])
    for meth,methtype in str.__dict__.items():
        if callable(methtype) and meth not in ["__class__","__new__","__getattribute__","__getattr__","__repr__","__str__"]:
           exec(f"def {meth}(self,*args,**kwargs):\n"
                f" StrFin = str.{meth}(self,*args)\n"
                f" return DivStr(StrFin) if isinstance(StrFin,str) else StrFin")
