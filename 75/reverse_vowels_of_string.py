# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
#
#
# Example 1:
#
# Input: s = "IceCreAm"
#
# Output: "AceCreIm"
#
# Explanation:
#
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
#
# Example 2:
#
# Input: s = "leetcode"
#
# Output: "leotcede"
#
#
#
# Constraints:
#
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


class Solution:
    def reverse_vowels(self, s: str) -> str:
        output = ''
        vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
        s_vowels = []
        if len(s) == 1:
            return s

        for char in s:
            if char in vowels:
                s_vowels.append(char)
        s_vowels.reverse()
        for char in s:
            if char in vowels:
                output += s_vowels.pop(0)
            else:
                output += char
        return output




def test_output(passed: bool):
    if passed:
        print("Passed")
    else:
        print("Failed")


solution = Solution()
test_output(solution.reverse_vowels('IceCreAm') == 'AceCreIm')
test_output(solution.reverse_vowels('leetcode') == 'leotcede')
