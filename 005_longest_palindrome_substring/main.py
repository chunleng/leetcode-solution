#!/usr/bin/env python
# https://leetcode.com/problems/longest-palindromic-substring/


class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.longestPalindrome_by_manacher_algo(s)

    def longestPalindrome_by_manacher_algo(self, s):
        # Basic concept of this algorithm:
        # 1. After counting the left side of the symmetry, it's pointless to
        #    count the right side again
        # 2. Right side can further expand, so
        #    DON'T stop expanding after getting the values from left side of
        #    the symmetry
        #    DO    continue expand and possibly replace the centre pivot
        n = len(s) * 2 + 1
        l = [0] * n
        l[0] = 0
        l[1] = 1
        ans = 1
        centre_pos = 1
        centre_length = 1

        for i in xrange(2, n):
            # Readjust if out of centre
            if i > centre_pos + centre_length:
                centre_pos = i
                centre_length = 0

            mirror = centre_pos * 2 - i
            l[i] = l[mirror]

            # Try expanding at i
            loop_ceil = min(i, len(phrase) - i - 1)

            for i in xrange(l[i], loop_ceil)

        return s[(ans - l[ans]) / 2:(ans + l[ans]) / 2]

    def longestPalindrome_by_palindrome_around(self, s):
        if s is None or s == '':
            return None

        start = 0
        end = 0
        len_ans = end - start

        for i in xrange(0, len(s)):
            start1, end1 = self.palindrome_around(i, i, s)
            start2, end2 = self.palindrome_around(i, i + 1, s)

            len_can1 = end1 - start1
            len_can2 = end2 - start2

            if len_can1 > len_can2:
                if len_can1 > len_ans:
                    start = start1
                    end = end1
                    len_ans = len_can1
            elif len_can2 > len_ans:
                start = start2
                end = end2
                len_ans = len_can2

        return s[start:end + 1]

    def palindrome_around(self, start, end, phrase):
        if (end >= len(phrase)
                or phrase[start] != phrase[end]):
            return 0, -1

        loop_ceil = min(start, len(phrase) - end - 1)

        for i in xrange(loop_ceil):
            if phrase[start - i - 1] != phrase[end + i + 1]:
                return (start - i, end + i)

        return start - loop_ceil, end + loop_ceil


if __name__ == '__main__':
    s = Solution()
    # s.longestPalindrome('rgczcpratwyqxaszbuwwcadruayhasynuxnakpmsyhxzlnxmdtsqqlmwnbxvmgvllafrpmlfuqpbhjddmhmbcgmlyeypkfpreddyencsdmgxysctpubvgeedhurvizgqxclhpfrvxggrowaynrtuwvvvwnqlowdihtrdzjffrgoeqivnprdnpvfjuhycpfydjcpfcnkpyujljiesmuxhtizzvwhvpqylvcirwqsmpptyhcqybstsfgjadicwzycswwmpluvzqdvnhkcofptqrzgjqtbvbdxylrylinspncrkxclykccbwridpqckstxdjawvziucrswpsfmisqiozworibeycuarcidbljslwbalcemgymnsxfziattdylrulwrybzztoxhevsdnvvljfzzrgcmagshucoalfiuapgzpqgjjgqsmcvtdsvehewrvtkeqwgmatqdpwlayjcxcavjmgpdyklrjcqvxjqbjucfubgmgpkfdxznkhcejscymuildfnuxwmuklntnyycdcscioimenaeohgpbcpogyifcsatfxeslstkjclauqmywacizyapxlgtcchlxkvygzeucwalhvhbwkvbceqajstxzzppcxoanhyfkgwaelsfdeeviqogjpresnoacegfeejyychabkhszcokdxpaqrprwfdahjqkfptwpeykgumyemgkccynxuvbdpjlrbgqtcqulxodurugofuwzudnhgxdrbbxtrvdnlodyhsifvyspejenpdckevzqrexplpcqtwtxlimfrsjumiygqeemhihcxyngsemcolrnlyhqlbqbcestadoxtrdvcgucntjnfavylip')

    if True:
        print(s.longestPalindrome('a'))
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
