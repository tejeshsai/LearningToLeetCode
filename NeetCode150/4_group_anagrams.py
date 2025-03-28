# Group Anagrams
# https://leetcode.com/problems/group-anagrams/

# Problem Description:
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An anagram is a word formed by rearranging the letters of another word.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Time Complexity: O(n * k) where n is number of strings and k is max length of string
# Space Complexity: O(n * k) to store all strings

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen_map = {}  # Store character count -> list of anagrams
        for s in strs:  # Iterate through each string
            count = [0] * 26  # Count array for 26 lowercase letters
            for c in s:  # Count frequency of each character
                count[ord(c) - ord("a")] += 1
            key = str(count)  # Convert count array to string for hashmap key
            if key in seen_map:  # If we've seen this anagram pattern before
                seen_map[key].append(s)  # Add current string to its group
            else:  # If this is a new anagram pattern
                seen_map[key] = [s]  # Create new group with current string
        return list(seen_map.values())  # Return all groups 