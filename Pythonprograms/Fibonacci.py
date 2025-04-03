n=int(input("Enter a number:"))
a=0
b=1
while n>0:
    print(a,end=" ")
    c=a+b
    b=a
    a=c
    n=n-1