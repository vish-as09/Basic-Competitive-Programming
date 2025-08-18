a1=int(input("Enter your first angle:"))
a2=int(input("Enter your second angle:"))
a3=int(input("Enter your third angle:"))
sum=a1 + a2 + a3
if(sum == 90):
    print("The triangle is right angle triangle.")
elif(sum <90 and sum>180):
    print("The triangle is right obtuse triangle.")
elif(sum>90):
    print("The triangle is right acute triangle.")
else:
    print("The triangle is not valid.")


