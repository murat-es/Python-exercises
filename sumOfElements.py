numberOfElements=int(input("How many number you want to sum?: "))

list=[]
x=0
while x<numberOfElements:
    list.append(int(input(f"Please enter the {x+1}. elements: " )))
    x+=1

total=0
for i in list:
    total+=i
   
print("Sum of elements: ",total)