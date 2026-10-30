class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # to keep track of the characters
        s_arr = [0] * 26 
        t_arr = [0] * 26

        # count of characters in string s and t
        for i, j in zip(s, t):
            s_arr[ord(i) - ord('a')] += 1
            t_arr[ord(j) - ord('a')] += 1
        
        # compare the character counts
        for i in range(26):
            if s_arr[i] != t_arr[i]:
                return False
        
        return True

