number=int(input("Please enter the number whose factors you want to find: "))

for i in range(1,number):
    if(number%i==0):
        print(i)