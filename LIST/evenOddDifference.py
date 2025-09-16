A = list(map(int,input().split()))
sum_even=0
sum_odd=0
for i in range(len(A)):
    if (A[i]%2 == 0):
        sum_even=abs(sum_even-A[i])
    else:
        sum_odd=abs(sum_odd-A[i])
print(sum_even-sum_odd)