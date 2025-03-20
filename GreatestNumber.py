# Getting input from user to find greatest number.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

#Using logical operator find the greatest of 3 numbers entered by the user..
if(a>b) and (a>c):
    print("Greatest number is ",a )

elif(b>a) and (b>c):
    print("Greatest number is ",b)  

else:
    print("Greatest number is ",c)
