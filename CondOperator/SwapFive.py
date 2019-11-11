numb=eval(input())
digit=numb*numb
major=0
counter=1
final=numb
while digit!=numb:
    if digit>=10:
        major=digit//10
    digit=digit%10
    final=final+digit*(10**counter)
    digit=digit*numb+major
    major=0
    counter+=1
print(final)
