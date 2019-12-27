#Написать, держитесь крепче, генератор-декоратор statcounter(), который конструирует объекты (назовём один из них stat)
#со следующим поведением. Первый вызов next(stat) (он же stat.send(None)) возвращает словарь, в котором stat будет хранить информацию
#вида функция: количество вызовов, где функция — это исходный (не обёрнутый) объект-функция (да, так тоже можно!).
#Все последующие вызовы stat.send(function) оборачивают вызов произвольной функции function увеличением
#на 1 соответствующего элемента словаря. Глобальными именами пользоваться нельзя.
#В примере видны уникальные id объектов, в тестах их не будет (я воспользуюсь function.__name__ или просто не буду их учитывать).

def statcounter():
    Dict={}
    New_fun=yield Dict
    def MainDecoratior(fun):
        def Wrapper(*args,**kwargs):
            Check=Dict.get(fun)
            Dict[fun]=Check+1 if Check else 1
            return fun(*args,**kwargs)
        return Wrapper
    while (New_fun):
        New_fun = yield MainDecoratior(New_fun)
