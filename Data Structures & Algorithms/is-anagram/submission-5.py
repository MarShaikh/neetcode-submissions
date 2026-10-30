class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charS, charT = [0] * 26, [0] * 26
        for p, q in zip(s, t):
            charS[ord(p) - ord('a')] += 1
            charT[ord(q) - ord('a')] += 1
        
        for i in range(len(charS)):
            if charS[i] != charT[i]:
                return False

        return True