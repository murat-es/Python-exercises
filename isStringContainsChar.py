string=input("Please enter the string: ")
character=input("Please enter the character you want to find: ")

countChar=0
for i in string:
    if (i==character):
        countChar+=1

if(countChar==0):
    print(f"String doesn't contain '{character}'")
else:
    print(f"String contains '{character}' {countChar} times")