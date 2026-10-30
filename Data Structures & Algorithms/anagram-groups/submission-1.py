class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            alphabet_array = [0] * 26
            for c in s:
                alphabet_array[ord(c) - ord('a')] += 1
            
            res[tuple(alphabet_array)].append(s)
        
        return list(res.values())