class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = collections.defaultdict(int)
        for n in nums:
            counts[n] += 1
    
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        output = []
        for bucket in range(len(buckets)-1, 0, -1):
            for num in buckets[bucket]:
                output.append(num)
                if len(output) == k:
                    return output
        
