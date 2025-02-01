# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
#
# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.
#
#
#
# Example 1:
#
# Input: nums = [1]
#
# Output: true
#
# Explanation:
#
# There is only one element. So the answer is true.
#
# Example 2:
#
# Input: nums = [2,1,4]
#
# Output: true
#
# Explanation:
#
# There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.
#
# Example 3:
#
# Input: nums = [4,3,1,6]
#
# Output: false
#
# Explanation:
#
# nums[1] and nums[2] are both odd. So the answer is false.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
#

class Solution:
    def is_array_special(self, nums: [int]) -> bool:
        nums_len = len(nums)
        if nums_len == 1:
            return True
        for index, num in enumerate(nums):
            if index >= 1:
                if num % 2 == nums[index - 1] % 2:
                    return False
        nums.reverse()
        for index, num in enumerate(nums):
            if index >= 1:
                if num % 2 == nums[index - 1] % 2:
                    return False
        return True


def test_passed(passed: bool) -> str:
    print("Passed") if passed else print("Failed")


solution = Solution()
test_passed(solution.is_array_special([1]) == True)
test_passed(solution.is_array_special([1,2]) == True)
test_passed(solution.is_array_special([1,5]) == False)
test_passed(solution.is_array_special([2,10]) == False)
test_passed(solution.is_array_special([2,1,4]) == True)
test_passed(solution.is_array_special([4,3,1,6]) == False)