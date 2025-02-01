# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
#
#
#
# Example 1:
#
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
#
# Example 2:
#
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#
#
#
# Constraints:
#
# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length
#

class Solution:
    def can_place_flowers(self, flowerbed: [int], n: int) -> bool:
        plot_attempt = False
        skip_next = False
        flowerbed_len = len(flowerbed)

        if flowerbed_len == 1:
            return n <= 1 if flowerbed[0] == 0 else n == 0

        for index, plot in enumerate(flowerbed):
            if skip_next:
                skip_next = False
            elif plot == 0:
                if plot_attempt:
                    # 3 == flower plot spot
                    flowerbed[index-1] = 3
                    plot_attempt = False
                else:
                    plot_attempt = True
            else:
                skip_next = True
                plot_attempt = False

        # Clean up ends of flowerbed
        if flowerbed_len >= 3:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 3
            if flowerbed[-2] == 0 and flowerbed[-1] == 0:
                flowerbed[-1] = 3

        return flowerbed.count(3) >= n








def test_output(passed: bool):
    if passed:
        print("Passed")
    else:
        print("Failed")

solution = Solution()
test_output(solution.can_place_flowers([1,0,0,0,1], 1) == True)
test_output(solution.can_place_flowers([0,0,1,0,1], 1) == True)
test_output(solution.can_place_flowers([1,0,0,0,1,0,0], 2) == True)
test_output(solution.can_place_flowers([1,0,0,0,0,1], 2) == False)
test_output(solution.can_place_flowers([1,0,1,0,1,0,1], 1) == False)
test_output(solution.can_place_flowers([1,0,0,0,0,0,0,0,0], 3) == True)
test_output(solution.can_place_flowers([1,0,0,0,1], 2) == False)
test_output(solution.can_place_flowers([1,0,0,0], 1) == True)
test_output(solution.can_place_flowers([1,0,0,0,0], 2) == True)
test_output(solution.can_place_flowers([0,0], 1) == True)
test_output(solution.can_place_flowers([0], 1) == True)
test_output(solution.can_place_flowers([1], 0) == True)
test_output(solution.can_place_flowers([1,0,0], 1) == True)
test_output(solution.can_place_flowers([0], 0) == True)

