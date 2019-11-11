#Ввести небольшое натуральное число 2⩽N⩽1000000 и проверить, является ли
#оно степенью натурального числа (>1). Вывести YES и NO соответственно.
import math
number=eval(input())
n=2;
while( n <= math.sqrt(number)):
    copy=number
    while copy!=1:
        if copy%n == 0:
            copy=copy//n
        else:
            break
    if copy==1:
        print("YES")
        break
    n+=1
if (number<4 or copy!=1):
    print("NO")
