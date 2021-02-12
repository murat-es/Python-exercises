def fib(term,count):
    fib1=0
    fib2=1
    
    if(term==1):
        return
    else:
        while count<term:
            fib3=fib1+fib2
            
            print(fib3)
            fib1=fib2
            fib2=fib3
            
            count+=1    
    
    return fib(term-1,count)

COUNT=1
fib(10,COUNT)