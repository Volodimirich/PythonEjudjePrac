#Написать функцию chainslice(begin, end, seq0, seq1, …), которая принимает не менее трёх параметров:
#два целых числа и не менее одной последовательности.
#Рассмотрим последовательность seq, образованную всеми элементами seq0,затем — всеми элементами seq1, и т. д.
#Вернуть эта функция должна итератор, пробегающий элементы последовательности seq с №begin до №end-1 включительно.

from itertools import *
def chainslice(begin,end,*seq):
    for i in  islice((chain.from_iterable(seq)), begin, end):
        yield i
