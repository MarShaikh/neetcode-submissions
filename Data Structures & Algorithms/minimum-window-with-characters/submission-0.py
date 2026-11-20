class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t):
            return ""
        
        t_hashmap = {}
        window = {}
        for char in t: 
            t_hashmap[char] = 1 + t_hashmap.get(char, 0)
        
        have, need = 0, len(t_hashmap) # count unique chars in t
        res, resLen = [-1, -1], float("infinity")

        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in t_hashmap and window[char] == t_hashmap[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l , r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in t_hashmap and window[s[l]] < t_hashmap[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""

