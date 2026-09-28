class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        pref = []
        suff = []

        length = len(nums)

        prev = 1
        for i in range(len(nums)):
            
            pref.append(prev)
            val = nums[i] * prev
            prev = val

        prev = 1

        nums.reverse()
        for i in range(len(nums)):
           
            suff.append(prev)
            val = nums[i] * prev
            prev = val

        res = []

        print(len(pref), len(suff))

        suff.reverse()

        for i in range(len(nums)):

            print(i, pref[i], suff[i])

            val = pref[i] * suff[i]
            res.append(val)

        return res