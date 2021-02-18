# -*- coding:utf-8 -*-
# @author : MaLei 
# @datetime : 2021/1/21 2:23 下午
# @file : 2021-1-21.py
# @software : PyCharm

# 如果字符串满足以下条件之一，则可以称之为 有效括号字符串（valid parentheses string，可以简写为 VPS）：
#
#     字符串是一个空字符串 ""，或者是一个不为 "(" 或 ")" 的单字符。
#     字符串可以写为 AB（A 与 B 字符串连接），其中 A 和 B 都是 有效括号字符串 。
#     字符串可以写为 (A)，其中 A 是一个 有效括号字符串 。
#
# 类似地，可以定义任何有效括号字符串 S 的 嵌套深度 depth(S)：
#
#     depth("") = 0
#     depth(C) = 0，其中 C 是单个字符的字符串，且该字符不是 "(" 或者 ")"
#     depth(A + B) = max(depth(A), depth(B))，其中 A 和 B 都是 有效括号字符串
#     depth("(" + A + ")") = 1 + depth(A)，其中 A 是一个 有效括号字符串
#
# 例如：""、"()()"、"()(()())" 都是 有效括号字符串（嵌套深度分别为 0、1、2），而 ")(" 、"(()" 都不是 有效括号字符串 。
#
# 给你一个 有效括号字符串 s，返回该字符串的 s 嵌套深度 。
# s = "(1+(2*3)+((8)/4))+1"
# stack = []
# degree = 0
# for i in s:
#     if i=='(':
#         stack.append(i)
#     elif i==')':
#         degree=max(degree,len(stack))
#         stack.pop()
# print(degree)

# 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：
#
#     任何左括号 ( 必须有相应的右括号 )。
#     任何右括号 ) 必须有相应的左括号 ( 。
#     左括号 ( 必须在对应的右括号之前 )。
#     * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
#     一个空字符串也被视为有效字符串。
# s="(***((()*)))"
# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         # 记录最少，最多需要右括弧的数量
#         a=[0,0]
#         for i in s:
#             if i=='(':
#                 a[0]+=1
#                 a[1]+=1
#             elif i=='*':
#                 if a[0]:
#                     a[0]-=1
#                 a[1]+=1
#             else:
#                 if a[0]:
#                     a[0]-=1
#                 a[1]-=1
#             if a[1]<0:
#                 return False
#         return a[0]==0
#
#
# print(Solution().checkValidString(s))

# 给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，
# 其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj] 。
# 每个区间列表都是成对 不相交 的，并且 已经排序 。
# 返回这 两个区间列表的交集 。
#
# 形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b 。
#
# 两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。

# class Solution:
#     def intervalIntersection(self, firstList, secondList):
#         a=[]
#

# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。
# 请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# a=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target=5
#
# class Solution:
#     def findNumberIn2DArray(self, matrix, target) -> bool:
#         p_h,p_s=0,0
#         mid=[int(len(matrix[0])/2),int(len(matrix)/2)]
#
#
#
#
# print(Solution().findNumberIn2DArray(a,target))

class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


tree = TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5)), TreeNode(6)),
                TreeNode(0, TreeNode(0), TreeNode(0)))

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         dept1,dept2=0,0
#         if root:
#             if root.left:
#                 dept1+=self.maxDepth(root.left)+1
#             if root.right:
#                 dept2+=self.maxDepth(root.right)+1
#             if not root.left and not root.right:
#                 return 1
#         return max(dept1,dept2)
#
# class Solution2:
#     def maxDepth(self, root: TreeNode) -> int:
#         def test(nodes):
#             if nodes:
#                 return max(test(nodes.left),test(nodes.right))+1
#             else:
#                 return 0
#         return test(root)
#
#
#
# print(Solution().maxDepth(tree))

# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         left,right=0,0
#         if root:
#             if root.left:
#                 left+=self.minDepth(root.left)+1
#             if root.right:
#                 right+=self.minDepth(root.right)+1
#             if not root.left and root.right:
#                 return 1
#         if min(left,right)==0:
#             return max(left,right)
#         else:
#             return min(left,right)
# print(Solution().minDepth(tree))

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        root = pre[0]
        tree = TreeNode(root)
        for i in range(1, len(pre)):
            index_tin = tin.index(pre[i])
            index_root = tin.index(pre[i - 1])
            if index_tin < index_root:
                tree.left = TreeNode(pre[i])
            elif index_tin > index_root:
                tree.right = TreeNode(pre[i])
        return tree


Solution().reConstructBinaryTree(pre=[1,2,3,4,5,6,7],tin=[3,2,4,1,6,5,7])