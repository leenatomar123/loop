element=[23,45,56,18,23,45]
a=0
sum=0
sum1=0
while a<len(element):
    if element[a]%2==0:
       sum+=element[a] 
    else:
        a+=1
print(sum,"sum of even number")
        

