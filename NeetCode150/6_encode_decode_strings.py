# Encode and Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings/

# Problem Description:
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network 
# and is decoded back to the original list of strings. The encoding/decoding algorithm should work with any string 
# containing any possible characters out of 256 valid ASCII characters.

# Example 1:
# Input: ["Hello","World"]
# Output: ["Hello","World"]
# Explanation: The encoded string is "5#Hello5#World"
# When decoded, it returns the original list ["Hello","World"]

# Example 2:
# Input: [""]
# Output: [""]
# Explanation: Empty string is encoded as "0#"
# When decoded, it returns the original list [""]

# Example 3:
# Input: ["Hello","#World","123"]
# Output: ["Hello","#World","123"]
# Explanation: The encoded string is "5#Hello6##World3#123"
# When decoded, it returns the original list ["Hello","#World","123"]

# Time Complexity: O(n) where n is the total length of all strings
# Space Complexity: O(n) to store the encoded string

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Handle empty input case
        if not strs:
            return ""
        # Initialize result string
        res = ""
        # For each string in input list
        for string in strs:
            # Encode as: length + "#" + string
            res+=str(len(string))+"#"+string
        return res

    def decode(self, s: str) -> List[str]:
        # Initialize result list and pointer
        res, i = [], 0
        # Continue until we reach end of string
        while i < len(s):
            # Build length string until we hit delimiter
            length = ""
            while s[i]!="#":
                length += s[i]
                i+=1
            # Skip the delimiter
            i+=1
            # Convert length string to integer
            length = int(length)
            # Extract the actual string using length
            res.append(s[i:i+length])
            # Move pointer past current string
            i+=length
        return res