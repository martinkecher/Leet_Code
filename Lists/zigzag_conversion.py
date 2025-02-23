class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1: return s
        tmp_rows = {}
        i = 0
        for j in range(numRows):
            tmp_rows[j] = ''
        inc_dec = True # True when counter increases, False when counter decreases
        for ch in s:
            # print(i)
            tmp_rows[i] += ch
            if inc_dec and i < numRows-1:
                i += 1
            elif inc_dec and i == numRows-1:
                inc_dec = False
                i -= 1
            elif not inc_dec and i > 0:
                i -= 1
            elif not inc_dec and i == 0:
                inc_dec = True
                i += 1
        # print(tmp_rows)
        res = ''
        for j in range(numRows):
            res += tmp_rows[j]
        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 4))
