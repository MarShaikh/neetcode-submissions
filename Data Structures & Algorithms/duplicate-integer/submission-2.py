class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _hash_set = set()

        for n in nums:
            if n in _hash_set:
                return True
            _hash_set.add(n)
        return False