#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 16:20
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : AddTwoNumbers.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = AddTwoNumbers
    __author__ = yeyuc
    __time__ = 2019/11/21 16:20
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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkList(object):
    def __init__(self):
        self.head = None

    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return self.head

    # 链表判空
    def isEmpty(self):
        if self.head.next == 0:
            print
            "Empty List!"
            return 1
        else:
            return 0

    # 取链表长度
    def getLength(self):
        if self.isEmpty():
            exit(0)

        p = self.head
        len = 0
        while p:
            len += 1
            p = p.next
        return len

    # 遍历链表
    def traveList(self):
        if self.isEmpty():
            exit(0)
        print('\rlink list traving result: ')
        p = self.head
        while p:
            print(p.data)
            p = p.next

    # 链表插入数据函数
    def insertElem(self, key, index):
        if self.isEmpty():
            exit(0)
        if index < 0 or index > self.getLength() - 1:
            print("\rKey Error! Program Exit.")
            exit(0)

        p = self.head
        i = 0
        while i <= index:
            pre = p
            p = p.next
            i += 1

        # 遍历找到索引值为 index 的结点后, 在其后面插入结点
        node = ListNode(key)
        pre.next = node
        node.next = p

    # 链表删除数据函数
    def deleteElem(self, index):
        if self.isEmpty():
            exit(0)
        if index < 0 or index > self.getLength() - 1:
            print("\rValue Error! Program Exit.")
            exit(0)

        i = 0
        p = self.head
        # 遍历找到索引值为 index 的结点
        while p.next:
            pre = p
            p = p.next
            i += 1
            if i == index:
                pre.next = p.next
                p = None
                return 1

        # p的下一个结点为空说明到了最后一个结点, 删除之即可
        pre.next = None


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        1.从左到右对链表进行迭代
        2.位置相对应的2个数字相加，10为除数，商为进位，余数为新链表当前位置的数据
        3.此时应考虑相加是否会进位
        4.注意空指针异常问题
        """
        v = []
        c = 0
        while l1 or l2:
            if l1 and l2:
                num1 = l1.val
                num2 = l2.val
                s = num1 + num2 + c
                l1 = l1.next
                l2 = l2.next
            elif l1 and not l2:
                s = l1.val + c
                l1 = l1.next
            elif not l1 and l2:
                s = l2.val + c
                l2 = l2.next
            v.append(s % 10)
            c = int(s / 10)
        if c:
            v.append(c)
        head = ListNode(v[0])
        p = head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in v[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return head

    def addTwoNumbers3(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 转换与整数化同时进行
        num1 = 0
        t = 0
        while l1:
            num1 += l1.val * 10 ** t
            t += 1
            l1 = l1.next
        num2 = 0
        t = 0
        while l2:
            num2 += l2.val * 10 ** t
            t += 1
            l2 = l2.next
        num = num1 + num2

        # 转换与去整数化同时进行
        num = str(num)
        head = ListNode(num[-1])
        p = head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in range(len(str(num)) - 2, -1, -1):
            node = ListNode(num[i])
            p.next = node
            p = p.next
        return head

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 转换与整数化同时进行
        num1 = 0
        t = 0
        while l1:
            num1 += l1.val * 10 ** t
            t += 1
            l1 = l1.next
        num2 = 0
        t = 0
        while l2:
            num2 += l2.val * 10 ** t
            t += 1
            l2 = l2.next
        num = num1 + num2
        l = [int(str(num)[i]) for i in range(len(str(num)) - 1, -1, -1)]

        head = ListNode(l[0])
        p = head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in l[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return head

    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 将l1和l2转换为列表
        list1 = []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        list2 = []
        while l2:
            list2.append(l2.val)
            l2 = l2.next

        # 直接将问题转换成整数加法
        num1 = 0
        t = 0
        for i in list1:
            num1 += i * 10 ** t
            t += 1

        num2 = 0
        t = 0
        for i in list2:
            num2 += i * 10 ** t
            t += 1

        num = num1 + num2
        l = [int(str(num)[i]) for i in range(len(str(num)) - 1, -1, -1)]

        head = ListNode(l[0])
        p = head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in l[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return head


@fn_timer
def main():
    # l1 = [2, 4, 3]，l2 = [5, 6, 4]
    # 当一个列表比另一个列表长时
    # l1 = [0, 1]，l2 = [0, 1, 2]
    # 当一个列表比另一个列表长时
    # l1 = []，l2 = [0, 1]
    # 当一个列表为空时，即出现空列表
    # l1 = [9, 9]，l2 = [1]
    # 求和运算最后可能出现额外的进位，这一点很容易被遗忘

    # 初始化链表与数据
    l1, l2 = LinkList(), LinkList()
    # l1=l1.initList(data=[2, 4, 3])
    # l2=l2.initList(data=[5, 6, 4])
    # l1=l1.initList(data=[0])
    # l2=l2.initList(data=[0])
    # l1 = l1.initList(data=[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    # l2 = l2.initList(data=[5, 6, 4])
    # l1 = l1.initList(data=[5])
    # l2 = l2.initList(data=[5])
    l1 = l1.initList(data=[1])
    l2 = l2.initList(data=[9, 9, 9])

    class_client = Solution()
    result = class_client.addTwoNumbers(l1=l1, l2=l2)
    print(result)


if __name__ == '__main__':
    main()
