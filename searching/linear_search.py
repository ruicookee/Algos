'''Write a Python program for sequential search.

Sequential Search : In computer science, linear search or sequential search 
is a method for finding a particular value in a list that checks each element
in sequence until the desired element is found or the list is exhausted. 
The list need not be ordered.

Test Data :
Sequential_Search([11,23,58,31,56,77,43,12,65,19],31) -> (True, 3)'''

def seqsearch(lst, target):
    # good ol search
    for index, num in enumerate(lst):
        if num == target:
            return (True, index)
    return False    
    
        
print(seqsearch([11,23,58,31,56,77,43,12,65,19],31))