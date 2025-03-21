#Creating function to sum of array
def Array_sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum

#main function
if __name__== "__main__":
    arr = [1,2,3]                     #input value to the list
    result= Array_sum(arr)            #calling function

print("The sum of array is",result)   #printing value on screen 