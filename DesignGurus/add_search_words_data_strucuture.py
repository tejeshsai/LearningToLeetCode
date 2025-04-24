# 211. Design Add and Search Words Data Structure
# Medium

# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:
# - WordDictionary() Initializes the object.
# - void addWord(word) Adds word to the data structure, it can be matched later.
# - bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
#   word may contain dots '.' where dots can be matched with any letter.

# Example:
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]

# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True

class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes for each character
        self.children = {}  
        # Flag to mark the end of a word
        self.isEnd = False  

class WordDictionary:
    def __init__(self):
        # Initialize the root node of the trie
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """Add a word into the data structure.
        
        Args:
            word: The word to be added to the dictionary
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        """Search for a word in the data structure.
        
        Args:
            word: The word to search for, may contain dots '.' as wildcards
            
        Returns:
            bool: True if the word exists in the dictionary, False otherwise
        """
        return self.dfs(self.root, word, 0)

    def dfs(self, node: TrieNode, word: str, index: int) -> bool:
        """Helper function to perform DFS search with wildcard support.
        
        Args:
            node: Current node in the trie
            word: The word being searched
            index: Current position in the word
            
        Returns:
            bool: True if a match is found, False otherwise
        """
        # Base case: we've reached the end of the word
        if index == len(word):
            return node.isEnd

        char = word[index]
        
        # If current character is a wildcard
        if char == '.':
            # Try all possible children
            for child in node.children.values():
                if self.dfs(child, word, index + 1):
                    return True
            return False
        
        # If current character is not a wildcard
        if char not in node.children:
            return False
            
        # Continue search with the next character
        return self.dfs(node.children[char], word, index + 1)

# Test cases
if __name__ == "__main__":
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    
    print(wordDictionary.search("pad"))  # False
    print(wordDictionary.search("bad"))  # True
    print(wordDictionary.search(".ad"))  # True
    print(wordDictionary.search("b.."))  # True