#Написать класс sausage, имитирующий киберколбасу. Киберколбаса может быть проинициализирована нулём значений
#(создаётся колбаса по умолчанию), одним (фарш) и двумя (фарш и объём). Длина целого батона киберколбасы 12 символов фарша
#и 2 оболочки. Колбаса единичного объёма — это один полный батон, более, чем единичного — это несколько батонов
#(последний, возможно, неполон). Неполный батон заканчивается срезом. Киберколбаса поддерживает операции умножения и
#деления на целое число, а также сложения и вычитания с другой киберколбасой
#(фарш результата совпадает с фаршем первого операнда). Если объём киберколбасы нулевой, батон считается пустым.

from fractions import Fraction
import copy
class sausage:
    def __init__(self,Str="pork!",Leng=1):
        self.Base=(Str*(12//len(Str) + 1))[0:12]
        self.LengF=Fraction(12)*Fraction(Leng)


    def __add__(self,other):
        _copy = copy.deepcopy(self)
        _copy.LengF += other.LengF
        return _copy

    def __sub__(self,other):
        _copy = copy.deepcopy(self)
        _copy.LengF -= other.LengF
        return _copy
    
    def __mul__(self,other):
        _copy = copy.deepcopy(self)
        _copy.LengF *= Fraction(other)
        return _copy
    __rmul__=__mul__

    def __truediv__(self, other):
        _copy = copy.deepcopy(self)
        _copy.LengF /= Fraction(other)
        return _copy

    def __bool__(self):
        return True if self.LengF>0 else False


    def __str__(self):
        Fin=""
        Top="/"+"-"*12+"\\"
        Middle="|"+self.Base+"|"
        Low="\\"+"-"*12+"/"
        if self.LengF<0:
            self.LengF=0
            return "/|\n||\n||\n||\n\|"
        ind=1 if self.LengF%12 else 0
        Fin+=Top*(self.LengF//12)+Top[0:int(self.LengF%12)+ind]
        Fin+="|"*ind +"\n"
        for i in range(3):
            Fin+=Middle*(self.LengF//12)+Middle[0:int(self.LengF%12)+ind]
            Fin+="|"*ind +"\n"
        Fin+=Low*(self.LengF//12)+Low[0:int(self.LengF%12)+ind]
        Fin+="|"*ind
        return Fin
    
