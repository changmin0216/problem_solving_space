from itertools import combinations
class Solution(object):
    def twoSum(self, nums, target):
        # l = []
        # for i, x in enumerate(nums):
        #     l.append((i, x))
        # for k in combinations(l, 2):
        #     if k[0][1] + k[1][1] == target:
        #         return [k[0][0], k[1][0]]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))