''''
Input : arr[] = {3, 1, 2}
           k = 1
Output : arr[] = {1, 2, 3}

'''

def splitArr(arr,k):
    c = arr[k:]+ arr[:k]
    return c

#Initializing the value.
arr=[5,1,2,3,4]
k=1
result = splitArr(arr,k) #calling function
print("The new array is after spliting",result)

