import random
import string

def generatePassword(length):
    password=[]
    chars= "{}{}{}".format(string.ascii_letters,string.digits,string.punctuation)
     
    i=0
    while i<length:
        password.append(random.choice(chars))
        i+=1
    
    return "".join(password)

print(generatePassword(12))