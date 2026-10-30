class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        res = [] 
        product = 1
                    
        # calculate prefix product array
        for i in range(len(nums)):
            prefix[i] = product
            product *= nums[i]
                    
           # calculate postfix product array
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = product
            product *= nums[i]
                    
        # calculate final product
        for a, b in zip(prefix, postfix):
            res.append(a * b)
                    
        return res