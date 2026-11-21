class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:

        result = []

        mapp = {}

        for num in nums:

            res = mapp.get(num, 0)

            if res == 0:
                mapp[num] = 1

            else:
                mapp[num] = 2
                result.append(num)

        for i in range(1, len(nums)+1):

            if i not in mapp:

                result.append(i)

        return result

            





        