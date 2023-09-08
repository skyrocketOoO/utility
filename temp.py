class Solution:
    def countInterestingSubarrays(self, nums, modulo: int, k: int) -> int:
        can = set()
        
        for num in nums:
            if num % modulo == k:
                can.add(num)

        res = 0
        n = len(nums)
        for l in range(n):
            for r in range(l+1, n+1):
                sub = nums[l: r]
                c = 0
                for num in sub:
                    if num in can:
                        c += 1

                if c % modulo == k:
                    res += 1
        return res


s = Solution()
nums = [3,1,9,6]
modulo = 3
k = 0
print(s.countInterestingSubarrays(nums, modulo, k))