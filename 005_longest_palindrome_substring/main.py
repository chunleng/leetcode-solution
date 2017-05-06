#!/usr/bin/env python
# https://leetcode.com/problems/longest-palindromic-substring/

import math

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if s is None or s == '':
            return None

        if len(s) == 1:
            return s

        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        # Init as minimum possible
        ans = s[0]

        add_val = 1
        dir = -1
        curr_ind = len(s)/2 # Get middle
        odd = len(s) % 2 == 1;

        # Loop by going through the variable closer to centre
        for i in xrange(0,len(s)-2):
            max_match = len(s) - 2 * (math.ceil(i / 2.0)) if odd else len(s) - 1 - 2 * (i / 2)
            middle_case = True
            lower_index = curr_ind - 1
            upper_index = curr_ind + 1

            for j in xrange(1, int(math.ceil(max_match/2.0) + 1)):
                if (lower_index >= 0 and upper_index < len(s) and
                    s[lower_index] == s[upper_index]):
                    temp = s[lower_index: upper_index + 1]
                    if (len(temp) > len(ans)):
                        print(j)
                        ans = temp
                    if middle_case:
                        if s[lower_index] != s[lower_index+1]:
                            middle_case = False
                    lower_index -= 1
                    upper_index += 1
                else:
                    if middle_case:
                        if (lower_index >= 0 and
                            s[lower_index] == s[lower_index+1]):
                            if (j * 2 > len(ans)):
                                ans = s[lower_index: upper_index]
                            lower_index -= 1
                        elif (upper_index < len(s) and 
                              s[upper_index-1] == s[upper_index]):
                            if (j * 2 > len(ans)):
                                ans = s[lower_index+1:upper_index+1]
                            upper_index += 1
                        else:
                            middle_case = False
                        continue
                    break

            # Terminate if current loop matches the max possible length
            if len(ans) >= max_match - 1:
                break

            # Pick curr_ind
            curr_ind = curr_ind + (add_val * dir)
            add_val = add_val + 1
            dir = dir * -1


        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('babad'))
    print(s.longestPalindrome('ababad'))
    print(s.longestPalindrome('bb'))
    print(s.longestPalindrome('bbbb'))
    print(s.longestPalindrome('cbbd'))
    print(s.longestPalindrome('cbbbbd'))
    print(s.longestPalindrome('cbbbbbbd'))
    print(s.longestPalindrome('abbcbcda'))
    print(s.longestPalindrome('abdbcbcda'))
    print(s.longestPalindrome('rgczcpratwyqxaszbuwwcadruayhasynuxnakpmsyhxzlnxmdtsqqlmwnbxvmgvllafrpmlfuqpbhjddmhmbcgmlyeypkfpreddyencsdmgxysctpubvgeedhurvizgqxclhpfrvxggrowaynrtuwvvvwnqlowdihtrdzjffrgoeqivnprdnpvfjuhycpfydjcpfcnkpyujljiesmuxhtizzvwhvpqylvcirwqsmpptyhcqybstsfgjadicwzycswwmpluvzqdvnhkcofptqrzgjqtbvbdxylrylinspncrkxclykccbwridpqckstxdjawvziucrswpsfmisqiozworibeycuarcidbljslwbalcemgymnsxfziattdylrulwrybzztoxhevsdnvvljfzzrgcmagshucoalfiuapgzpqgjjgqsmcvtdsvehewrvtkeqwgmatqdpwlayjcxcavjmgpdyklrjcqvxjqbjucfubgmgpkfdxznkhcejscymuildfnuxwmuklntnyycdcscioimenaeohgpbcpogyifcsatfxeslstkjclauqmywacizyapxlgtcchlxkvygzeucwalhvhbwkvbceqajstxzzppcxoanhyfkgwaelsfdeeviqogjpresnoacegfeejyychabkhszcokdxpaqrprwfdahjqkfptwpeykgumyemgkccynxuvbdpjlrbgqtcqulxodurugofuwzudnhgxdrbbxtrvdnlodyhsifvyspejenpdckevzqrexplpcqtwtxlimfrsjumiygqeemhihcxyngsemcolrnlyhqlbqbcestadoxtrdvcgucntjnfavylip'))

