#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 13:00
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : test_nextPermutation.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = test_nextPermutation
    __author__ = yeyuc
    __time__ = 2019/12/9 13:00
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
from .NextPermutation import Solution


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
        self.input = [[1, 2, 3], [3, 2, 1], [1, 1, 5], [1, 3, 2], [2, 3, 1], [2, 3, 1, 1], [1, 5, 8, 4, 7, 6, 5, 3, 1]]
        self.assert_result = [[1, 3, 2], [1, 2, 3], [1, 5, 1], [2, 1, 3], [3, 1, 2], [3, 1, 1, 2], [1, 5, 8, 5, 1, 3, 4, 6, 7]]

    def test_lengthOfLongestSubstring(self):
        s = Solution()
        for i in range(len(self.assert_result)):
            result = s.nextPermutation(nums=self.input[i])
            self.assertEqual(self.assert_result[i], result)


@fn_timer
def main():
    unittest.main()


if __name__ == '__main__':
    main()
