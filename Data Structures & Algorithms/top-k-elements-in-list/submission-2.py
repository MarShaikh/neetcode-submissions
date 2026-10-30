class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        count_list = [[] for i in range(len(nums) + 1)]

        # getting counts of nums in the list and adding them to a hashmap
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        # using the index of `count_list` as count for the nums
        for key, value in hashmap.items():
            count_list[value].append(key)

        res = []
        # adding top K frequent values in a list
        tl = 0
        res = []
        for i in range(len(count_list) - 1, 0, -1):
            for c in count_list[i]:
                res.append(c)
                if len(res) == k:
                    return res

        
