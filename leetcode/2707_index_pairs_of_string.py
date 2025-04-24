"""
2707. Index Pairs of a String
https://leetcode.com/problems/index-pairs-of-a-string/

Given a text string and words (a list of strings), return all index pairs [i, j] such that the substring text[i...j] is in the list of words. Return the pairs [i,j] in sorted order (i.e., sort them by their first coordinate in case of ties sort them by their second coordinate).

Example 1:
Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
Output: [[3,7],[9,13],[10,17]]

Example 2:
Input: text = "ababa", words = ["aba","ab"]
Output: [[0,1],[0,2],[2,3],[2,4]]
Explanation: 
Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].
"""

class Solution:
    def indexPairs(self, text: str, words: list[str]) -> list[list[int]]:
        result = []
        for word in words:
            start = 0
            while True:
                index = text.find(word, start)
                if index == -1:
                    break
                result.append([index, index + len(word) - 1])
                start = index + 1
        
        # Sort the result
        result.sort()
        return result

def test_indexPairs():
    solution = Solution()
    
    # Test case 1
    text1 = "thestoryofleetcodeandme"
    words1 = ["story","fleet","leetcode"]
    expected1 = [[3,7],[9,13],[10,17]]
    assert solution.indexPairs(text1, words1) == expected1
    
    # Test case 2
    text2 = "ababa"
    words2 = ["aba","ab"]
    expected2 = [[0,1],[0,2],[2,3],[2,4]]
    assert solution.indexPairs(text2, words2) == expected2
    
    # Test case 3: No matches
    text3 = "abc"
    words3 = ["def"]
    expected3 = []
    assert solution.indexPairs(text3, words3) == expected3
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_indexPairs() 