
a=int(input("Enter the number"))

b=0
c=int(a/2)
while b<a:
    if(b<c):
        print((a-b)*" ",b*"*",end="")
        print(b*"*")
    else:
        print((a-c)*" ",c*"*",end="")
        print(c*"*")
        c=c-1
    b+=1