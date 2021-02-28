number=int(input("Enter the number: "))
no=number

countDigit=1
while(number>9):
    countDigit+=1
    number=number//10

print("The number ",no," has",countDigit,"digits.")