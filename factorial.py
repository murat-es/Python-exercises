number=int(input("Please enter the number thah factorial you want to find: "))
no=number

factorial=1
while(number>1):
    factorial*=number
    number-=1

print("Factorial of ",no," = ",factorial)