#!/usr/bin/env python
# https://leetcode.com/problems/median-of-two-sorted-arrays/
import bisect


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # Handle all none case
        if ((nums1 is None or len(nums1) == 0)
                and (nums2 is None or len(nums2) == 0)):
            return None

        # Handle single none case (Get median of the non-none)
        if nums1 is None or len(nums1) == 0:
            return self.oneArrayMedian(nums2)
        if nums2 is None or len(nums2) == 0:
            return self.oneArrayMedian(nums1)

        return self.twoArrayMedian(nums1, nums2)

    def oneArrayMedian(self, nums):
        arrlength = len(nums)
        index = arrlength / 2
        if arrlength % 2 == 0:
            return (nums[index] + nums[index - 1]) / 2.0
        else:
            return nums[index]

    def twoArrayMedian(self, nums1, nums2):
        lenNums1 = len(nums1)
        lenNums2 = len(nums2)

        if (lenNums1 >= lenNums2):
            return self.twoArrayMedianSearcher(
                nums1, lenNums1, 0, lenNums1, nums2, lenNums2, 0, lenNums2)
        else:
            return self.twoArrayMedianSearcher(
                nums2, lenNums2, 0, lenNums2, nums1, lenNums1, 0, lenNums1)

    def twoArrayMedianSearcher(self, x, lenFullX, startX, endX, y, lenFullY, startY, endY):
        # twoArrayMedianSearcher() execute in the following steps
        # 1.  Try to search the middle position of the longer array (i.e. x) and
        #     fit into the left of the shorter array (i.e. y), such that the sort
        #     can be maintained
        # 2.  The sum of the middle position (i.e. mid_pos) and the fitted
        #     position (i.e. fit_pos) will give you the middle number's actual
        #     sorted position in relative to both array
        # 3a. If the summed position (i.e. sum_pos = mid_pos + fit_pos) is in the
        #     middle position of both array, you get the median
        #     In the case of 2 median (even length arrays), the next variable
        #     should be x[mid_pos-1] or y[fit_pos-1] whichever is smaller
        # 3b. If the summed position is greater than the middle position, the
        #     median would be in x (lesser than mid_pos) or y (lesser than
        #     fit_pos)
        # 3c. If the summed position is smaller than the middle position, the
        #     median would be in x (greater than mid_pos) or y (greater than
        #     fit_pos)
        # 4.  Repeat until the median is obtained

        mid_pos = (startX + endX) / 2
        fit_pos = bisect.bisect_left(y, x[mid_pos], startY, endY)
        median_pos = (lenFullX + lenFullY) / 2
        if mid_pos + fit_pos == median_pos:
            if (lenFullX + lenFullY) % 2 == 0:
                median2 = None

                if mid_pos > 0 and fit_pos > 0:
                    median2 = max(x[mid_pos - 1], y[fit_pos - 1])
                elif mid_pos > 0:
                    median2 = x[mid_pos - 1]
                else:
                    median2 = y[fit_pos - 1]
                return (median2 + x[mid_pos]) / 2.0

            return x[mid_pos]
        else:
            if mid_pos + fit_pos < median_pos:
                startX = mid_pos + 1
                startY = fit_pos
            else:
                endX = mid_pos
                endY = fit_pos

        if endX - startX >= endY - startY:
            return self.twoArrayMedianSearcher(
                x, lenFullX, startX, endX, y, lenFullY, startY, endY)
        else:
            return self.twoArrayMedianSearcher(
                y, lenFullY, startY, endY, x, lenFullX, startX, endX)


def execute(nums1, nums2, expectedMedian):
    result = s.findMedianSortedArrays(nums1, nums2)

    if result == expectedMedian or result is expectedMedian:
        print(' * Matches expected median of ' + str(expectedMedian))
    else:
        print(' * Result: ' + str(result) +
              '\tExpected: ' + str(expectedMedian))

if __name__ == '__main__':
    s = Solution()

    print('[Case] Handle length 0 cases')
    execute([], [], None)
    execute([], [1, 2], 1.5)

    print('[Case] Middle case is the answer')
    execute([1], [2, 3], 2)
    execute([1, 2, 4], [1, 2], 2)
    execute([1, 2, 4], [1, 1, 4], 1.5)

    print('[Case] First case is skewed left')
    execute([1, 2], [1, 2], 1.5)

    print('[Case] Balanced case')
    execute([1, 2], [3, 4, 5], 3)
