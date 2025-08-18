#if a number is divsible by 3 and last digit is 4
num=int(input("Enter your number : "))
n=num%10
if(num%3==0 and n==4):
    print("YOur number is divisible by 3 and having last digit 4")
else:
    print("Any of or both the conditions are not fulfilling") 