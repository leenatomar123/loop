num=int(input("enter the number"))
sum=0
b=num
order=len(str(num))
while num>0:
    digit=num%10
    sum=sum+(order**digit)
    print(sum)
    num=num//10
if sum==b:
    print(b,"is armstrong numbrer")
else:        
    print(b,"is not armstrong number")