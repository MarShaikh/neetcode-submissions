class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        count_list = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        for key, value in hashmap.items():
            count_list[value].append(key)
        
        res = []
        for c in reversed(count_list):
            for n in c:
                res.append(n)
                if len(res) == k:
                    return res
                