#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 13:00
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : NextPermutation.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = NextPermutation
    __author__ = yeyuc
    __time__ = 2019/12/9 13:00
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
    #####成功的解法#####
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        解法：一遍扫描
        1.思路
            1）对于任何给定序列的降序，没有可能的下一个更大的排列。例如，[9, 5, 4, 3, 1]
            2）我们需要从右边找到第一对两个连续的数字 a[i] 和 a[i−1]，它们满足 a[i]>a[i−1]。现在，没有对 a[i-1] 右侧的重新排列可以创建更大的排列，因为该子数组由数字按降序组成。因此，我们需要重新排列 a[i-1] 右边的数字，包括它自己。
            3）我们想要创建比当前更大的排列。因此，我们需要将数字 a[i-1] 替换为位于其右侧区域的数字中比它更大的数字。交换数字 a[i−1] 和 a[j]。索引 i−1 处有正确的数字。 但目前的排列仍然不是我们正在寻找的排列。
            4）我们需要通过仅使用 a[i−1]右边的数字来形成最小的排列。 因此，我们需要放置那些按升序排列的数字，以获得最小的排列。但是，请记住，在从右侧扫描数字时，我们只是继续递减索引直到我们找到 a[i] 和 a[i−1] 这对数。其中，a[i] > a[i-1]。因此，a[i−1] 右边的所有数字都已按降序排序。此外，交换 a[i−1] 和 a[j] 并未改变该顺序。因此，我们只需要反转 a[i−1] 之后的数字，以获得下一个最小的字典排列。

        2.算法
            1）从右往左遍历，找到第一对两个连续的数字 a[i] 和 a[i−1]，满足 a[i]>a[i−1]
            2）从右往左遍历，找到第一个比a[i]更大的数a[j]
            3）交换数字 a[i-1] 和 a[j]
            4）以交换后a[i-1]所在位置为中心，左右部分翻转，
        """

        def overturn(l):
            length = len(l)
            for i in range(int(length / 2)):
                l[i], l[length - i - 1] = l[length - i - 1], l[i]
            return l

        length = len(nums)
        if length in [0, 1]:
            return nums

        # 1）从右往左遍历，找到第一对两个连续的数字 a[i] 和 a[i−1]，满足 a[i]>a[i−1]
        p, q = -2, -1
        while nums[p] >= nums[q]:
            p -= 1
            q -= 1
            if -q >= length:
                nums = overturn(l=nums)
                return nums

        # 2）从右往左遍历，找到第一个比a[i]更大的数a[j]
        for i in range(1, length):
            if nums[-i] > nums[p]:
                break

        # 3）交换数字 a[i-1] 和 a[j]
        nums[-i], nums[p] = nums[p], nums[-i]

        # 4）以交换后a[i-1]所在位置为中心，左右部分翻转，
        j = -1
        q = q + length
        for i in range(q, q + int((length - q) / 2)):
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        return nums

    #####尝试中的解法#####

    #####失败的尝试#####
    def count_sum(self, nums):
        length = len(nums)
        sum0 = sum([nums[i] * 10 ** (length - i - 1) for i in range(length)])
        return sum0

    def compare_two_lists(self, nums_1, nums_2):
        length = len(nums_1)
        for i in range(length):
            if nums_1 < nums_2:
                return nums_2
            elif nums_1 > nums_2:
                return nums_1

    def compare_two_lists(nums_1, nums_2):
        length = len(nums_1)
        for i in range(length):
            if nums_1 < nums_2:
                return nums_2
            elif nums_1 > nums_2:
                return nums_1

    def dfs(self, curNum, curNums, res, sum0):
        """
        :param curStr: 当前访问元素
        :param curNums: 目标剩余数字列表
        :param res: 当前数字列表
        :return:
        """

        # 因为是递归函数，所以先写递归终止条件
        # 目标剩余数字列表长度为0/1时开始结算
        if not curNums or len(curNums) == 1:
            res.append(curNum)
            return res

        # 目标剩余数字列表长度大于1，继续进行递归
        for num in set(curNums):
            # 子分支新增数字不小于目标列表对应位数字
            if curNum > num:
                continue
            nums_1 = [i for i in curNums]
            nums_1.remove(num)
            res_1 = [i for i in res]
            res_1.append(num)
            res = self.dfs(curNum=nums_1[0], curNums=nums_1, res=res_1, sum0=sum0)
            sum1 = self.count_sum(res)
            if sum1 > sum0[0]:
                if len(sum0) == 1:
                    sum0.append(sum1)
                elif sum1 < sum[1]:
                    sum0[1] = sum1
            res = []
        return res

    def nextPermutation2(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """ 
        回溯法
        1. 想法：
            len == 0, 1, 2时，容易；len>2时应该能够转换成多个len-1的子问题；
            
        2、画图以后，可以分析出的结论：
            每一个分支，每一步至多有一个子分支能保留，子分支新增数字不小于目标列表对应位数字：
                1) 如果新增数字<目标列表对应位数字，整支去掉
                2) 如果超过一个分支的新增数字大于目标列表对应位数字，取最小的分支
                3）如果有多个相同分支，仅保留一个
            剩余数字为空时进行结算     
        """

        # 回溯法
        length = len(nums)
        if length in [0, 1]:
            return nums

        nums_1 = [i for i in nums]
        nums_1.sort(reverse=True)
        if nums == nums_1:
            nums.sort()
            return nums
        # 执行深度优先遍历，搜索可能的结果

        res = self.dfs(curNum=nums[0], curNums=nums, res=[], sum0=[self.count_sum(nums)])

        return res

    def nextPermutation1(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 根据题意：分析规律, 暴力破解，失败！TODO
        # （1）nums长度为0/1， nums不变
        # （2）如果元素是最大的，则返回最小值
        # （3）如果直接把最后两个元素对换, 兑换后的数更大，则结束; 否则，最后一位继续向前移动一位
        def count_sum(nums):
            length = len(nums)
            sum0 = sum([nums[i] * 10 ** (length - i - 1) for i in range(length)])
            return sum0

        length = len(nums)
        if length in [0, 1]:
            return nums

        sum0 = count_sum(nums=nums)

        nums_1 = [i for i in nums]
        nums_1.sort(reverse=True)
        if nums == nums_1:
            nums.sort()
            return nums
        else:
            for j in range(2, length + 1):
                nums_1 = [i for i in nums]
                nums_1.insert(-j, nums_1[-1])
                if count_sum(nums_1[:-1]) > sum0:
                    nums = [i for i in nums]
                    nums.insert(-j, nums[-1])
                    nums.pop()
                    break
            return nums


@fn_timer
def main():
    pass


if __name__ == '__main__':
    main()
