def sum(a,b):
    print("result is",a+b,"\n")

def substract(a,b):
    print("result is",a-b,"\n")

def multiply(a,b):
   print("result is",a*b,"\n")

def divide(a,b):
    print("result is",a/b,"\n")

while True:
    operation=int(input("for addition -------> press 1 \nfor subtraction ----> press 2"
    "\nfor multiplication -> press 3 \nfor division -------> press 4"
    "\nto quit ------------> press 0\nEnter the operation: "))

    if(operation==0):
        print("exiting...")
        break
    if(not(0<operation<5)):
        print("invalid choice\n")
        continue

    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))

    
    if(operation==1):
        sum(a,b)
    elif(operation==2):
        substract(a,b)
    elif(operation==3):
        multiply(a,b)
    elif(operation==4):
        divide(a,b)