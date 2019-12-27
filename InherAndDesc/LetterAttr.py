#Написать класс LetterAttr, в котором будут допустимы поля с любым именем;
#значение каждого поля по умолчанию будет совпадать с именем поля (строка), а при задании нового строкового значения туда
#будут попадать только буквы, встречающиеся в имени поля.

class LetterAttr():
    def __getattr__(self,attr):
        return attr
    def __setattr__(self,attr,value):
        if attr == value:
            self.__dict__[attr] = value
        else:
            List=""
            for elem in value:
                if elem in attr:
                    List+=str(elem)
                self.__dict__[attr]=List
