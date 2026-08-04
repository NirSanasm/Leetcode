class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        nums.sort()

        k =0 
        res = []
        for i in range(nums[0], nums[-1]):

            if i != nums[k]:
                res.append(i)
            else:
                k += 1

        return res

