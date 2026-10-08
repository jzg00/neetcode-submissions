class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # use a hashmap to count the frequency of each number
        counts = collections.defaultdict(int)
        for num in nums:
            counts[num] += 1

        # create an array of arrays: each buckets index represents frequency
        # a number's frequency can be at most the length of the nums array
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)   # store numbers in their respective frequency bucket

        # iterate through the buckets array in reverse and add the most frequent numbers
        output = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
            
