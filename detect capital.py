s=input()
flag=0
l=[]
for x in s[0::]:
      if s.islower()==True:
        flag=1
        print('true')
        #return True
        exit()

for x in s:
     if x.isupper()==True:
        l.append(1)
     else:
        l.append(0)
if all(l) == True:
    print(True)
    flag=1
    exit()

if s == s.capitalize():
    print(True)
    flag=1
    exit()

if flag==0:
    print("No capilizatin ")
    print(False)
