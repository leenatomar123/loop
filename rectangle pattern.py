num=int(input("enter the number"))
row=1
while row<num:
    col=1
    while col<num:
        print("*",end="")
        col+=1
    print()
    row=row+1    