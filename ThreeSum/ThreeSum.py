#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/2 16:53
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : 3Sum.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = 3Sum
    __author__ = yeyuc
    __time__ = 2019/12/2 16:53
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
    def threeSum(self, nums):
        """
        分析：先排序，再用双指针法
        """
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 2):
            if nums[i] > 0:
                break

            if i != 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while (left < right and nums[left] == nums[left + 1]):
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif s > 0:
                    right -= 1
                else:
                    left += 1
        return result

    def threeSum2(self, nums):
        """
        分析：暴力解法，遍历a+b,判断-(a+b)是否在内,运行超时
        """
        result = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if -(nums[i] + nums[j]) in nums[j + 1:]:
                    l = [nums[i], nums[j], -(nums[i] + nums[j])]
                    l.sort()
                    result.append(l)

        # 去重
        result1 = []
        for item in result:
            if item not in result1:
                result1.append(item)
        return result1

    def threeSum1(self, nums):
        """
        分析：三数之和为0，有以下情况：
        （1）两正一负
        （2）两负一正
        （3）0和一对相反数
        运行超时
        """
        result = []

        # 第一步，按符号分类
        pos, neg, zeros = [], [], []
        for i in nums:
            if i < 0:
                neg.append(i)
            elif i > 0:
                pos.append(i)
            else:
                zeros.append(i)
        pos.sort()
        neg.sort()
        # 0 和一对相反数
        if zeros:
            if len(zeros) >= 3:
                result.append([0, 0, 0])
            for i in pos:
                if -i in neg:
                    result.append([-i, 0, i])
        # 两负一正
        if len(neg) >= 2:
            for i in range(len(neg) - 1):
                for j in range(i + 1, len(neg)):
                    if -(neg[i] + neg[j]) in pos:
                        result.append([neg[i], neg[j], -(neg[i] + neg[j])])
        # 两正一负
        if len(pos) >= 2:
            for i in range(len(pos) - 1):
                for j in range(i + 1, len(pos)):
                    if -(pos[i] + pos[j]) in neg:
                        result.append([-(pos[i] + pos[j]), pos[i], pos[j]])

        # 去重
        result1 = []
        for item in result:
            if item not in result1:
                result1.append(item)
        return result1


@fn_timer
def main():
    s = [[-1, 0, 1, 2, -1, -4], [0, 0, 0], [-2, 0, 0, 2, 2]]
    class_client = Solution()
    result = class_client.threeSum(nums=s[-1])
    result


if __name__ == '__main__':
    main()
