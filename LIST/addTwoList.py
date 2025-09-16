A = list(map(int,input().split()))
A1 = list(map(int,input().split()))
sum=[]
for i in range(len(A)):
    sum.append(A[i]+A1[i])
print("list1: ",A)
print("list2: ",A1)
print("Sum of lists",sum)