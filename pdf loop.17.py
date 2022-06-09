a=input("enter number")
i=0
digit=len(a)
sum=0
while i<len(a):
    b=a[i]
    c=(int(b)**3)
    sum=c+sum
    i=i+1
if int(a)==sum:
        print("it is armstrong number")
else:
        print("not armstrong number")