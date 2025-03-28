# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Input: nums = [1, 2, 3, 3]

# Output: true

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))