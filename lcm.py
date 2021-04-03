a=int(input("enter the number"))
b=int(input("enter the number"))
if a>b:
    m=a
else:
    m=b
while 1:
    if m%a==0 and m%b==0:
        print("lCM is:",m) 
        break
    m+=1       