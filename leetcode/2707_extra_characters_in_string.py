"""
2707. Extra Characters in a String
https://leetcode.com/problems/extra-characters-in-a-string/

You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

Example 1:
Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

Example 2:
Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
"""

class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]  # Initialize with worst case
            
            for word in dictionary:
                if i + len(word) <= n and s[i:i + len(word)] == word:
                    dp[i] = min(dp[i], dp[i + len(word)])
        
        return dp[0]

def test_minExtraChar():
    solution = Solution()
    
    # Test case 1
    s1 = "leetscode"
    dictionary1 = ["leet","code","leetcode"]
    assert solution.minExtraChar(s1, dictionary1) == 1
    
    # Test case 2
    s2 = "sayhelloworld"
    dictionary2 = ["hello","world"]
    assert solution.minExtraChar(s2, dictionary2) == 3
    
    # Test case 3: Empty string
    s3 = ""
    dictionary3 = ["a"]
    assert solution.minExtraChar(s3, dictionary3) == 0
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_minExtraChar() 