#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 16:21
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : ContainerWithMostWater.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = ContainerWithMostWater
    __author__ = yeyuc
    __time__ = 2019/12/2 16:21
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
    def maxArea(self, height) -> int:
        # 两个指针
        n = len(height)
        left, right = 0, n - 1
        h = min(height[left], height[right])
        max_area = (n - 1) * h
        while left <= right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            area = (right - left) * min(height[left], height[right])
            max_area = max(area, max_area)
        return max_area

    def maxArea2(self, height) -> int:
        # 两个指针
        n = len(height)
        left, right = 0, n - 1
        h = min(height[left], height[right])
        max_area = (n - 1) * h
        while left <= right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            area = (right - left) * min(height[left], height[right])
            max_area = max(area, max_area)
        return max_area

    def maxArea1(self, height) -> int:
        # 暴力破解
        max_area = 0
        n = len(height)

        for i in range(n - 1):
            for j in range(i + 1, n):
                area = (j - i) * min(height[i], height[j])
                max_area = max(area, max_area)
        return max_area


@fn_timer
def main():
    s = [[1, 8, 6, 2, 5, 4, 8, 3, 7]]
    class_client = Solution()
    result = class_client.maxArea(height=s[0])
    result


if __name__ == '__main__':
    main()
