"""
问题描述：给定一棵二叉树的头结点head,分别实现按层打印和ZigZag打印二叉树的函数。例如，二叉树为：
head = Node(1)
head.left = Node(2)
head.right = Node(3)
head.left.left = Node(4)
head.right.left = Node(5)
head.right.right = Node(6)
head.right.left.left = Node(7)
head.right.left.right = Node(8)

按层打印时，输出格式为：
Level 1: 1
Level 2: 2 3
Level 3: 4 5 6
Level 4: 7 8

ZigZag打印时，输出格式为：
Level 1: 1
Level 2: 3 2
Level 3: 4 5 6
Level 4: 8 7

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class PrintZigzag:
    #层次遍历的思想，按层打印二叉树
    @classmethod
    def print_by_level(cls, root):
        if root is None:
            return None
        last = root #每层的最后一个打印结点
        nlast = None #用于在打印时找到最后一个节点的变量

        queue = [root]
        level = 1 #指示层数
        print('level {}'.format(level), end=':')
        while queue:
            cur = queue.pop(0)
            print(cur.value, end=' ')

            if cur.left:
                queue.append(cur.left)
                nlast = cur.left
            if cur.right:
                queue.append(cur.right)
                nlast = cur.right
            if (cur == last) and queue:
                print()
                level += 1
                print('level {}'.format(level), end=':')
                last = nlast # 更新下一层的最后一个打印结点

    # 按之字形打印，奇数层从左到右，偶数层从右到左
    @classmethod
    def print_by_zigzag(cls, root):
        if root is None:
            return

        flag = True # 标志奇数层 或 偶数层
        queue = [root] #使用链表实现双端队列
        last = root
        nlast = None
        level = 1
        print('Level {}'.format(level), end=':')

        while queue:
            # 奇数层 左-右
            if flag:
                # 奇数层 头部进 头部出元素
                cur = queue.pop(0)
                # 偶数层 按照先左后右进入
                if cur.left:
                    queue.append(cur.left) #偶数层的 尾部进 尾部出
                    if nlast is None:
                        nlast = cur.left
                if cur.right:
                    queue.append(cur.right) #偶数层的 尾部进 尾部出
                    if nlast is None:
                        nlast = cur.right
            # 偶数层
            else:
                cur = queue.pop() #偶数层的 尾部进 尾部出
                # 奇数层 按照先右后左进入
                if cur.right is not None:
                    queue.insert(0, cur.right)
                    if nlast is None:
                        nlast = cur.right
                if cur.left is not None:
                    queue.insert(0, cur.left)
                    if nlast is None:
                        nlast = cur.left
            print(cur.value, end=' ')

            if last == cur and len(queue) > 0:
                last = nlast #更新下一层的last结点
                nlast = None
                flag = not flag #切换层数
                level += 1
                print()
                print('Level {}'.format(level), end=':')



if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.right.left = Node(5)
    head.right.right = Node(6)
    head.right.left.left = Node(7)
    head.right.left.right = Node(8)

    PrintZigzag.print_by_level(head)
    print()
    print()
    PrintZigzag.print_by_zigzag(head)