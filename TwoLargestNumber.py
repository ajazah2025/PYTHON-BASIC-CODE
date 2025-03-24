# Input : [4, 5, 1, 2, 9] 
# N = 2
# Output :  [9, 5]

def LargestNumber(list,n):
    list.sort()
    value = list[-n:]
    return value


list = [4, 5, 1, 2, 9]
n = 2
print("The two largest element in the given list are",LargestNumber(list,n))'
