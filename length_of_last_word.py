class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split(' ')
        idx = -1
        while(len(a[idx]) == 0):
            idx -= 1
        return len(a[idx])

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World"))
