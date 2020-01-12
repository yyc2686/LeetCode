#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 9:54
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : test_binarySearch.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = test_binarySearch
    __author__ = yeyuc
    __time__ = 2019/12/24 9:54
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
import unittest
from functools import wraps

from .BinarySearch import Solution


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
        self.input = [[5, 7, 7, 8, 8, 10], [2, 3, 5, 7], [2, 3, 5, 7]]
        self.target = [8, 1, 10]
        self.assert_result = [[3, 4], [-1], [-1]]

    def test_nextPermutation(self):
        s = Solution()
        for i in range(len(self.assert_result)):
            # result = s.binary_search(nums=self.input[i], target=self.target[i])
            result = s.binary_search_first(nums=self.input[i], target=self.target[i])
            # result = s.binary_search_last(nums=self.input[i], target=self.target[i])
            self.assertEqual(result in self.assert_result[i], True)


@fn_timer
def main():
    unittest.main()


if __name__ == '__main__':
    main()
