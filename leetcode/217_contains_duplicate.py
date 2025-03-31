# Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

# Problem Description:
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation: The value 1 appears twice in the array

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: All values appear only once in the array

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true
# Explanation: The values 1, 2, 3, and 4 all appear multiple times

# Time Complexity: O(n) - we need to traverse the array once
# Space Complexity: O(n) - we need a hashset to store unique numbers

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))