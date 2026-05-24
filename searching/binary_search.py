'''Binary Search
Write a Python program for binary search.
Binary Search : In computer science, a binary search or half-interval search algorithm 
finds the position of a target value within a sorted array. 
The binary search algorithm can be classified as a dichotomies divide-and-conquer
 search algorithm and executes in logarithmic time.

Test Data :
binary_search([1,2,3,5,8], 6) -> False
binary_search([1,2,3,5,8], 5) -> True
'''

def binarysearch(lst, target):
    #repeatedly halving sorted list till you get what you want
    start = 0
    end = len(lst)-1
    while start <= end:
        if target == lst[(start+end)//2]:
            return True
        elif target < lst[(start+end)//2]:
            end = ((start+end)//2)-1
        else:
            start = (start+end)//2+1
    return False


    '''LISTEN
    there are only 3 meaningful relationships
    1) start < end --> there are a few elements in between to be checked
    2) start == end --> there is only one element left to be checked
    3) start > end --> overrun, none in between left
    dont doubt intuition
    '''

print(binarysearch([1,2,3,5,8], 6))
print(binarysearch([1,2,3,5,8], 5))