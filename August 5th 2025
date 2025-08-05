from collections import defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])
        total_words = len(words)
        total_length = word_length * total_words
        word_count = defaultdict(int)

        for word in words:
            word_count[word] += 1

        result = []

        for i in range(word_length):
            left = i
            count = 0
            sub_count = defaultdict(int)

            for j in range(i, len(s) - word_length + 1, word_length):
                sub_word = s[j:j + word_length]

                if sub_word in word_count:
                    sub_count[sub_word] += 1
                    count += 1

                    while sub_count[sub_word] > word_count[sub_word]:
                        left_word = s[left:left + word_length]
                        sub_count[left_word] -= 1
                        left += word_length
                        count -= 1

                    if count == total_words:
                        result.append(left)

                else:
                    # Reset everything
                    sub_count.clear()
                    count = 0
                    left = j + word_length

        return result
