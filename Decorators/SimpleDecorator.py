#Написать функцию-декоратор nonify(func), которая заменяет возвращаемое значение функции func на None,
#если оно было пустое (и не меняет в противном случае).

def nonify(func):
    def Wrapper(*args,**kwargs):
        return func(*args, **kwargs) if func(*args, **kwargs) else None
    return Wrapper
