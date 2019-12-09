#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 15:15
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : test_two_sum.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = test_lengthOfLongestSubstring
    __author__ = yeyuc
    __time__ = 2019/11/21 15:15
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
import unittest
from .LongestSubstringWithoutRepeatingCharacters import Solution


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


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.string = ["abcabcbb", "bbbbb", "pwwkew", "aab", "dvdf", "cdd", "", " "]
        self.assert_result = [3, 1, 3, 2, 3, 2, 0, 1]

    def test_lengthOfLongestSubstring(self):
        s = Solution()
        for i in range(len(self.assert_result)):
            result = s.lengthOfLongestSubstring(s=self.string[i])
            self.assertEqual(result, self.assert_result[i])

    def test_lengthOfLongestSubstring1(self):
        s = Solution()
        for i in range(len(self.assert_result)):
            result = s.lengthOfLongestSubstring1(s=self.string[i])
            self.assertEqual(result, self.assert_result[i])


@fn_timer
def main():
    unittest.main()


if __name__ == '__main__':
    main()
