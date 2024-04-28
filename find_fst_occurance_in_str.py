class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)



if __name__ == '__main__':
    sol = Solution()
    print(sol.strStr("sadbutsad", "uuy"))
