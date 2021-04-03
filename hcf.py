num1=int(input("enter the num"))
num2=int(input("enter the num"))
while num1%num2!=0:
    rem=num1%num2
    num1=num2
    num2=rem
if num2==rem:
    print("hcf is",num2)    


