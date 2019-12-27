#Ввести в столбик последовательность целых (положительных и отрицательных) чисел,не равных нулю;
#в конце этой последовательности стоит 0. Вывести наибольшую сумму последовательно идущих элементов этой последовательности.

CheckSum=0
num=int(input())
Sum=num
while (num!=0):
    CheckSum+=num
    Sum= CheckSum if CheckSum>Sum else Sum
    num=int(input())
    if CheckSum<0:
        CheckSum=0
print(Sum)
