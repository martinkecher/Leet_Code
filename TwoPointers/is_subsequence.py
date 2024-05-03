class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for ch in s:
                idx = t.find(ch, idx) + 1
                if idx == 0:
                    return False

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isSubsequence("l: Panama", "A man, a plan, a canal: Panama"))
