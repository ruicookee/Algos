'''Remove All Occurrences of an Element in an Array
https://www.geeksforgeeks.org/dsa/remove-element/
'''
def remover(lst, ele):
    ### fast and slow pointers, very cool
    # slow for pos to insert, fast to check which are the acceptable ones to fit into lst
    # changing the array in place
    slow = 0
    for fast in range(len(lst)):
        if lst[fast] != ele:
            lst[slow] = lst[fast]
            
            if fast > slow:
                 lst[fast] = None
            
            slow += 1
        else:
            lst[fast] = None
    return lst

print(remover([3, 2, 2, 3, 4, 2, 5], 2))
'''
[2, 3, 2, 3, 4, 2, 5]
[None, 3, 2, 3, 4, 2, 5]
arr = [3, 2, 2, 3, 4, 2, 5]
ele = 2
print(remover())
'''