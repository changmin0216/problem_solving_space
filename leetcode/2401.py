class Solution(object):
    def longestNiceSubarray(self, nums):
        ans = j = mask = 0
        for i, x in enumerate(nums):
            while mask & x: # 나는 and 연산한 값이 0인 얘들을 원한다.
                mask ^= nums[j]
                j += 1
            ans = max(ans, i - j + 1)
            mask |= x
        return ans

nums = [135745088,609245787,16,2048,2097152]
solution = Solution()
answer = solution.longestNiceSubarray(nums)
print(answer)