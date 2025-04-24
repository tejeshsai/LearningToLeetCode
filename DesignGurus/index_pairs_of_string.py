"""
1065. Index Pairs of a String
Easy

Given a text string and words (a list of strings), return all index pairs [i, j] so that the substring text[i...j] is in the list of words.

Example 1:
Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
Output: [[3,7],[9,13],[10,17]]

Example 2:
Input: text = "ababa", words = ["aba","ab"]
Output: [[0,1],[0,2],[2,3],[2,4]]
Note: The returned pairs can be in any order.

Constraints:
1 <= text.length <= 100
1 <= words.length <= 20
1 <= words[i].length <= 50
text consists of lowercase English letters only.
words[i] consists of lowercase English letters only.
"""

class TrieNode:
    def __init__(self) -> None:
        self.children = {}  # Dictionary to store child nodes
        self.isEnd = False  # Flag to mark end of a word

class Solution:
    def __init__(self) -> None:
        self.root = TrieNode()  # Initialize root of the trie
    
    def insert(self, word):
        # Insert a word into the trie
        curr = self.root
        for i in word:
            if not curr.children.get(i, None):
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.isEnd = True  # Mark the end of the word
    
    def indexPairsOfStrings(self, text, words):
        # Build trie with all words
        for word in words:
            self.insert(word)
            
        result = []
        # For each starting position in text
        for i in range(len(text)):
            p = self.root
            # Try to match words starting from position i
            for j in range(i, len(text)):
                currCharacter = text[j]
                if not p.children.get(currCharacter, None):
                    break  # No matching word found, try next starting position
                p = p.children[currCharacter]
                if p.isEnd:  # If we found a complete word
                    result.append([i,j])
        
        return result

if __name__ == "__main__":
    solution = Solution()
    # Test cases
    print("Test Case 1:")
    print(solution.indexPairsOfStrings("thestoryofleetcodeandme", ["story","fleet","leetcode"]))
    print("\nTest Case 2:")
    print(solution.indexPairsOfStrings("ababa", ["aba","ab"]))