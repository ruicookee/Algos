'''Valid Palindrome II
You are given a string s, return true if the s can be a palindrome after deleting at most one character from it.
https://neetcode.io/problems/valid-palindrome-ii/question

Input: s = "aca"
Output: true

Input: s = "abbda"
Output: true
'''
def delete_to_palindrome(s):
    p1 = 0
    p2 = len(s)-1
    counter = 0
    
    while p1 < p2:
        if s[p1] != s[p2]:
            if s[p1+1] == s[p2]:
                counter += 1
                p1 += 1
                continue
            elif s[p1] == s[p2-1]:
                counter += 1
                p2 -= 1
                continue
            else:
                return False
        p1 += 1
        p2 -= 1
    return counter <= 1