y=int(input("enter a no\n"))
flag=1
for x in range(2, y, +1):
    if y%x == 0:
        print("Not prime")
        flag=0
        break
if flag==1:
    print("It is prime")

   
         
            
    
