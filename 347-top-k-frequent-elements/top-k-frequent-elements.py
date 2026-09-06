class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashset = {}
        
        for num in nums:
            if hashset.get(num, None):
                hashset[num] = hashset[num] + 1
            else:
                hashset[num] = 1

        
        new_list = [k for k, v in sorted(hashset.items(), reverse = True, key=lambda item: item[1])]

        return new_list[:k]



        