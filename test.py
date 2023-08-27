class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        # we can take sum of first target/2 values
        x = min(n, target >> 1)
        n -= x
        res = x * (x + 1) >> 1
        print(res)
        # then add the residual
        print(n * (target * 2 + n - 1) >> 1)
        res += n * (target * 2 + n - 1) >> 1
        return res
    

s = Solution()
print(s.minimumPossibleSum(2, 11))