#!/usr/bin/env python3


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(None)
        cur = ans
        over = 0
        # NOTE: leetcode did not have a testcase for different
        # length ListNode case
        while(l1 is not None or l2 is not None or over > 0):
            l1val, l2val = 0, 0
            if l1 is None:
                l1val = 0
            else:
                l1val = l1.val
                l1 = l1.next

            if l2 is None:
                l2val = 0
            else:
                l2val = l2.val
                l2 = l2.next

            sum = l1val + l2val + over
            if (sum - 9 > 0):
                over = 1
                sum -= 10
            else:
                over = 0

            cur.next = ListNode(sum)
            cur = cur.next

        return ans.next


class ListNode(object):
    ''' Definition for singly-linked list. '''

    def __init__(self, x):
        self.val = x
        self.next = None

if __name__ == '__main__':
    x1 = ListNode(2)
    x2 = ListNode(4)
    x3 = ListNode(3)

    y1 = ListNode(5)
    y2 = ListNode(6)
    y3 = ListNode(4)

    x1.next = x2
    x2.next = x3

    y1.next = y2
    y2.next = y3

    s = Solution()
    ans = s.addTwoNumbers(x1, y1)
    buffer = ''
    while(ans is not None):
        buffer += str(ans.val)
        ans = ans.next
    print(buffer)
