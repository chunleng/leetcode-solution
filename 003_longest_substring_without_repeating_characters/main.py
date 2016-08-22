#!/usr/bin/env python3


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return naive_recursive_solution(s)


solutions = dict()


def naive_recursive_solution(s):
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
                ans1 = naive_recursive_solution(s[:j])
                ans2 = naive_recursive_solution(s[i + 1:])

                # return largest of the duplicates
                if ans1 < ans2:
                    solutions[s] = ans2
                    return ans2
                solutions[s] = ans1
                return ans1

    # return as there is no duplicate
    solutions[s] = len(s)
    return len(s)

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring(''))           # prints ''
    print(s.lengthOfLongestSubstring('a'))          # prints 'a'
    print(s.lengthOfLongestSubstring('aba'))        # prints 'ab'
    print(s.lengthOfLongestSubstring('abcadefg'))   # prints 'bcadefg'
    print(s.lengthOfLongestSubstring('abcabefg'))   # prints 'cadefg'
    print(s.lengthOfLongestSubstring('dcabcebade'))  # prints 'abceb'
    print(s.lengthOfLongestSubstring(
        'zbexrampetvhqnddjeqvuygpnkazqfrpjvoaxdpcwmjobmskskfojnewxgxnnofwltwjwnnvbwjckdmeouuzhyvhg'))
