s = "abcd"
t = "cdab"


def test(s, t):
    for i in range(len(s)):
        if  s[i:] + s[:i]== t:
            return i

class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        offsets = self.offset(s, t)
        n = len(s)
        self.ans = 0
        self.bk(0, offsets, n, 0, k)
        print(self.ans)
    

    def bk(self, cur, offset, n, step, k):
        if step == k:
            if cur % n in offset:
                self.ans = (self.ans + 1) % 1000000007
            return
        for i in range(1, n):
            self.bk(cur + i, offset, n, step+1, k)


    def offset(self, s, t):
        ofs = set()
        for i in range(0, len(s)):
            if s[i:] + s[:i]== t:
                ofs.add(i)
        print(ofs)
        return ofs

so = Solution()
s = "abcde"
t = "cdeab"
for k in range(1, 10):
    so.numberOfWays(s, t, k)