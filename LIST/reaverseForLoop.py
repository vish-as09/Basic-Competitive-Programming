A = list(map(int,input().split()))
n=(len(A))
for i in range(0,n//2):
    A[i],A[n-1-i]=A[n-1-i],A[i]
print("the Reversed Array is : ",A)