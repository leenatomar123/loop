i=5
n=1
a=10
while n<=a:
    s=int(input("enter the number"))
    if s==1:
        print("you win")
        break
    elif s!=i and  s<a:
        print(a-5,"remaining chances")
    else:
        print("you have no chance")
    a-=s    