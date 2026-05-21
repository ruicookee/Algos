'''Merge Sorted Array
https://neetcode.io/problems/merge-sorted-array/question
You are given two integer arrays nums1 and nums2, 
both sorted in non-decreasing order, along with two integers m and n, where:

m is the number of valid elements in nums1,
n is the number of elements in nums2.
The array nums1 has a total length of (m+n), with the first m elements containing the values to be merged, and the last n elements set to 0 as placeholders.

Your task is to merge the two arrays such that the final merged array is also sorted in non-decreasing order and stored entirely within nums1.
You must modify nums1 in-place and do not return anything from the function.

Example 1:

Input: nums1 = [10,20,20,40,0,0], m = 4, nums2 = [1,2], n = 2

Output: [1,2,10,20,20,40]'''
def merge(nums1, m, nums2, n):
    ### Three pointer approach
    p1 = m-1
    p2 = n-1
    last = m+n-1
    
    while p1 >= 0 and p2 >= 0: #neither nums1 nor nums2 have been emptied
        if nums1[p1] > nums2[p2]:
            nums1[last] = nums1[p1]
            p1 -= 1
        else: # if nums2[p2] is bigger than or equal, if its equal then it will loop back again anyway
            nums1[last] = nums2[p2]
            p2 -= 1
        last -= 1
    
    while p2 >= 0: #only nums2 will ever be not emptied because in nums1, the remaining number will already be in place
        nums1[last] = nums2[p2]
        p2 -= 1
        last -= 1
    
    return nums1




nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n))
    