class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # to keep track of characters
        s_array = [0] * 26
        t_array = [0] * 26

        for i, j in zip(s, t):
            s_array[ord(i) - ord('a')] += 1
            t_array[ord(j) - ord('a')] += 1
        
        for i in range(26):
            if s_array[i] != t_array[i]:
                return False
        
        return True