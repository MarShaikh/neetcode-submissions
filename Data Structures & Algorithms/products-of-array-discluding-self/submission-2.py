class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        res = [1] * n 

        prefix[0] = postfix[n-1] = 1
        # calculate prefix product array
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
                    
        # calculate postfix product array
        for i in range(n - 2, -1, -1):
            postfix[i] = nums[i + 1] * postfix[i + 1]
                    
        # calculate final product
        for i in range(n):
            res[i] = prefix[i] * postfix[i]
                    
        return res