# Find Median from Data Stream
# https://leetcode.com/problems/find-median-from-data-stream/

# Problem Description:
# Implement the MedianFinder class:
# - MedianFinder() initializes the MedianFinder object.
# - void addNum(int num) adds the integer num from the data stream to the data structure.
# - double findMedian() returns the median of all elements so far.

# Example:
# Input:
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output:
# [null, null, null, 1.5, null, 2.0]

# Time Complexity:
# - insertNum: O(log n)
# - findMedian: O(1) - Note: The current implementation pops elements which is not correct
# Space Complexity: O(n) where n is the number of elements in the data stream

import heapq
class Solution:
    def __init__(self) -> None:
        # Min heap for the larger half of numbers
        self.min_heap = []
        # Max heap for the smaller half of numbers (using negative values)
        self.max_heap = []
    
    def insertNum(self, num):
        # Add number to the appropriate heap
        if not self.max_heap or num > self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)

        # Balance the heaps
        if len(self.max_heap) > len(self.min_heap)+1:
            top = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -top)
        if len(self.min_heap) > len(self.max_heap):
            top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -top)

    def findMedian(self):
        # Find median based on heap sizes
        if len(self.min_heap) == len(self.max_heap):
            return (-heapq.heappop(self.max_heap)/2.0 + heapq.heappop(self.min_heap)/2.0)
        else:
            return -heapq.heappop(self.max_heap)/1.0
