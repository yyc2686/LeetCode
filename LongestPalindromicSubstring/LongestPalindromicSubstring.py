#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 19:41
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : LongestPalindromicSubstring.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = LongestPalindromicSubstring
    __author__ = yeyuc
    __time__ = 2019/12/1 19:41
    Code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃        ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import time
from functools import wraps
import numpy as np


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        cost_time = t1 - t0
        if cost_time <= 1:
            cost_time *= 10000
            print("本次运行耗时：{0}秒 ".format(str(cost_time)))
        elif cost_time <= 60:
            print("本次运行耗时：{0}秒 ".format(str(cost_time)))
        else:
            print('本次运行耗时：{0}时{1}分{2}秒 '.format(int(cost_time / 3600), int((cost_time / 60) % 60), int(cost_time % 60)))
        return result

    return function_timer


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 使用动态规划思想，穷举所有的可能情况
        """
        根据回文的特性，一个大回文按比例缩小后的字符串也必定是回文，比如ABCCBA，那BCCB肯定也是回文。
        所以我们可以根据动态规划的两个特点：
            （1）把大问题拆解为小问题
            （2）重复利用之前的计算结果
        这道题。如何划分小问题，我们可以先把所有长度最短为1的子字符串计算出来，根据起始位置从左向右，这些必定是回文。
        然后计算所有长度为2的子字符串，再根据起始位置从左向右。
        到长度为3的时候，我们就可以利用上次的计算结果：如果中心对称的短字符串不是回文，那长字符串也不是，如果短字符串是回文，那就要看长字符串两头是否一样。
        这样，一直到长度最大的子字符串，我们就把整个字符串集穷举完了。
        """
        n = len(s)
        max_Palindrome = ""
        max_length = 0

        f = [[0 for i in range(n)] for j in range(n)]
        # f = np.zeros((n, n))

        for j in range(n):
            for i in range(j + 1):
                if j - i <= 1:
                    if s[i] == s[j]:
                        f[i][j] = 1
                else:
                    if s[i] == s[j] and f[i + 1][j - 1]:
                        f[i][j] = 1
                if f[i][j]:
                    if max_length < j - i + 1:
                        max_length = j - i + 1
                        max_Palindrome = s[i:j + 1]
        return max_Palindrome

    def longestPalindrome2(self, s: str) -> str:
        # 回文数定义，与逆序字符串比较，找最大公共子串串
        s_r = s[::-1]
        for i in range(len(s)):
            if s[i] == s_r[i]:
                s[i] == "_*_"
        s = s.split("_*_")

        if not s:
            return s

        def is_palindrome(s):
            return s == s[::-1]

        palindrome = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if is_palindrome(s[i:j + 1]) and j + 1 - i > len(palindrome):
                    palindrome = s[i:j + 1]
        return palindrome

    def longestPalindrome1(self, s: str) -> str:
        # 穷举法，运行超时
        if not s:
            return s

        def is_palindrome(s):
            return s == s[::-1]

        palindrome = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if is_palindrome(s[i:j + 1]) and j + 1 - i > len(palindrome):
                    palindrome = s[i:j + 1]
        return palindrome


@fn_timer
def main():
    s = ["babad", "cbbd", "abcda"]
    class_client = Solution()
    # len = class_client.longestPalindrome(s=s[-1])
    len = class_client.longestPalindrome(s=s[0])
    len


if __name__ == '__main__':
    main()
