# Given an input string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
#
# Return a string of the words in reverse order concatenated by a single space.
#
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
#
#
#
# Example 1:
#
# Input: s = "the sky is blue"
# Output: "blue is sky the"
#
# Example 2:
#
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
#
# Example 3:
#
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
#
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# There is at least one word in s.
#
#
#
# Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

class Solution:
    def reverse_words(self, s: str) -> str:
        output = ''
        word_list = []
        word = ''
        for index, char in enumerate(s):
            if char.isspace():
                if word:
                    word_list.append(word)
                    word = ''
                else:
                    continue
            else:
                word += char
            if index == len(s) - 1 and word:
                word_list.append(word)
        word_list.reverse()
        for index, word in enumerate(word_list):
            if index == len(word_list) - 1:
                output += word
            else:
                output += f"{word} "
        return output
        # Optimized solution
        # words = s.split()  # Split the string into words
        # words.reverse()    # Reverse the list of words
        # return " ".join(words)





def test_output(passed: bool) -> str:
    if passed:
        print("Passed")
    else:
        print("Failed")


solution = Solution()
test_output(solution.reverse_words("the sky is blue") == "blue is sky the")
test_output(solution.reverse_words("  hello world  ") == "world hello")
test_output(solution.reverse_words("a good   example") == "example good a")
