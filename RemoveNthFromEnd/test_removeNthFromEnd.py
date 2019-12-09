#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 11:51
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : test_removeNthFromEnd.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = test_removeNthFromEnd
    __author__ = yeyuc
    __time__ = 2019/12/5 11:51
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
from .RemoveNthFromEnd import Solution, ListNode, LinkList


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
        self.l = [[1, 2, 3, 4, 5], [1], [1, 2]]
        self.n = [2, 1, 2]
        self.assert_result = [[1, 2, 3, 5], [], [2]]

    def test_removeNthFromEnd(self):
        s = Solution()
        l1 = LinkList()
        for i in range(len(self.assert_result)):
            # 初始化链表与数据
            l2 = l1.initList(data=self.l[i])
            s = Solution()
            result = s.removeNthFromEnd(head=l2, n=self.n[i])
            result = l1.traveList1(head=result)
            self.assertEqual(self.assert_result[i], result)


@fn_timer
def main():
    unittest.main()


if __name__ == '__main__':
    main()
