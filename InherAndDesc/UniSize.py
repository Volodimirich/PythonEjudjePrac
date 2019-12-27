#Написать декоратор класса sizer, который добавляет в него поле size, равное длине объекта, если у объекта есть длина,
#или модулю целочисленного представления объекта в противном случае (предполагается, что ошибок нет).
#Предоставить пользователю возможность произвольно менять это поле.

class Halp(object):
    def __get__(self,obj,objtype):
        return abs(int(obj)) if isinstance(obj,(int,float)) else len(obj)
    
def sizer(cls):
    class  CU(cls):
        size=Halp()
    return CU 
