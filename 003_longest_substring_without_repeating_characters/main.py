#!/usr/bin/env python


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #return divide_conquer_solution(s)
        return sliding_window_solution(s)


solutions = dict()


def divide_conquer_solution(s):
    if s == '' or len(s) == 1:
        return len(s)

    # return cached answer if available
    if s in solutions:
        return solutions[s]

    # perform duplicate search
    for i in range(len(s)):
        match = s[i]
        for j in range(i + 1, len(s)):
            if match == s[j]:
                ans1 = divide_conquer_solution(s[:j])
                ans2 = divide_conquer_solution(s[i + 1:])

                # return largest of the duplicates
                if ans1 < ans2:
                    solutions[s] = ans2
                    return ans2
                solutions[s] = ans1
                return ans1

    # return as there is no duplicate
    solutions[s] = len(s)
    return len(s)


def sliding_window_solution(s):
    if s == '' or len(s) == 1:
        return len(s)

    i = 0
    maxlength = 1
    letters = dict()
    for j in range(0, len(s)):
        if s[j] in letters:
            i = max(letters[s[j]] + 1, i)

        maxlength = max(j - i + 1, maxlength)
        letters[s[j]] = j

    return maxlength


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(''))           # returns 0
    print(s.lengthOfLongestSubstring('a'))          # returns 1
    print(s.lengthOfLongestSubstring('aba'))        # returns 2
    print(s.lengthOfLongestSubstring('abcadefg'))   # returns 7
    print(s.lengthOfLongestSubstring('abcabefg'))   # returns 6
    print(s.lengthOfLongestSubstring('dcabcebade'))  # returns 5
    print(s.lengthOfLongestSubstring('abcabcbb'))  # returns 3
    print(s.lengthOfLongestSubstring(
        'zbexrampetvhqnddjeqvuygpnkazqfrpjvoaxdpcwmjobmskskfojnewxgxnnofwltwjwnnvbwjckdmeouuzhyvhg'))  # returns 13
