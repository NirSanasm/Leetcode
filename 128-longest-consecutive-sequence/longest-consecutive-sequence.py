class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        if not nums:
            return 0

        num_set = set(nums)
        length = 0
        max_len = 1
        for n in num_set:
            if n - 1 not in num_set:
               
               
                length = 1
                j = n + 1
                
               
                while j in num_set:
                    length += 1
                    j += 1
                        

                max_len = max(max_len, length) 
                

        return max_len
        