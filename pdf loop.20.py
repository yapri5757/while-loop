a=int(input("enter number"))
r=0
i=a
while a>0:
    r=(r*10)+a%10
    a=a//0
if i==r:
    print("palindrome number")
else:
    print("not palindrome")