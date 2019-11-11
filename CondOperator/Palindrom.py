a=eval(input())
if (a%10 == 0):
    print("NO")
else:
    while a>0:
        counter=0
        first=a
        while (first>=10):
            first=first//10
            counter+=1
        last=a%10
        if (first!=last):
            print("NO")
            break
        a=(a-first*(10**counter))//10
if (a==0):
    print("YES")
