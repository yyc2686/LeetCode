#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 15:32
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : LongestSubstringWithoutRepeatingCharacters.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = LongestSubstringWithoutRepeatingCharacters
    __author__ = yeyuc
    __time__ = 2019/11/25 15:32
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
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len

    def lengthOfLongestSubstring1(self, s: str) -> int:
        if not s: return 0
        max_length = 0
        l = []
        for i in s:
            if i not in l:
                l.append(i)
            else:
                max_length = max(max_length, len(l))
                l.append(i)
                index = l.index(i)
                l = l[index + 1:]
        max_length = max(max_length, len(l))
        return max_length


@fn_timer
def main():
    s = ["abcabcbb", "bbbbb", "pwwkew", "aab", "dvdf", "cdd", " "]
    class_client = Solution()
    len = class_client.lengthOfLongestSubstring1(s=s[-1])
    len


if __name__ == '__main__':
    main()
