class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_hash = {}
        res, l = 0, 0

        for r in range(len(s)):
            character_hash[s[r]] = 1 + character_hash.get(s[r], 0) # Gets the value of s[r] if exits, otherwise defaults to 0
            while (r - l + 1) - max(character_hash.values()) > k:
                character_hash[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res
        


"""
k: int

Choose up to k characters of the string and replace them with any other uppercase english character
After performing at most k replacements, return the length of the longest substring which contains only one distinct character. 

AAABBBABB k = 2

max(hash_map.values()) - len(r - l + 1) < k for a valid window
If window is valid: 
    max_length = max(len(r - l + 1), max_length)

l += 1

A: 2
B: 1

"""