

from math import *
f=eval(f"lambda x: {input('')}")
left,right=eval(input(""))
while (right-left > 0.000001):
    point=(right+left)/2;
    
    if (f(point)>0):
        right=point
    else:
        left=point
print(right)
