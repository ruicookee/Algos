'''Write a Python program to sort a list of elements using the insertion sort algorithm.

Note : According to Wikipedia "Insertion sort is a simple sorting algorithm that builds the final sorted 
array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms 
such as quicksort, heapsort, or merge sort."

Sample Data: [14,46,43,27,57,41,45,21,70]
Expected Result : [14, 21, 27, 41, 43, 45, 46, 57, 70]'''

def inssort(lst):
    for i in range(1, len(lst)):
        current = lst[i]
        n = i - 1
        while n >= 0 and current < lst[n]:
            lst[n+1] = lst[n]
            n -= 1
        lst[n+1] = current
    return lst

#i dont really like this one please relook at it

print(inssort([14,46,43,27,57,41,45,21,70]))