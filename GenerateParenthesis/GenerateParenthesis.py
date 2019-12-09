#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/8 19:01
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : GenerateParenthesis.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = GenerateParenthesis
    __author__ = yeyuc
    __time__ = 2019/12/8 19:01
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
    def isValid(self, s: str) -> bool:
        """
        :param s: 括号字符串
        :return: 字符串是否合法
        """
        """
        1. 算法原理
            (1) 栈先入后出特点恰好与本题括号排序特点一致，即若遇到左括号入栈，遇到右括号时将对应栈顶左括号出栈，则遍历完所有括号后 stack 仍然为空；
            (2) 建立哈希表 dic 构建左右括号对应关系：key左括号，value右括号；这样查询 2个括号是否对应只需 O(1)时间复杂度；建立栈 stack，遍历字符串 s 并按照算法流程一一判断。
        2. 算法流程
            (1) 如果 c 是左括号，则入栈 push；
            (2) 否则通过哈希表判断括号对应关系，若 stack 栈顶出栈括号 stack.pop() 与当前遍历括号 c 不对应，则提前返回 false。
        3. 解决边界问题：
            栈 stack 为空： 此时 stack.pop() 操作会报错；因此，我们采用一个取巧方法，给 stack 赋初值 ?，并在哈希表 dic 中建立 key: '?'，value:'?'的对应关系予以配合。此时当 stack 为空且 c 为右括号时，可以正常提前返回 false;
            字符串 s 以左括号结尾： 此情况下可以正常遍历完整个 s，但 stack 中遗留未出栈的左括号；因此，最后需返回 len(stack) == 1，以判断是否是有效的括号组合。
        4. 复杂度分析
            时间复杂度 O(N)：正确的括号组合需要遍历 1 遍 s；
            空间复杂度 O(N)：哈希表和栈使用线性的空间大小。
        """
        # （0）空串返回True, 奇串返回False
        length = len(s)
        if length == 0:
            return True
        if length % 2 == 1:
            return False

        stack = ['?']  # 栈 stack 为空： 此时 stack.pop() 操作会报错
        for c in s:
            if c == '(':
                stack.append(c)
            elif stack.pop() != '(':
                return False
        return len(stack) == 1

    def generateParenthesis1(self, n: int):
        """
        n对括号的所有合法组合
        :param n: 括号对数
        :return: 所有合法的组合列表
        """
        """
        一、反思：
            首先，面向小白：什么是动态规划？在此题中，动态规划的思想类似于数学归纳法，当知道所有 i<n 的情况时，我们可以通过某种算法算出 i=n 的情况。
            本题最核心的思想是，考虑 i=n 时相比 n-1 组括号增加的那一组括号的位置。

        二、思路：
            当我们清楚所有 i<n 时括号的可能生成排列后，对与 i=n 的情况，我们考虑整个括号排列中最左边的括号。
            它一定是一个左括号，那么它可以和它对应的右括号组成一组完整的括号 "( )"，我们认为这一组是相比 n-1 增加进来的括号。
            那么，剩下 n-1 组括号有可能在哪呢？
            【这里是重点，请着重理解】
            剩下的括号要么在这一组新增的括号内部，要么在这一组新增括号的外部（右侧）。
            既然知道了 i<n 的情况，那我们就可以对所有情况进行遍历：
            "(" + 【i=p时所有括号的排列组合】 + ")" + 【i=q时所有括号的排列组合】
            其中 p + q = n-1，且 p q 均为非负整数。
            事实上，当上述 p 从 0 取到 n-1，q 从 n-1 取到 0 后，所有情况就遍历完了。
            注：上述遍历是没有重复情况出现的，即当 (p1,q1)≠(p2,q2) 时，按上述方式取的括号组合一定不同。        
        """

        # 动态规划
        if n == 0:
            return []
        total_l = [[None]]  # 标记n=0的情形
        total_l.append(['()'])  # 标记n=1的情形

        # 遍历其余的n-1括号的组合
        for i in range(2, n + 1):
            # 保存n = i的结果
            l = []
            for j in range(i):
                now_list_p = total_l[j]  # p=j时的所有组合
                now_list_q = total_l[i - j - 1]  # q=i-j+1时的所有组合
                for k1 in now_list_p:
                    for k2 in now_list_q:
                        if not k1:
                            k1 = ""
                        if not k2:
                            k2 = ""
                        s = '(' + k1 + ')' + k2
                        l.append(s)
            total_l.append(l)
        return total_l[n]

    def dfs(self, curStr, left, right, res):
        """
        :param curStr: 当前递归得到的结果
        :param left: 左括号还有几个没有用掉
        :param right: 右边的括号还有几个没有用掉
        :param res: 结果集
        :return:
        """
        # 因为是递归函数，所以先写递归终止条件
        # 左右括号数量均为0，终止，开始结算
        if not left and not right:
            res.append(curStr)
            return res

        # 因为每一次尝试，都使用新的字符串变量，所以没有显式的回溯过程
        # 在递归终止的时候，直接把它添加到结果集即可，与「力扣」第 46 题、第 39 题区分
        # 如果左边还有剩余，继续递归下去
        if left:
            # 拼接上一个左括号，并且剩余的左括号个数减 1
            self.dfs(curStr=curStr + "(", left=left - 1, right=right, res=res)

        # 什么时候可以用右边？例如，(((((()，此时 left < right，
        # 不能用等号，因为只有先拼了左括号，才能拼上右括号
        if right and left < right:
            # 拼接上一个右括号，并且剩余的右括号个数减 1
            self.dfs(curStr=curStr + ")", left=left, right=right - 1, res=res)
        return res

    def generateParenthesis2(self, n: int):
        """
        n对括号的所有合法组合
        :param n: 括号对数
        :return: 所有合法的组合列表
        """
        """
        方法：回溯算法（深度优先遍历）
        一、思路
            如果完成一件事情有很多种方法，并且每一种方法分成若干步骤，那多半就可以使用“回溯”算法完成。
            “回溯”算法的基本思想是“尝试搜索”，一条路如果走不通（不能得到想要的结果），就回到上一个“路口”，尝试走另一条路。
            因此，“回溯”算法的时间复杂度一般不低。如果能提前分析出，走这一条路并不能得到想要的结果，可以跳过这个分支，这一步操作叫“剪枝”。

        二、做“回溯”算法问题的基本套路是：
            1、使用题目中给出的示例，画树形结构图，以便分析出递归结构；一般来说，树形图不用画完，就能够分析出递归结构和解题思路。
            2、分析一个结点可以产生枝叶的条件、递归到哪里终止、是否可以剪枝、符合题意的结果在什么地方出现（可能在叶子结点，也可能在中间的结点）；
            3、完成以上两步以后，就要编写代码实现上述分析的过程，使用代码在画出的树形结构上搜索符合题意的结果。
            
        三、画图以后，可以分析出的结论：
            左右都有可以使用的括号数量，即严格大于 0 的时候，才产生分支；
            左边不受右边的限制，它只受自己的约束；
            右边除了自己的限制以外，还收到左边的限制，即：右边剩余可以使用的括号数量一定得在严格大于左边剩余的数量的时候，才可以“节外生枝”；
            在左边和右边剩余的括号数都等于 0 的时候结算。
        """

        # 回溯法
        if n == 0:
            return []
        # 执行深度优先遍历，搜索可能的结果
        res = self.dfs(curStr="", left=n, right=n, res=[])
        return res

    def dfs_plus(self, curStr, left, right, n, res):
        """
        :param curStr: 当前递归得到的结果
        :param left: 左括号还有几个没有用掉
        :param right: 右边的括号还有几个没有用掉
        :param res: 结果集
        :return:
        """
        # 因为是递归函数，所以先写递归终止条件
        # 左右括号数量均为n，终止，开始结算
        if left == n and right == n:
            res.append(curStr)
            return res

        # 因为每一次尝试，都使用新的字符串变量，所以没有显式的回溯过程
        # 在递归终止的时候，直接把它添加到结果集即可，与「力扣」第 46 题、第 39 题区分
        # 如果左边还有剩余，继续递归下去
        if left < n:
            # 拼接上一个左括号，并且剩余的左括号个数减 1
            self.dfs_plus(curStr=curStr + "(", left=left + 1, right=right, n=n, res=res)

        # 什么时候可以用右边？例如，(((((()，此时 left < right，
        # 不能用等号，因为只有先拼了左括号，才能拼上右括号
        if right < n and left > right:
            # 拼接上一个右括号，并且剩余的右括号个数减 1
            self.dfs_plus(curStr=curStr + ")", left=left, right=right + 1, n=n, res=res)
        return res

    def generateParenthesis(self, n: int):
        """
        n对括号的所有合法组合
        :param n: 括号对数
        :return: 所有合法的组合列表
        """
        """
        三、画图以后，可以分析出的结论：
            左右都有可以使用的括号数量，即严格小于 n 的时候，才产生分支；
            左边不受右边的限制，它只受自己的约束；
            右边除了自己的限制以外，还收到左边的限制，即：右边剩余可以使用的括号数量一定得在严格小于左边剩余的数量的时候，才可以“节外生枝”；
            在左边和右边剩余的括号数都等于 n 的时候结算。
        """

        # 回溯法：做加法
        if n == 0:
            return []
        # 执行深度优先遍历，搜索可能的结果
        res = self.dfs_plus(curStr="", left=0, right=0, n=n, res=[])
        return res


@fn_timer
def main():
    pass


if __name__ == '__main__':
    main()
