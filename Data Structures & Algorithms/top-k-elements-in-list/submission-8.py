class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        count_list = [[] for _ in range(len(nums) + 1)]
        
        # count the number of items
        for n in nums:
            hash_map[n] = 1 + hash_map.get(n, 0)    

        for key, value in hash_map.items():
            count_list[value].append(key)

        res = []
        for c in reversed(count_list):
            for n in c:
                res.append(n)
                if len(res) == k:
                    return res

