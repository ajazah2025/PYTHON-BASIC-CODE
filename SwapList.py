#Python program to interchange first and last elements in a list

def swapList(list):
    get = list[0], list[-1] # now get has two value first 1 and second 10
    list[-1] , list[0] = get  #Here whatever value get has is being assigned at given index like list[-1] = 1 and #list[0]= 10
    return list

newlist =[10,2,3,4,5,6,7,8,9,1]
print("The new list after interchanging first and last element:",swapList(newlist))



