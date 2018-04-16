#!/usr/bin/env python3
# https://leetcode.com/problems/regular-expression-matching


class Solution(object):
    def __init__(self):
        self.cache = {}

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # break pattern into parts
        plist = []
        for c in p:
            if c == '*':
                plist[-1] = plist[-1] + c
            else:
                plist.append(c)

        # reduction of pattern
        # a*.* => .*
        # .*a* => .*
        # a*a* => a*
        i = 1
        while i < len(plist):
            updated = False
            if plist[i].endswith('*') and plist[i-1].endswith('*'):
                if plist[i] == plist[i-1]:
                    del plist[i]
                elif plist[i] == '.*':
                    del plist[i-1]
                elif plist[i-1] == '.*':
                    del plist[i]

            if not updated:
                i += 1

        return self.match(plist, 0, s, 0)


    def match(self, p, p_i , s, s_i):
        if (p_i, s_i) in self.cache:
            return False # self.cache[(p_i, s_i)]
        if p_i == len(p) and s_i == len(s):
            return True
        elif s_i == len(s):
            for i in range(p_i, len(p)):
                if not p[i].endswith('*'):
                    return False
            return True
        elif p_i == len(p):
            return False

        if p[p_i] in (s[s_i], '.'):
            # definitely match one digit
            self.cache[(p_i, s_i)] = self.match(p, p_i+1, s, s_i+1)
            return self.cache[(p_i, s_i)]
        elif p[p_i] in (s[s_i]+'*', '.*'):
            # for this case, we can: 
            # * match and next pattern
            # * match and continue pattern
            # * don't match
            self.cache[(p_i, s_i)] = self.match(p, p_i+1, s, s_i+1) or \
                self.match(p, p_i, s, s_i+1) or \
                self.match(p, p_i+1, s, s_i)
            return self.cache[(p_i, s_i)]
        elif p[p_i].endswith('*'):
            # continue matching because `*` is optional
            self.cache[(p_i, s_i)] = self.match(p, p_i+1, s, s_i)
            return self.cache[(p_i, s_i)]
        else:
            # different
            self.cache[(p_i, s_i)] = False
            return self.cache[(p_i, s_i)]

def printTest(s, p, ans):
    out = Solution().isMatch(s, p)

    if ans == out:
        print("Test passed for %s and %s: output - %s, expected - %s" % (s, p, out, ans))
    else:
        print("Test failed for %s and %s: output - %s, expected - %s" % (s, p, out, ans))


if __name__ == '__main__':
    s = Solution()

    printTest('a', 'a', True)  # simple win
    printTest('a', '', False)  # simple loss
    printTest('a', 'b', False)  # simple loss
    printTest('a', '.', True)  # introduce `.`
    printTest('a', '..', False)  # simple loss with `.`
    printTest('a', '.*', True)  # introduce `*`
    printTest('a', 'a*', True)  # introduce `*`
    printTest('aaa', '.*', True)  # `*` to match multiple character
    printTest('abb', 'c*ab*', True)  # `*` to skip matching when not necessary
    printTest('abb', 'a*c*ab*', True)  # `*` to skip matching when not necessary
    printTest('a', 'ab*', True)  # edge case
    printTest('abc', '.*a*', True)  # ensure reduction works
