"""
2707. Extra Characters in a String
Medium

You are given a string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

Example 1:
Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

Example 2:
Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra. Hence, we return 3.

Constraints:
1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
dictionary[i] and s consists of only lowercase English letters
dictionary contains distinct words
"""

class TrieNode:
    def __init__(self) -> None:
        self.children = {}  # Dictionary to store child nodes
        self.isEnd = False  # Flag to mark end of a word
    
class Solution:
    def __init__(self):
        self.root = TrieNode()  # Initialize root of the trie
        self.memo = None  # Memoization array

    def buildTree(self, dictionary):
        """Build a trie from the dictionary words."""
        for word in dictionary:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.isEnd = True
    
    def dfs(self, start: int, s: str) -> int:
        """Perform DFS with memoization to find minimum extra characters.
        
        Args:
            start: Current position in the string
            s: The input string
            
        Returns:
            int: Minimum number of extra characters from start position
        """
        if start == len(s):
            return 0
        
        if self.memo[start] is not None:
            return self.memo[start]
        
        # Initialize with the case where we skip current character
        minExtra = self.dfs(start + 1, s) + 1
        
        # Try to match words starting from current position
        node = self.root
        for end in range(start, len(s)):
            if s[end] not in node.children:
                break
            node = node.children[s[end]]
            
            if node.isEnd:
                minExtra = min(minExtra, self.dfs(end + 1, s))
        
        self.memo[start] = minExtra
        return minExtra

    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        """Find the minimum number of extra characters in s.
        
        Args:
            s: The input string
            dictionary: List of valid words
            
        Returns:
            int: Minimum number of extra characters
        """
        self.memo = [None] * len(s)
        self.buildTree(dictionary)
        return self.dfs(0, s)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    s1 = "leetscode"
    dictionary1 = ["leet","code","leetcode"]
    print("Test Case 1:")
    print("Expected: 1")
    print("Actual:", solution.minExtraChar(s1, dictionary1))
    
    # Test Case 2
    s2 = "sayhelloworld"
    dictionary2 = ["hello","world"]
    print("\nTest Case 2:")
    print("Expected: 3")
    print("Actual:", solution.minExtraChar(s2, dictionary2))
