#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/8 11:43
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : IsBracketsValid.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = IsBracketsValid
    __author__ = yeyuc
    __time__ = 2019/12/8 11:43
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
    def isValid(self, s: str) -> bool:
        """
        :param s: 括号字符串
        :return: 字符串是否合法
        """
        """
        1. 算法原理
            (1) 栈先入后出特点恰好与本题括号排序特点一致，即若遇到左括号入栈，遇到右括号时将对应栈顶左括号出栈，则遍历完所有括号后 stack 仍然为空；
            (2) 建立哈希表 dic 构建左右括号对应关系：key左括号，value右括号；这样查询 2个括号是否对应只需 O(1)时间复杂度；建立栈 stack，遍历字符串 s 并按照算法流程一一判断。
        2. 算法流程
            (1) 如果 c 是左括号，则入栈 push；
            (2) 否则通过哈希表判断括号对应关系，若 stack 栈顶出栈括号 stack.pop() 与当前遍历括号 c 不对应，则提前返回 false。
        3. 解决边界问题：
            栈 stack 为空： 此时 stack.pop() 操作会报错；因此，我们采用一个取巧方法，给 stack 赋初值 ?，并在哈希表 dic 中建立 key: '?'，value:'?'的对应关系予以配合。此时当 stack 为空且 c 为右括号时，可以正常提前返回 false;
            字符串 s 以左括号结尾： 此情况下可以正常遍历完整个 s，但 stack 中遗留未出栈的左括号；因此，最后需返回 len(stack) == 1，以判断是否是有效的括号组合。
        4. 复杂度分析
            时间复杂度 O(N)：正确的括号组合需要遍历 1 遍 s；
            空间复杂度 O(N)：哈希表和栈使用线性的空间大小。
        """
        # （0）空串返回True, 奇串返回False
        length = len(s)
        if length == 0:
            return True
        if length % 2 == 1:
            return False

        stack = ['?']  # 栈 stack 为空： 此时 stack.pop() 操作会报错
        dict = {'(': ')', '[': ']', '{': '}', '?':'?'}
        for c in s:
            if c in dict:
                stack.append(c)
            elif dict.get(stack.pop()) != c:
                return False
        return len(stack) == 1

    def isValid1(self, s: str) -> bool:
        """
        :param s: 括号字符串
        :return: 字符串是否合法
        """
        # 单指针，寻找第一个左右交汇处 : 递归实现

        # （0）空串返回True
        length = len(s)
        if length == 0:
            return True
        if length % 2 == 1:
            return False

        brackets = ['(', '[', '{', ')', ']', '}']

        # （1）各类括号在任意时刻左括号数量大于等于右括号数量
        dict = {bracket: 0 for bracket in brackets}

        for i in s:
            dict[i] += 1

        # （2）各类括号成对出现
        for i in range(3):
            if dict.get(brackets[i]) != dict.get(brackets[i + 3]):
                return False

        brackets = {'(': 0, '[': 1, '{': 2, ')': 3, ']': 4, '}': 5}
        for i in range(length - 1):
            index1 = brackets.get(s[i])
            index2 = brackets.get(s[i + 1])
            if index1 < 3 and index2 >= 3:
                if index2 - index1 == 3:
                    return self.isValid(s=s[:i] + s[i + 2:])
                else:
                    return False
            elif index1 >= 3 and index2 < 3:
                return False
        return True


@fn_timer
def main():
    pass


if __name__ == '__main__':
    main()
