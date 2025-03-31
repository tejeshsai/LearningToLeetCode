# Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

# Problem Description:
# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order. It is guaranteed that the answer is unique.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Explanation: 1 appears 3 times, 2 appears 2 times, 3 appears 1 time
# The two most frequent elements are 1 and 2

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# Explanation: 1 is the only element in the array

# Example 3:
# Input: nums = [1,2,2,3,3,3], k = 3
# Output: [3,2,1]
# Explanation: 3 appears 3 times, 2 appears 2 times, 1 appears 1 time
# All three elements are returned as k=3

# Time Complexity: O(n) - we need to traverse the array once
# Space Complexity: O(n) - we need a hashmap to store frequencies

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number using a hashmap
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # Step 2: Create buckets where index represents frequency
        # freq[i] contains all numbers that appear i times
        freq = [[] for _ in range(len(nums)+1)]
        for n, c in count.items():
            freq[c].append(n)

        # Step 3: Build result by taking top k most frequent elements
        # Start from highest frequency (end of array) and move backwards
        res = []
        for i in range(len(freq)-1, 0, -1):
            res.append(freq[i])
            if len(res) == k:
                return res
        return res