#read a number check if a number is divisible by or last digit is 7 or  last digit 5
num=int(input("enter your number : "))
n=num%10
if(num%7==0 and n==5):
    print("Your number is divisible by 7 and having last digit 5")

elif(num%7==0):
    print("Your number is only divisible by 7 but not having last digit 5")
elif(n==5):
    print("Your number is not divisible by 7 but having last digit 5")
else:
    print("Your number is not divisible by 7 and not having last digit 5")