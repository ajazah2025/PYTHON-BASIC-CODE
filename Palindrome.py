s = input("Enter the string:")
#first way
str1 = s[0:]
str2 = s[::-1]

if str1 == str2:
    print("The given string is a Palindrome")
else:
    print("The given string is not a Palindrome")

#Second way
s = "malayalam"
rev = ''.join(reversed(s))
if s == rev:
    print("Yes")
else:
    print("No")
