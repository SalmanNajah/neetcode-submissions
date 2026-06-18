class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num ,0) + 1
        pairs = list(freq.items())
        s = sorted(pairs, key=lambda x: x[1], reverse=True)
        result = []
        for i in s[:k]:
            result.append(i[0])
        return result 
