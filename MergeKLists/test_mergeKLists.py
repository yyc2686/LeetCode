#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/8 22:06
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : test_mergeKLists.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = test_mergeKLists
    __author__ = yeyuc
    __time__ = 2019/12/8 22:06
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
from .MergeKLists import Solution, ListNode, LinkList


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
        self.l = [[[1, 4, 5], [1, 3, 4], [4, 6]]]
        self.assert_result = [[1, 1, 3, 4, 4, 4, 5, 6]]

    def test_mergeKLists(self):
        s = Solution()
        l = LinkList()
        for i in range(len(self.assert_result)):
            # 初始化链表与数据
            ls = [l.initList(data=li) for li in self.l[i]]
            s = Solution()
            result = s.mergeKLists(lists=ls)
            result = l.traveList1(head=result)
            result.sort()
            self.assertEqual(self.assert_result[i], result)


@fn_timer
def main():
    unittest.main()


if __name__ == '__main__':
    main()
