class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""  # If the input list is empty, there is no common prefix
        
        # Find the length of the shortest string in the list
        min_len = min(len(s) for s in strs)
        
        # Initialize the common prefix as an empty string
        common_prefix = ""
        
        # Iterate through the characters of the first string
        for i in range(min_len):
            # Get the current character
            char = strs[0][i]
            
            # Compare the current character with the corresponding character in other strings
            for s in strs:
                if s[i] != char:
                    return common_prefix  # Return the common prefix if a mismatch is found
            
            # If all characters match, add the character to the common prefix
            common_prefix += char
        
        return common_prefix