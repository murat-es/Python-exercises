import math

print("ax^2 + bx + c")
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))

delta=(b**2)-4*a*c

if(delta>0):
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print("The roots are {} and {}".format(x1,x2))

elif(delta==0):
    x1=-b/(2*a)
    print(f"The root is {x1}")
else:
    print("There is no reel root.")