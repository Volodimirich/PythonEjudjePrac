#Написать функцию-параметрический декоратор fix(n), с помощью которой все вещественные (как позиционные, так и именные)
#параметры произвольной декорируемой функции, а также её возвращаемое значение, округляются до n-го знака после запятой.
#Если какие-то параметры функции оказались не вещественными, или не вещественно возвращаемое значение, эти объекты не меняются.

def fix(Accuracy):
    def MainDecorator(func):
        def Wrapper(*args,**kwargs):
            Numbers=[]
            for i in args:
                if isinstance(i,(int,float)):
                    Numbers+=[round(i,Accuracy)]
                else:
                    Numbers+=[i]
            return round(func(*Numbers,**kwargs),Accuracy) \
                   if isinstance(func(*Numbers,**kwargs),(int,float)) else func(*Numbers,**kwargs)
        return Wrapper
    return MainDecorator
