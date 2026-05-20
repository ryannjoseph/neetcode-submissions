class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First, check if lengths are different
        if len(s) != len(t):
            return False
        
        # Create dictionaries to count character frequencies
        count_s = {}
        count_t = {}
        
        # Count characters in string s
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1
        
        # Count characters in string t
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1
        
        # Compare the two dictionaries
        return count_s == count_t