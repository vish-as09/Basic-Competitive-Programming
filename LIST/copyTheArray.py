A = list(map(int,input().split()))
element=int(input("Enter element : "))
A2=[]
sum=0
for i in A:
    i=i+element
    A2.append(i)
print("The existing list : ",A)
print("the Added list is : ",A2)