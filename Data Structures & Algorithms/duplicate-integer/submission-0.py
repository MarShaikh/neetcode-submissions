class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for n in nums: 
            if n in hash: 
                if hash[n] == 1:
                    return True
            hash[n] = 1
        return False
        