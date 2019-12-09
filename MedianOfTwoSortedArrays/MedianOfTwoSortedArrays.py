#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 19:30
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : MedianOfTwoSortedArrays.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = MedianOfTwoSortedArrays
    __author__ = yeyuc
    __time__ = 2019/11/28 19:30
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
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if not nums1:
            return nums2[int(len(nums2) / 2)] if len(nums2) % 2 == 1 else (nums2[int(len(nums2) / 2)] + nums2[
                int(len(nums2) / 2) - 1]) / 2
        if not nums2:
            return nums1[int(len(nums1) / 2)] if len(nums1) % 2 == 1 else (nums1[int(len(nums1) / 2)] + nums1[
                int(len(nums1) / 2) - 1]) / 2

        INT_MIN = min(nums1[0], nums2[0])
        INT_MAX = max(nums1[-1], nums2[-1])
        # 保证数组1一定最短
        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2
        n = len(nums1)
        m = len(nums2)

        # Ci 为第i个数组的割, 比如C1为2时表示第1个数组只有2个元素。
        # LMaxi为第i个数组割后的左元素。
        # RMini为第i个数组割后的右元素。
        lo = 0
        hi = 2 * n
        while lo <= hi:
            c1 = int((lo + hi) / 2)
            c2 = m + n - c1

            LMax1 = INT_MIN if c1 == 0 else nums1[int((c1 - 1) / 2)]
            LMax2 = INT_MIN if c2 == 0 else nums2[int((c2 - 1) / 2)]
            RMin1 = INT_MAX if c1 == 2 * n else nums1[int(c1 / 2)]
            RMin2 = INT_MAX if c2 == 2 * m else nums2[int(c2 / 2)]

            if LMax1 > RMin2:
                hi = c1 - 1
            elif LMax2 > RMin1:
                lo = c1 + 1;
            else:
                break

        return (max(LMax1, LMax2) + min(RMin1, RMin2)) / 2.0

    def findMedianSortedArrays3(self, nums1, nums2) -> float:
        """不引入内嵌函数"""
        # 两个列表本身有序,简化合并与排序
        nums = []
        i, j = 0, 0
        for k in range(len(nums1) + len(nums2)):
            if i >= len(nums1) and j < len(nums2):
                nums.append(nums2[j])
                j += 1
            elif i < len(nums1) and j >= len(nums2):
                nums.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if len(nums) % 2 == 0:
            return 0.5 * (nums[int(len(nums) / 2)] + nums[int(len(nums) / 2) - 1])
        else:
            return nums[int(len(nums) / 2)]

    def findMedianSortedArrays2(self, nums1, nums2) -> float:
        """利用题设条件，优化合并于排序，引入内嵌函数，减少代码量"""

        def return_median(nums):
            if len(nums) % 2 == 0:
                return 0.5 * (nums[int(len(nums) / 2)] + nums[int(len(nums) / 2) - 1])
            else:
                return nums[int(len(nums) / 2)]

        if not nums1:
            return return_median(nums=nums2)
        if not nums2:
            return return_median(nums=nums1)

        # 两个列表本身有序,简化合并与排序
        nums = []
        i, j = 0, 0
        for k in range(len(nums1) + len(nums2)):
            if i >= len(nums1) and j < len(nums2):
                nums.append(nums2[j])
                j += 1
            elif i < len(nums1) and j >= len(nums2):
                nums.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        return return_median(nums=nums)

    def findMedianSortedArrays1(self, nums1, nums2) -> float:
        """直接合并，然后取中位数, 复杂度："""
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 0:
            return 0.5 * (nums1[int(len(nums1) / 2)] + nums1[int(len(nums1) / 2) - 1])
        else:
            return nums1[int(len(nums1) / 2)]


@fn_timer
def main():
    nums1 = [1, 2]
    nums2 = [3, 4, 5]
    class_client = Solution()
    median = class_client.findMedianSortedArrays(nums1=nums1, nums2=nums2)
    median


if __name__ == '__main__':
    main()
