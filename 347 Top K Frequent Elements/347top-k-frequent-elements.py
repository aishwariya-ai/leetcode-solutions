class Solution(object):
    def topKFrequent(self, nums, k):
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        bucket=[[] for i in range(len(nums)+1)]
        for num,count in freq.items():
            bucket[count].append(num)
        result=[]
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                result.append(n)
                if len(result)==k:
                    return result
        