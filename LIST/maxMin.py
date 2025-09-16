A = list(map(int,input().split()))
max=A[0]
min=A[0]
for i in A:
    if(i>max):
        max=i
    if(i<min):
        min=i
print("Maximum element: ",max)
print("Minimum element: ",min)
