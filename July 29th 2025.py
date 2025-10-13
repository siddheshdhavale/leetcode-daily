class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0    # line is var for the current line, and length is var for curr line length
        i = 0   # looping through entire input of array of words

        while i < len(words):
            # Case 1: curr line is complete
            if length + len(line) + len(words[i]) > maxWidth:    # len(line) is no. of spaces:
                # distributing extra space evenly:
                extra_space = maxWidth - length

                spaces = extra_space // max(1, len(line) - 1)
                remainder = extra_space % max(1, len(line) - 1)    # mod to get remainder

                # edge case: just a single word: "apple" -> using max as below
                # add spaces to cur line
                for j in range(max(1, len(line) - 1)):
                    line[j] += " " * spaces  # adding as many spaces as the number
                    if remainder:   # if remainder is non-zero
                        line[j] += " "
                        remainder -= 1# Decrement remainder by 1

                res.append("".join(line))
                line, length = [], 0    # resetting line & length

            # Case 2: curr line is not complete
                # adding curr word to our curr line, and update len of cur line instead of adding to our res
            line.append(words[i])
            length += len(words[i])
            i += 1  # incrementing our i ptr to get to the next word.

        # Handling the last line:
        last_line = " ".join(line)  # this will not adda trailing space
        trail_space = maxWidth - len(last_line)

        res.append(last_line + " " * trail_space)
        return res
