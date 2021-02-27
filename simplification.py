numerator=int(input("Enter the numerator: "))
denumerator=int(input("Enter the denumerator: "))

if(numerator>denumerator):
    small=numerator
else:
    small=denumerator


for i in range(small+1,1,-1):
    if(numerator%i==0 and denumerator%i==0):
        numerator/=i
        denumerator/=i

print("\nnumerator = ",int(numerator),"\ndenumerator = ",int(denumerator))