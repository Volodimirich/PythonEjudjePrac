#Написать функцию fcounter(), которая первым параметром получает некоторый класс, а остальные параметры применяет
#для создания экземпляра этого класса. Функция должна возвращать 4 отсортированных списка: имена методов класса,
#имена полей класса, имена методов, которые появились в экземпляре и имена полей, которые появились в экземпляре
#(под «полями» имеются в виду не-callable() объекты).

def StatFound(Cl):
    MethH,FielH=[],[]
    for Elem in dir(Cl):
        if callable(getattr(Cl,Elem)) and Elem[0]!="_":
            MethH.append(Elem)
        elif Elem[0]!="_":
            FielH.append(Elem)
    return(MethH,FielH)

def fcounter(Cl,*args):
    Res=Cl(*args)
    cm,cf,om,of=[],[],[],[]
    cm,cf=StatFound(Cl)
    om,of=StatFound(Res)
    om=list(set(om)-set(cm))
    of=list(set(of)-set(cf))
    return (sorted(cm),sorted(cf),sorted(om),sorted(of))
