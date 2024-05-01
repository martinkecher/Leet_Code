from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        current_line_list = []
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + len(current_line_list) <= maxWidth:
                current_line = current_line + word
                current_line_list.append(word)

            else:
                spaces = maxWidth - len(current_line) # the last is the munber of spaces in current_line


                if len(current_line_list) > 1:
                    #####################################
                    idx = 0
                    sp = []
                    for _ in range(len(current_line_list)-1):
                        sp.append("")
                    for _ in range(spaces):
                        sp[idx] += " "
                        idx = 0 if idx == (len(current_line_list) - 2) else idx + 1
                    l = ""
                    for idx in range(len(sp)):
                        l += current_line_list[idx] + sp[idx]
                    l += current_line_list[-1]
                    lines.append(l)
                    #####################################
                    # space_between_words = spaces / (len(current_line_list) - 1)
                    # sps = " " * int(space_between_words)
                    # if space_between_words % 1 != 0:
                    #     current_line_list[0] = current_line_list[0] + " "
                    # lines.append(sps.join(current_line_list))


                else:
                    sps = " " * (maxWidth - len(current_line) -(len(current_line_list)-1))
                    lines.append("".join(current_line_list) + sps)

                current_line = word
                current_line_list = [word]


        #########################################
        spaces = maxWidth - len(current_line) - len(current_line_list)+1 # the last is the munber of spaces in current_line
        sps = " " * (spaces)
        # lines.append(current_line + sps)
        lines.append(" ".join(current_line_list) + sps)
        return lines


if __name__ == '__main__':
    sol = Solution()
    str_lst = ["Science","is","what","we","understand","well","enough","to","explain","to",
                           "a","computer.","Art","is","everything","else","we","do"]
    # str_lst = ["example", "of", "text", "justification."]
    # str_lst = ["What","must","be","acknowledgment","shall","be"]
    print(sol.fullJustify(str_lst, 20))
