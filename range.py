def range(stop,start=0,step=0):
    if start==0:
        while(start<stop):
          print(start)
          start+=1
    if step==0:
        while(start<stop):
          print(start)
          start+=1
    else:
        while(start<stop):
            print(start)
            start+=step


range(10)
print("---------------")
range(25,7)
print("---------------")
range(99,33,3)