# Valid Anagram
# https://leetcode.com/problems/valid-anagram/

# Problem Description:
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An anagram is a word formed by rearranging the letters of another word.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Explanation: "nagaram" is an anagram of "anagram" because it contains the same letters

# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Explanation: "car" is not an anagram of "rat" because they contain different letters

# Example 3:
# Input: s = "aacc", t = "ccac"
# Output: false
# Explanation: "ccac" is not an anagram of "aacc" because they have different letter frequencies

# Time Complexity: O(n) - we need to traverse both strings once
# Space Complexity: O(1) - we only need a fixed-size array of 26 characters

# Constraints:
# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count = [0]*26
        for i in range(0, len(s)):
            count[ord(s[i])-ord("a")] += 1
            count[ord(t[i])-ord("a")] -= 1
        
        for val in count:
            if val != 0:
                return False
        
        return True