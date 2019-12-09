#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 20:56
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : LetterCombinations.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = LetterCombinations
    __author__ = yeyuc
    __time__ = 2019/12/4 20:56
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
    def letterCombinations(self, digits: str):
        def list_product(l1, l2):
            return [i+j for i in l1 for j in l2]

        # 暴力解法
        if not digits:
            return []

        # （1）确定每一个数字对应的字母
        dic = {"2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'],
               "4": ['g', 'h', 'i'], "5": ['j', 'k', 'l'], "6": ['m', 'n', 'o'],
               "7": ['p', 'q', 'r', 's'], "8": ['t', 'u', 'v'], "9": ['w', 'x', 'y', 'z']}
        t = [dic[i] for i in digits]
        l = t[0]
        for i in range(1, len(digits)):
            l = list_product(l1=l, l2=t[i])
        return l



@fn_timer
def main():
    digits = ["23"]
    class_client = Solution()
    result = class_client.letterCombinations(digits=digits[-1])
    result


if __name__ == '__main__':
    main()
