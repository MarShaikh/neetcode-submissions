class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        longest_length = 0
        l, r = 0, 0

        while r < len(s):
            if s[r] not in char_set:
                longest_length = max(longest_length, r - l + 1)
                char_set.add(s[r])
                r += 1
            else:
                char_set.remove(s[l])
                l += 1
        
        return longest_length