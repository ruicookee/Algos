'''Write a Python program to sort a list of elements using the selection sort algorithm.

Note : The selection sort improves on the bubble sort by making only one exchange for every pass through the list. 

Sample Data: [14,46,43,27,57,41,45,21,70]
Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70]'''

def selsort(lst):
    # each loop:
    ### note min value index
    ### at the end of loop, swap current with min value
    for i in range(0, len(lst)-1):
        min_val_index = i
        for n in range(i+1, len(lst)):
            if lst[n] < lst[min_val_index]:
                min_val_index = n
        lst[i], lst[min_val_index] = lst[min_val_index], lst[i]
    return lst

    '''This is not stable cause relative order of repeated elements may change
    ie.[4a, 2, 4b, 1]'''

print(selsort([14,46,43,27,57,41,45,21,70]))