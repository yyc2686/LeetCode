#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 20:55
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : 123.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = 123
    __author__ = yeyuc
    __time__ = 2019/11/20 20:55
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
        # if cost_time <= 1:
        #     cost_time *= 10000
        #     print("本次运行耗时：{0}秒 ".format(str(cost_time)))
        if cost_time <= 60:
            print("本次运行耗时：{0}秒 ".format(str(cost_time)))
        else:
            print('本次运行耗时：{0}时{1}分{2}秒 '.format(int(cost_time / 3600), int((cost_time / 60) % 60), int(cost_time % 60)))
        return result

    return function_timer


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """遍历列表同时查字典"""
        dct = {}
        for i, n in enumerate(nums):
            if target - n in dct:
                return [dct[target - n], i]
            dct[n] = i

    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 构建哈希表，存放值与索引关系，相较list.index(value)更快
        hashmap = {num: id for id, num in enumerate(nums)}
        for i in range(len(nums) - 1):
            j = hashmap.get(target - nums[i])
            if j and i != j:
                return [i, j]

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 通过单重循环找到匹配， num2 = target - num1，是否也在 list 中
        for i in range(len(nums) - 1):
            if target - nums[i] in nums[i + 1:]:
                return [i, i + 1 + nums[i + 1:].index(target - nums[i])]

    def twoSum3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 通过两重循环找到匹配
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


@fn_timer
def main():
    class_client = Solution()
    # result = class_client.twoSum(nums=[1, 2, 3, 4], target=5)
    # result = class_client.twoSum1(nums=[1, 2, 3, 4], target=5)
    # result = class_client.twoSum2(nums=[1, 2, 3, 4], target=5)
    result = class_client.twoSum3(nums=[1, 2, 3, 4], target=5)
    print(result)


if __name__ == '__main__':
    main()
