#Написать рекурсивную функцию binpow(), которая принимает три параметра: python3-объект a, натуральное число 0<N<1000000,
#и некоторую ассоциативную бинарную функциюf(). Функция binpow() реализует алгоритм бинарного возведения в степень
#(кроме нулевой степени). Результатом binpow(a, n, f) будет применение f(x) к a n-1 раз. Более точно, binpow(a, 1, f) == a,
#binpow(a, 2, f) == f(a,a), binpow(a, 3, f) == f(a,f(a, a)) == f(f(a, a), a) (в силу ассоциативности),… binpow(a, n, f) == f(f(…f(a, a), …), a).

def BinPow(elem,qty,operation):
    if qty==1:
        return elem
    if qty %2 == 1:
        return operation(BinPow(elem,qty-1,operation),elem)
    else:
        amount=BinPow(elem,qty/2,operation);
        return operation(amount,amount)
