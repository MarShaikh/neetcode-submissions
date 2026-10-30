class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array: List = [1] * len(nums)
        right_array: List = [1] * len(nums)
        res = [1] * len(nums)

        for i in range(1, len(nums)):
            left_array[i] = nums[i-1] * left_array[i-1]
        
        for i in range(len(nums) - 2, -1, -1):
            right_array[i] = nums[i + 1] * right_array[i + 1]

        for i in range(len(nums)):
            res[i] = left_array[i] * right_array[i]
        
        return res

"""
nums: [1 2 4 6]

left array: [1 1.1 2.1]
right array: [48 24 6 1]

"""