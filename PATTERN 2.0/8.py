n=int(input())
r=n//2
if (n%2==0):
    r+=0
else:
    r+=1
print(r)
for i in range(1,n+1):
    if(i==r):
        for j in range(1,2):
            print("*",end=" ")
    else:
        for j in range(1,3):
            print("*",end=" ")
    print( )
