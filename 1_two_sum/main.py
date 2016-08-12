#!/usr/bin/env python3
# https://leetcode.com/problems/two-sum/


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # remove values out of range
        possible_min = min(nums) - target
        possible_max = max(nums) - target
        possible = [i for i in nums if (
            i <= possible_max or i >= possible_min)]
        possible.sort()

        for i in range(len(possible)):
            for j in range(i + 1, len(possible)):
                if (possible[i] + possible[j] == target):
                    index0 = nums.index(possible[i])
                    index1 = len(nums) - nums[::-1].index(possible[j]) - 1
                    return [index0, index1]
                elif (possible[i] + possible[j] > target):
                    break


if __name__ == '__main__':
    s = Solution()

    nums = [-3, 4, 3, 90]
    target = 0
    print(s.twoSum(nums, target))
