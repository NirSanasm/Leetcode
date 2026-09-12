class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
       
        left_sum = 0
        right_sum = sum(nums)

        for num in range(len(nums)):
            
            if num == 0:
                left_sum = 0
            else:
                left_sum = left_sum + nums[num-1]

            right_sum = right_sum - nums[num]
           
            if left_sum == right_sum:
         
                return num
        return -1

        
        