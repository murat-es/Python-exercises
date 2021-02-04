list=[1,7,9,5,4,14,89,45,32,2]

search=int(input("Please enter the number you want search: "))
check=False

for i in range(len(list)):
    if(search==list[i]):
        print("You found it",search,"at index of",i)
        check=True
        break

if(check==False):
    print(search,"not found")