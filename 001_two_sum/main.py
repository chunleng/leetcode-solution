#!/usr/bin/env python3
# https://leetcode.com/problems/two-sum/


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checked = dict()

        for i in range(len(nums)):
            if (target - nums[i] in checked):
                return [checked[target - nums[i]], i]
            # In case of collision, overwrite
            checked[nums[i]] = i


if __name__ == '__main__':
    s = Solution()

    nums = [-3, 4, 3, 90]
    target = 0
    print(s.twoSum(nums, target))
