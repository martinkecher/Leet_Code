class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for ch in s:
            if ch not in t[idx:]:
                return False
            else:
                idx = t.find(ch, idx) + 1
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isSubsequence("l: Panama", "A man, a plan, a canal: Panama"))
