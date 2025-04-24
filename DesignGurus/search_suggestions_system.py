"""
1268. Search Suggestions System
Medium

You are given an array of strings products and a string searchWord. Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix with searchWord, return the three lexicographically smallest products.

Return a list of lists of the suggested products after each character of searchWord is typed.

Example 1:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo, all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]

Example 2:
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Constraints:
1 <= products.length <= 1000
1 <= products[i].length <= 3000
1 <= sum(products[i].length) <= 2 * 10^4
All the strings of products are unique.
products[i] consists of lowercase English letters.
searchWord consists of lowercase English letters.
"""

from typing import List

class TrieNode:
    def __init__(self) -> None:
        self.children = {}  # Dictionary to store child nodes
        self.isEnd = False  # Flag to mark end of a word

class Solution:
    def __init__(self):
        self.root = TrieNode()  # Initialize root of the trie

    def buildTree(self, products: List[str]) -> None:
        """Build a trie from the products list."""
        for word in products:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.isEnd = True

    def dfs(self, node: TrieNode, prefix: str, result: List[str]) -> List[str]:
        """Perform DFS to find all words with given prefix.
        
        Args:
            node: Current node in the trie
            prefix: Current prefix string
            result: List to store matching words
            
        Returns:
            List of up to 3 matching words
        """
        if len(result) == 3:
            return result
        
        if node.isEnd:
            result.append(prefix)

        # Try all characters in lexicographical order
        for ch in sorted(node.children.keys()):
            self.dfs(node.children[ch], prefix + ch, result)
            if len(result) == 3:
                break
                
        return result
    
    def searchByWord(self, prefix: str) -> List[str]:
        """Search for words with given prefix.
        
        Args:
            prefix: The prefix to search for
            
        Returns:
            List of up to 3 matching words
        """
        node = self.root
        result = []
        
        # First, navigate to the node corresponding to the prefix
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        
        # Then, find all words with this prefix
        return self.dfs(node, prefix, result)
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """Get suggestions for each character typed.
        
        Args:
            products: List of product names
            searchWord: The search word being typed
            
        Returns:
            List of lists containing up to 3 suggestions for each prefix
        """
        # Sort products lexicographically
        products.sort()
        self.buildTree(products)
        result = []
        prefix = ""
        
        # For each character typed, get suggestions
        for ch in searchWord:
            prefix += ch
            result.append(self.searchByWord(prefix))
            
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    products1 = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord1 = "mouse"
    print("Test Case 1:")
    print("Input: products =", products1, ", searchWord =", searchWord1)
    print("Expected: [['mobile','moneypot','monitor'], ['mobile','moneypot','monitor'], ['mouse','mousepad'], ['mouse','mousepad'], ['mouse','mousepad']]")
    print("Actual:", solution.suggestedProducts(products1, searchWord1))
    
    # Test Case 2
    products2 = ["havana"]
    searchWord2 = "havana"
    print("\nTest Case 2:")
    print("Input: products =", products2, ", searchWord =", searchWord2)
    print("Expected: [['havana'], ['havana'], ['havana'], ['havana'], ['havana'], ['havana']]")
    print("Actual:", solution.suggestedProducts(products2, searchWord2))
    
    # Test Case 3 - Empty products
    products3 = []
    searchWord3 = "mouse"
    print("\nTest Case 3:")
    print("Input: products =", products3, ", searchWord =", searchWord3)
    print("Expected: [[], [], [], [], []]")
    print("Actual:", solution.suggestedProducts(products3, searchWord3))
    
    # Test Case 4 - No matches
    products4 = ["code","coder","coding"]
    searchWord4 = "apple"
    print("\nTest Case 4:")
    print("Input: products =", products4, ", searchWord =", searchWord4)
    print("Expected: [[], [], [], [], []]")
    print("Actual:", solution.suggestedProducts(products4, searchWord4))