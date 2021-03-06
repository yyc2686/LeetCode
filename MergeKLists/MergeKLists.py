#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/8 22:06
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : MergeKLists.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = MergeKLists
    __author__ = yeyuc
    __time__ = 2019/12/8 22:06
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
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        方法2：迭代
        1. 想法
            我们假设 l1 元素严格比 l2元素少，我们可以将 l2 中的元素逐一插入 l1 中正确的位置。
        2. 算法
            首先，
                我们设定一个哨兵节点 "prehead" ，这可以在最后让我们比较容易地返回合并后的链表。
                我们维护一个 prev 指针，我们需要做的是调整它的 next 指针。
            然后，我们重复以下过程，直到 l1 或者 l2 指向了 null ：
                如果 l1 当前位置的值小于等于 l2 ，我们就把 l1 的值接在 prev 节点的后面同时将 l1 指针往后移一个。
                否则，我们对 l2 做同样的操作。不管我们将哪一个元素接在了后面，我们都把 prev 向后移一个元素。
            在循环终止的时候， l1 和 l2 至多有一个是非空的。由于输入的两个链表都是有序的，所以不管哪个链表是非空的，它包含的所有元素都比前面已经合并链表中的所有元素都要大。这意味着我们只需要简单地将非空链表接在合并链表的后面，并返回合并链表。
        """

        # 迭代法：遍历两个链表, 插入小表
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next

    def mergeKLists(self, lists) -> ListNode:
        # 转换成K/2组两个列表合并
        length = len(lists)
        if length == 0:
            return None
        elif length == 1:
            return lists[0]
        else:
            new_lists = []
            for i in range(int(length / 2)):
                new_lists.append(self.mergeTwoLists(l1=lists[i], l2=lists[length - i - 1]))
            if length % 2 == 1:
                new_lists.append(lists[int(length / 2)])
            return self.mergeKLists(lists=new_lists)

    def mergeKLists1(self, lists) -> ListNode:
        # 定义法：遍历K个链表, 建新表
        head = ListNode(-1)
        l = head
        # ps = [list for list in lists]
        ps = {i: lists[i] for i in range(len(lists))}
        BIG_NUM = 100000
        while True:
            # 获取非空链表的值
            vals = {i: BIG_NUM for i in ps}
            for i in ps:
                if ps.get(i):
                    vals[i] = ps[i].val
            # 寻找最小值
            min = BIG_NUM
            for i in vals:
                if vals.get(i) < min:
                    min = vals.get(i)
                    index = i
            if min == BIG_NUM:
                break
            else:
                node = ListNode(ps[index].val)
                l.next = node
                l = l.next
                ps[index] = ps[index].next

        return head.next


@fn_timer
def main():
    pass


if __name__ == '__main__':
    main()
