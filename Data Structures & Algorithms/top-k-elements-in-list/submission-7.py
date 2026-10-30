class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # writing a solution using heap
        hash_map = {}
        for n in nums:
            hash_map[n] = 1 + hash_map.get(n, 0)

        heap = []
        for n, freq in hash_map.items():
            heapq.heappush(heap, (freq, n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res