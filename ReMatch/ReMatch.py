#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 17:29
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : ReMatch.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = ReMatch
    __author__ = yeyuc
    __time__ = 2019/12/3 17:29
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
    def isMatch(self, s: str, p: str) -> bool:
        """
        递归法：
            1、递归的终止条件：
            （1）如果s字符串的长度为0，如果此时字符串p当且仅当有形如"a*b*c*d*e*"这样的格式时，返回true；否则，返回false。
            （2）如果s字符串的长度不为0，而p字符串的长度为0，返回false。
            2、递归的过程：
            （1）如果s的最后一个字符与p的最后一个字符相等，或者说p的最后一个字符为"."，
                 那么我们直接看字符串s中除去最后一个字符的字符串能否与字符串p中除去最后一个字符的字符串相匹配。
            （2）如果p的最后一个字符为"*"，这种情况比较复杂，又分为两种情况。
                a.如果s的最后一个字符既不与p的最后第二个字符相等，p的最后第二个字符也不为"."，
                  那么我们直接看字符串s能否与字符串p中除去最后两个字符的字符串相匹配。
                b.如果s的最后一个字符与p的最后第二个字符相等，或者说p的最后第二个字符为"."，，这种情况比较复杂，又分为三种情况。
                    b-1：我们看字符串s中除去最后一个字符的字符串能否与字符串p相匹配（即把s中的最后一个字符与p的最后一个字符（*）相匹配）。
                    b-2：我们看字符串s能否与字符串p中除去最后一个字符的字符串相匹配（即把s中的最后一个字符与p的最后第二个字符相匹配）。
                    b-3：我们看字符串s中除去最后一个字符的字符串能否与字符串p中除去最后两个字符的字符串相匹配（直接舍去p中的最后两个字符）。
                只要上述b-1、b-2、b-3三种情况中有一种情况相匹配，我们就返回true。如果三种情况都不匹配，我们就返回false。
        """
        ns = len(s)
        np = len(p)
        # 如果s字符串的长度不为0，而p字符串的长度为0，返回false。
        if ns and not np:
            return False

        # 如果s字符串的长度为0，如果此时字符串p当且仅当有形如"a*b*c*d*e*"这样的格式时，返回true；否则，返回false。
        if not ns:
            if np % 2 == 1:
                return False
            i = 1
            while i < np and p[i] != '*':
                i += 2
            if i == np + 1 or i == 1:
                return True
            else:
                return False

        # （1）如果s的最后一个字符与p的最后一个字符相等，或者说p的最后一个字符为"."，那么我们直接看字符串s中除去最后一个字符的字符串能否与字符串p中除去最后一个字符的字符串相匹配。
        if s[-1] == p[-1] or p[-1] == '.':
            return self.isMatch(s=s[:-1], p=p[:-1])

        # （2）如果p的最后一个字符为"*"，这种情况比较复杂，又分为两种情况。
        if p[-1] == '*':
            # a.如果s的最后一个字符既不与p的最后第二个字符相等，p的最后第二个字符也不为"."，那么我们直接看字符串s能否与字符串p中除去最后两个字符的字符串相匹配。
            if s[-1] != p[-2] and p[-2] != '.':
                return self.isMatch(s=s, p=p[:-2])
            # b.如果s的最后一个字符与p的最后第二个字符相等，或者说p的最后第二个字符为"."，，这种情况比较复杂，又分为三种情况。
            # b - 1：我们看字符串s中除去最后一个字符的字符串能否与字符串p相匹配（即把s中的最后一个字符与p的最后一个字符（ * ）相匹配）。
            # b - 2：我们看字符串s能否与字符串p中除去最后一个字符的字符串相匹配（即把s中的最后一个字符与p的最后第二个字符相匹配）。
            # b - 3：我们看字符串s中除去最后一个字符的字符串能否与字符串p中除去最后两个字符的字符串相匹配（直接舍去p中的最后两个字符）。
            # 只要上述b - 1、b - 2、b - 3 三种情况中有一种情况相匹配，我们就返回true。如果三种情况都不匹配，我们就返回false。
            else:
                return self.isMatch(s=s[:-1], p=p) or self.isMatch(s=s, p=p[:-1]) or self.isMatch(s=s[:-1], p=p[:-2])
        else:
            return False


@fn_timer
def main():
    s = ["aa", "aa", "ab", "aab", "mississippi"]
    p = ["a", "a*", ".*", "c*a*b", "mis*is*p*."]
    class_client = Solution()
    result = class_client.isMatch(s=s[0], p=p[0])
    result


if __name__ == '__main__':
    main()
