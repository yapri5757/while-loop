a=int(input("enter number"))
b=1
i=1
sum=0
while i<=a:
    b=i*b
    sum=sum+b
    i=i+1
    print(b,end=",")