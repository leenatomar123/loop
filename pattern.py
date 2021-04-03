num=int(input("enter the number"))
column=1
while column<=num:
    row=1
    while row<column:
      print(row,end="")
      row+=1
    k=column
    while k>0:
        print(k,end="")
        k-=1
    print()
    column+=1      