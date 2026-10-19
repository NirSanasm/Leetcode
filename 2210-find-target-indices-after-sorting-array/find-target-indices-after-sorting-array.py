class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:

        nums.sort()

        l, r = 0, len(nums) - 1

        res = []

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:

                j = mid - 1
                while j >= 0 and nums[j] == target:
                    res.append(j)
                    j -= 1

                res.append(mid)

                k = mid + 1
                while k < len(nums) and nums[k] == target:
                    res.append(k)
                    k += 1


                res.sort()
                return res

            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return []
                
        