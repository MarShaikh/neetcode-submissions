class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = 1
        left_array, right_array = [], []
        
        for n in nums:
            left_array.append(left_prod)
            left_prod = n * left_prod

        right_prod = 1
        for n in reversed(nums):
            right_array.append(right_prod)
            right_prod = n * right_prod

        res = []
        for n, m in zip(left_array, reversed(right_array)):
            res.append(n * m)
        
        return res