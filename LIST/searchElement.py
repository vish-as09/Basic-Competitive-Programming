A = list(map(int,input().split()))
element = int(input("Enter element to be searched"))
search=False
for i in A:
    if(i==element ):
        search=True
        break
if(search==True):
    print("Element Founded!!")
else:
    print("Element not Found!!")