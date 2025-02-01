# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
#
# Return the merged string.
#
#
#
# Example 1:
#
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
#
# Example 2:
#
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s
#
# Example 3:
#
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d
#
#
#
# Constraints:
#
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

import itertools
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        interlaced_tuples = itertools.zip_longest(word1, word2)
        for it in interlaced_tuples:
            val1, val2 = it
            if val1 and val2:
                output += val1+val2
            elif val1:
                output += val1
            elif val2:
                output += val2
        return output


def test_output(passed: bool):
    if passed:
        print("Passed")
    else:
        print("Failed")


solution = Solution()
test_output(solution.mergeAlternately('abc', 'pqr') == 'apbqcr')
test_output(solution.mergeAlternately('ab', 'pqrs') == 'apbqrs')
test_output(solution.mergeAlternately('abcd', 'pq') == 'apbqcd')
