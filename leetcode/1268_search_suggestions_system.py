"""
1268. Search Suggestions System
https://leetcode.com/problems/search-suggestions-system/

You are given an array of strings products and a string searchWord. Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically smallest products.

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
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
"""

class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        result = []
        prefix = ""
        
        for char in searchWord:
            prefix += char
            suggestions = []
            for product in products:
                if product.startswith(prefix):
                    suggestions.append(product)
                    if len(suggestions) == 3:
                        break
            result.append(suggestions)
        
        return result

def test_suggestedProducts():
    solution = Solution()
    
    # Test case 1
    products1 = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord1 = "mouse"
    expected1 = [
        ["mobile","moneypot","monitor"],
        ["mobile","moneypot","monitor"],
        ["mouse","mousepad"],
        ["mouse","mousepad"],
        ["mouse","mousepad"]
    ]
    assert solution.suggestedProducts(products1, searchWord1) == expected1
    
    # Test case 2: Empty products
    products2 = []
    searchWord2 = "mouse"
    expected2 = [[], [], [], [], []]
    assert solution.suggestedProducts(products2, searchWord2) == expected2
    
    # Test case 3: No matches
    products3 = ["abc", "def", "ghi"]
    searchWord3 = "xyz"
    expected3 = [[], [], []]
    assert solution.suggestedProducts(products3, searchWord3) == expected3
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_suggestedProducts() 