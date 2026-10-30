class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        length = 0
        set_nums = set(nums)

        for i in set_nums:
            if (i - 1) not in set_nums:
                length = 1
                while (i + length) in set_nums:
                    length += 1
            
            longest = max(longest, length)

        return longest

"""
[2 6 4 5 8 1 2 0 7 3 9]

(2 6 5 8 1 0 7 3 9)
consecutive sequence: 0 1 2 3 
consecutive sequence: 5 6 7 8 9
"""