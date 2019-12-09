#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 11:51
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : RemoveNthFromEnd.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = RemoveNthFromEnd
    __author__ = yeyuc
    __time__ = 2019/12/5 11:51
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
        if not self.head.next:
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
        datas = []
        if self.isEmpty():
            exit(0)
        print('\rlink list traving result: ')
        p = self.head
        while p:
            datas.append(p.data)
            p = p.next

    def traveList1(self, head):
        def isEmpty(head):
            if not head or head.next == 0:
                return 1
            else:
                return 0

        datas = []
        if isEmpty(head):
            return []
        # print('\rlink list traving result: ')
        p = head
        while p:
            datas.append(p.val)
            p = p.next
        return datas

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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd4(self, head: ListNode, n: int) -> ListNode:
        """
        :param head: 链表表头
        :param n: 删除的节点位置
        :return: 删除完对应节点的链表表头
        """

        # 优化，添加哑节点，双指针一次遍历
        # 链表判空
        def isEmpty(head):
            if head.next == 0:
                return 1
            else:
                return 0

        if isEmpty(head):
            return head

        if n <= 0:
            return None

        # 添加哑节点
        p = ListNode(-1)
        p.next = head
        head = p

        i = 0
        p, q = head, head

        for i in range(n):
            p = p.next  # p先走n步

        while p.next:
            q = q.next
            p = p.next
        if q.next.next:
            q.next = q.next.next
        else:
            q.next = None
        return head.next

    def removeNthFromEnd3(self, head: ListNode, n: int) -> ListNode:
        """
        :param head: 链表表头
        :param n: 删除的节点位置
        :return: 删除完对应节点的链表表头
        """

        # 优化，添加哑节点，避免极端情况(两次遍历)
        # 链表判空
        def isEmpty(head):
            if head.next == 0:
                return 1
            else:
                return 0

        # 取链表长度
        def getLength(head):
            if isEmpty(head):
                exit(0)

            p = head
            len = 0
            while p:
                len += 1
                p = p.next
            return len

        if isEmpty(head):
            return head
        length = getLength(head)
        n = length - n

        if n < 0 or n > length - 1:
            return None

        # 添加哑节点
        p = ListNode(-1)
        p.next = head
        head = p

        i = 0
        p = head
        for i in range(n):
            p = p.next
        p.next = p.next.next

        return head.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        :param head: 链表表头
        :param n: 删除的节点位置
        :return: 删除完对应节点的链表表头
        """

        # 优化，添加哑节点，避免极端情况(两次遍历)
        # 链表判空
        def isEmpty(head):
            if head.next == 0:
                return 1
            else:
                return 0

        # 取链表长度
        def getLength(head):
            if isEmpty(head):
                exit(0)

            p = head
            len = 0
            while p:
                len += 1
                p = p.next
            return len

        if isEmpty(head):
            return head
        length = getLength(head)
        n = length - n

        if n < 0 or n > length - 1:
            return None

        # 添加哑节点
        p = ListNode(-1)
        p.next = head
        head = p

        i = 0
        p = head
        # 遍历找到索引值为 index 的结点
        try:
            while p.next:
                pre = p
                p = p.next
                if i == n:
                    pre.next = p.next
                    p = None
                    return head.next
                i += 1
        except:
            return head.next

        return head.next

    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        """
        :param head: 链表表头
        :param n: 删除的节点位置
        :return: 删除完对应节点的链表表头
        """

        # 暴力解法，变倒数为正数依次遍历
        # 链表判空
        def isEmpty(head):
            if head.next == 0:
                return 1
            else:
                return 0

        # 取链表长度
        def getLength(head):
            if isEmpty(head):
                exit(0)

            p = head
            len = 0
            while p:
                len += 1
                p = p.next
            return len

        if isEmpty(head):
            return head
        length = getLength(head)
        n = length - n

        if n < 0 or n > length - 1:
            return None

        if n == 0:
            if length == 1:
                return None
            else:
                head = head.next

        i = 0
        p = head
        # 遍历找到索引值为 index 的结点
        try:
            while p.next:
                pre = p
                p = p.next
                i += 1
                if i == n:
                    pre.next = p.next
                    p = None
                    return head
        except:
            return head

        # p的下一个结点为空说明到了最后一个结点, 删除之即可
        # try:
        # pre.next = None
        return head


@fn_timer
def main():
    l = [[1, 2, 3, 4, 5], [1], [1, 2]]
    n = [2, 1, 2]
    # 初始化链表与数据
    l1 = LinkList()
    l2 = l1.initList(data=l[-1])
    class_client = Solution()
    result = class_client.removeNthFromEnd(head=l2, n=n[-1])
    print(result)


if __name__ == '__main__':
    main()
