"""
97. Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

http://www.tangjikai.com/algorithms/leetcode-97-interleaving-string

"""


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        p = len(s3)

        if m + n != p:
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True

                elif i == 0:
                    dp[i][j] = s2[:j] == s3[:j]
                elif j == 0:
                    dp[i][j] = s1[:i] == s3[:i]

                else:
                    dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
                               (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"

    s3 = "aadbbcbcac"
    print Solution().isInterleave(s1, s2, s3)  # return true.

    s3 = "aadbbbaccc"
    print Solution().isInterleave(s1, s2, s3)  # return false.
