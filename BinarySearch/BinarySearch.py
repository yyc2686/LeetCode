#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 9:54
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : BinarySearch.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = BinarySearch
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
from functools import wraps


def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        cost_time = t1 - t0
        if cost_time <= 1:
            print("本次运行耗时：{0}秒 ".format(str(cost_time)))
        elif cost_time <= 60:
            print("本次运行耗时：{0}秒 ".format(str(cost_time)))
        else:
            print('本次运行耗时：{0}时{1}分{2}秒 '.format(int(cost_time / 3600), int((cost_time / 60) % 60), int(cost_time % 60)))
        return result

    return function_timer


class Solution:
    #####成功的解法#####
    #####一、寻找一个数（基本的二分搜索）#####
    def binary_search(self, nums, target):
        """
        搜索一个数，如果存在，返回其索引，否则返回 -1。
        :param nums: 有序数组
        :param target: 查询的数字
        :return: 如果存在，返回其索引，否则返回 -1。

        算法：
            因为我们初始化 right = nums.length - 1
            所以决定了我们的「搜索区间」是 [left, right]
            所以决定了 while (left <= right)
            同时也决定了 left = mid+1 和 right = mid-1

            因为我们只需找到一个 target 的索引即可
            所以当 nums[mid] == target 时可以立即返回
        """
        left, right = 0, len(nums) - 1  # 注意：搜索区域为[left, right]
        while left <= right:  # 注意：搜索区间为[left, right]
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid + 1
        return -1

    #####二、寻找左侧边界的二分搜索#####
    def binary_search_first(self, nums, target):
        """
        搜索一个数，如果存在，返回其第一个索引，否则返回 -1。
        :param nums: 有序数组
        :param target: 查询的数字
        :return: 如果存在，返回其索引，否则返回 -1。

        算法：
            因为我们初始化 right = nums.length
            所以决定了我们的「搜索区间」是 [left, right)
            所以决定了 while (left < right)
            同时也决定了 left = mid + 1 和 right = mid

            因为我们需找到 target 的最左侧索引
            所以当 nums[mid] == target 时不要立即返回
            而要收紧右侧边界以锁定左侧边界
        """
        length = len(nums)
        if not length:
            return -1
        left = 0
        right = length
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        # target 比所有数都大, 或者比所有数都小
        if left == length or nums[left] != target:
            return -1;
        else:
            return left

    #####三、寻找右侧边界的二分搜索#####
    def binary_search_last(self, nums, target):
        """
        搜索一个数，如果存在，返回其第一个索引，否则返回 -1。
        :param nums: 有序数组
        :param target: 查询的数字
        :return: 如果存在，返回其索引，否则返回 -1。

        算法：
            因为我们初始化 right = nums.length
            所以决定了我们的「搜索区间」是 [left, right)
            所以决定了 while (left < right)
            同时也决定了 left = mid + 1 和 right = mid

            因为我们需找到 target 的最右侧索引
            所以当 nums[mid] == target 时不要立即返回
            而要收紧左侧边界以锁定右侧边界

            又因为收紧左侧边界时必须 left = mid + 1
            所以最后无论返回 left 还是 right，必须减一
        """
        length = len(nums)
        if not length:
            return -1
        left = 0
        right = length
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        # target 比所有数都大, 或者比所有数都小
        if left == 0 or nums[left - 1] != target:
            return -1;
        else:
            return left - 1

    #####尝试中的解法#####

    #####失败的尝试#####
