# Getting input from user 
num=int(input("Enter the number you want to check factorial:"))

#Intialize the factorial variable to 1
factorial=1

#Calculate the factorial using loop
for i in range(1,num+1):
    factorial = i*factorial  #factorial *=i

#print the factorial of that number.
print(f"Factorial of {num} is {factorial}")    
