#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 17:37
# @Author  : yeyuc
# @Email   : yeyucheng_uestc@163.com
# @File    : LongestValidParentheses.py
# @Software: PyCharm
"""
    __project_ = LeetCode
    __file_name__ = LongestValidParentheses
    __author__ = yeyuc
    __time__ = 2019/12/11 17:37
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
    def longestValidParentheses3(self, s: str) -> int:
        """
        算法：动态规划
        1、思路：
            1) 我们定义一个}dp 数组，其中第 i 个元素表示以下标为 i 的字符结尾的最长有效子字符串的长度。我们将 dp 数组全部初始化为 0 。
        很明显有效的子字符串一定以‘)’ 结尾。这进一步可以得出结论：以 ‘(’ 结尾的子字符串对应的 dp 数组位置上的值必定为 0 。所以只需要更新‘)’ 在 dp 数组中对应位置的值。
            2) 为了求出 dp 数组，我们每两个字符检查一次，如果满足如下条件
                （1）s[i]=‘)’ 且 s[i−1]=‘(’ ，也就是字符串形如``……()"，我们可以推出：dp[i]=dp[i−2]+2
                我们可以进行这样的转移，是因为结束部分的 "()" 是一个有效子字符串，并且将之前有效子字符串的长度增加了 2 。

                （2）s[i]=‘)’ 且 s[i−1]=‘)’，也就是字符串形如 ``.......))"，我们可以推出：如果 s[i−dp[i−1]−1]=‘(’ ，那么：dp[i]=dp[i−1]+dp[i−dp[i−1]−2]+2
                这背后的原因是如果倒数第二个 ‘)’ 是一个有效子字符串的一部分（记为 sub_s），对于最后一个‘)’ ，如果它是一个更长子字符串的一部分，那么它一定有一个对应的‘(’ ，
                它的位置在倒数第二个‘)’ 所在的有效子字符串的前面（sub_s）。因此，如果子字符串 subs的前面恰好是‘(’ ，那么我们就用 2 加上 subs的长度（dp[i−1]）去更新 dp[i]。
                除此以外，我们也会把有效子字符串"(,sub_s,)"之前的有效子字符串的长度也加上，也就是加上 dp[i−dp[i−1]−2] 。

                注： i - dp[i - 1] - 1 （前一个合法序列的前边一个位置），所以，s[i−dp[i−1]−1]=‘(’时，天然+2， 若再往前一步dp[i−dp[i−1]−2]也合法，叠加！
        """

        length = len(s)
        if length in [0, 1]:
            return 0

        dp = [0] * length
        max = 0
        for i in range(1, length):
            if s[i] == ')' and s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2
            elif s[i] == ')' and s[i - 1] == ')':
                if s[i - dp[i - 1] - 1] == '(' and i - dp[i - 1] - 1 >= 0:
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
            if dp[i] > max:
                max = dp[i]
        return max

    def longestValidParentheses4(self, s: str) -> int:
        """
        算法：使用栈，思路一找出匹配位置再排序找连续的最大长度
        """

        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res

    def longestValidParentheses5(self, s: str) -> int:
        """
        算法：两边夹逼 + 直观法
            时间复杂度：O(n)
            空间复杂度：O(1)
            一个有效的括号字符串形如：'()'、'(())'、'()()'，无非就是这三种
            反过来形如：'(()'、'())'、'('、')'整体上就是无效的
            设置left、right两个变量
            从左到右遍历
            遇到'('，left++
            遇到')'，right++
            当left == right 时，就属于有效括号组合内
            当right > left 时，就属于无效括号组合内
            如'())'
            并且初始化left = right = 0，继续向右遍历
            以上循环后，重置left = right = 0
            同理继续从右到左遍历
        """

        if not s:
            return 0
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res

    #####尝试中的解法#####
    def longestValidParentheses(self, s: str) -> int:
        """
        算法：两边夹逼 + 直观法
            时间复杂度：O(n)
            空间复杂度：O(1)
            一个有效的括号字符串形如：'()'、'(())'、'()()'，无非就是这三种
            反过来形如：'(()'、'())'、'('、')'整体上就是无效的
            设置left、right两个变量
            从左到右遍历
            遇到'('，left++
            遇到')'，right++
            当left == right 时，就属于有效括号组合内
            当right > left 时，就属于无效括号组合内
            如'())'
            并且初始化left = right = 0，继续向右遍历
            以上循环后，重置left = right = 0
            同理继续从右到左遍历
        """

        if not s:
            return 0

        max = 0

        # 从左往右扫描
        left, right = 0, 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                right += 1
            if left < right:
                left, right = 0, 0
            elif left == right:
                max = max if max >= left * 2 else left * 2
        # 从右往左扫描
        left, right = 0, 0
        for i in s[::-1]:
            if i == '(':
                left += 1
            elif i == ')':
                right += 1
            if left > right:
                left, right = 0, 0
            elif left == right:
                max = max if max >= left * 2 else left * 2

        return max

    #####失败的尝试#####
    def longestValidParentheses1(self, s: str) -> int:
        """
        直接法：使用两个列表，一个作为栈
        失败："()(()"
        """
        # （0）空串返回True, 奇串返回False
        length = len(s)
        if length in [0, 1]:
            return 0

        stack = ['?']  # 栈 stack 为空： 此时 stack.pop() 操作会报错
        len1 = 0
        cur_len = 0
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                while True:
                    if stack.pop() == '(':
                        cur_len += 2
                    else:
                        if cur_len > len1:
                            len1 = cur_len
                        stack = ['?']
                        cur_len = 0
        if cur_len > len1:
            len1 = cur_len
        return len1

    def longestValidParentheses2(self, s: str) -> int:
        """
        算法：暴力破解：考虑给定字符串中每种可能的非空偶数长度子字符串，检查它是否是一个有效括号字符串序列。
            为了检查有效性，我们使用栈的方法。
            每当我们遇到一个‘(’ ，我们把它放在栈顶。对于遇到的每个‘)’ ，我们从栈中弹出一个‘(’ ，如果栈顶没有‘(’，或者遍历完整个子字符串后栈中仍然有元素，那么该子字符串是无效的。
            这种方法中，我们对每个偶数长度的子字符串都进行判断，并保存目前为止找到的最长的有效子字符串的长度。
        失败：长度过长时，运行超时
        """

        def isValid(s: str) -> bool:
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
            dict = {'(': ')', '[': ']', '{': '}', '?': '?'}
            for c in s:
                if c in dict:
                    stack.append(c)
                elif dict.get(stack.pop()) != c:
                    return False
            return len(stack) == 1

        length = len(s)
        if length in [0, 1]:
            return 0

        len1 = 0

        # 穷举所有可能的子字符串
        for i in range(2, length + 1, 2):  # i为所有可能的长度
            li = [s[j:j + i] for j in range(length - i + 1)]
            for j in li:
                if isValid(s=j):
                    len1 = i
                    break

        return len1


@fn_timer
def main():
    pass


if __name__ == '__main__':
    main()
