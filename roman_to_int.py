
class Solution:
    def romanToInt(self, s: str) -> int:
            rom_to_int = {'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}

            res = 0
            n = len(s)
            for i in range(n-2, -1, -1):
                if rom_to_int[s[i]] >= rom_to_int[s[i+1]]:
                    res += rom_to_int[s[i]]
                else:
                    res -= rom_to_int[s[i]]

            res += rom_to_int[s[n-1]]

            return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt("LVIII"))
