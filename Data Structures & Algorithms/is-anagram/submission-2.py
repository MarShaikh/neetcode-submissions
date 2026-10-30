class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_dict = {}
        for subs in s:
            if subs in anagram_dict:
                anagram_dict[subs] += 1
            else:
                anagram_dict[subs] = 1
        
        print(anagram_dict)
        for subs in t:
            if subs in anagram_dict:
                if anagram_dict[subs] == 0:
                    return False
                anagram_dict[subs] -= 1
            else:
                return False
        
        for k, v in anagram_dict.items():
            if v > 0:
                return False
        return True
            
        