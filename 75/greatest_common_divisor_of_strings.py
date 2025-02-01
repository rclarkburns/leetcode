# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
#
#
#
# Example 1:
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
#
# Example 2:
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
#
# Example 3:
#
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#
import itertools

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return ''
        if str1[0] != str2[0] or str1[-1] != str2[-1]:
            return ''
        shortest_str_len = len(min(str1, str2))
        if str1[0:shortest_str_len] != str2[0:shortest_str_len]:
            return ''

        intersection_list_1 = [char for char in str1 if char not in str2]
        intersection_list_2 = [char for char in str2 if char not in str1]
        if intersection_list_1 or intersection_list_2:
            return ''

        output = ''
        zip_tuples = itertools.zip_longest(str1, str2, fillvalue=None)

        for zip_tuple in zip_tuples:
            val1, val2 = zip_tuple
            if val1 == val2:
                output += val1
            elif not val1 and val2 and val2 not in output:
                output = ''
            elif not val2 and val1 and val1 not in output:
                output = ''
            else:
                break

        if not output:
            return output

        repeating_start = (output+output).find(output, 1, -1)
        if repeating_start > 0:
            output = output[0:repeating_start]
        str1_count = str1.count(output)
        str2_count = str2.count(output)
        # Filter out strings that don't contain the repeating pattern
        if len(str1_count * output) < len(str1) or len(str2_count * output) < len(str2):
            return ''
        a = str1_count
        b = str2_count
        while b:
            a, b = b, a % b
        if a > 0:
            output = output * a
        else:
            return ''

        return output

        # Optimized solution
        # if str1 + str2 != str2 + str1:
        #     return ""
        #
        # size = math.gcd(len(str1), len(str2))
        #
        # return(str1[:size])


def repeatedSubstringPattern(s):
    i = (s+s).find(s, 1, -1)
    string = (s + s)[1:-1]
    return string.find(s) != -1

def test_output(passed: bool):
    if passed:
        print("Passed")
    else:
        print("Failed")
# repeatedSubstringPattern("TAUXXTAUXXTAUXXTAUXXTAUXX")

solution = Solution()
test_output(solution.gcdOfStrings('ABCABC', 'ABC') == 'ABC')
test_output(solution.gcdOfStrings('ABABAB', 'ABAB') == 'AB')
test_output(solution.gcdOfStrings('LEET', 'CODE') == '')
test_output(solution.gcdOfStrings('ABCDEF', 'ABC') == '')
test_output(solution.gcdOfStrings('TAUXXTAUXXTAUXXTAUXXTAUXX', 'TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX') == 'TAUXX')
test_output(solution.gcdOfStrings('ABABABAB', 'ABAB') == 'ABAB')
test_output(solution.gcdOfStrings('AAAAAAAAA', 'AAACCC') == '')
test_output(solution.gcdOfStrings('ABCABCABC', 'ABCAAA') == '')
test_output(solution.gcdOfStrings('AABB', 'AB') == '')
test_output(solution.gcdOfStrings('ABABAB', 'ABA') == '')
test_output(solution.gcdOfStrings('ABCBAC', 'ABC') == '')
test_output(solution.gcdOfStrings('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
                                  'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
            == 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
test_output(solution.gcdOfStrings('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
                                  'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
            == 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
