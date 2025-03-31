# Two Sum
# https://leetcode.com/problems/two-sum/

# Problem Description:
# Given an array of integers nums and an integer target, return indices of the two numbers in nums 
# such that they add up to target. You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] = 2 + 7 = 9, we return [0, 1]

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Explanation: Because nums[1] + nums[2] = 2 + 4 = 6, we return [1, 2]

# Example 3:
# Input: nums = [-1,-2,-3,-4,-5], target = -8
# Output: [2,4]
# Explanation: Because nums[2] + nums[4] = -3 + -5 = -8, we return [2, 4]

# Time Complexity: O(n) - we only need to traverse the array once
# Space Complexity: O(n) - we need a hashmap to store numbers and their indices

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # Store numbers and their indices for O(1) lookup
        for i, num in enumerate(nums):  # Iterate through array with indices
            complement = target - num  # Calculate what we need to find
            if complement in seen:  # Check if we've seen the complement
                return [seen[complement], i]  # Return both indices if found
            seen[num] = i  # Store current number and its index
        return []  # No solution found