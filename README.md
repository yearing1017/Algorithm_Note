# Algorithm_Note

⏰记录刷题算法笔记

## 📑 目录
* [⭐️ Leetcode_simple刷题笔记](#leetcode)
* [⚡️  剑指offer](#offer)
* [〽️ 数据结构](#data-structure)
* [📝 算法](#algorithm)

<a id="leetCode"></a>

## ⭐️ Leetcode_simple刷题笔记
- 笔记链接：[Leetcode简单题目笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md)
- 目前已解决题目列表：

|  id  |            题目            | 语言 |                           题解链接                           |
| :--: | :------------------------: | :--: | :----------------------------------------------------------: |
|  1   |          两数之和          | C++  | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  7   |          整数反转          | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  9   |           回文数           | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  13  |       罗马数字转数字       | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  14  |        最长公共前缀        | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  20  |         有效的括号         | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  21  |      合并两个有序链表      | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  26  |   删除排序数组中的重复项   | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  27  |          移除元素          | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  35  |        搜索插入位置        | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  38  |            报数            | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  53  |         最大子序和         | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  58  |     最后一个单词的长度     | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  66  |            加一            | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  67  |         二进制求和         | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  69  |         x的平方根          | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  70  |           爬楼梯           | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  83  |  删除排序链表中的重复元素  | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
|  88  |      合并两个有序数组      | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
| 100  |          相同的树          | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
| 101  |         对称二叉树         | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
| 107  |    二叉树的层次遍历 II     | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
| 108  | 将有序数组转换为二叉搜索树 | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |
| 110  |         平衡二叉树         | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/leetcode.md) |


<a id="offer"></a>
## ⚡️ 剑指offer
###  已刷简单题目列表：

|    id    |       题目       |   语言    |                           题解链接                           |
| :------: | :--------------: | :-------: | :----------------------------------------------------------: |
| 面试题03 | 数组中重复的数字 | C++、Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/%E5%89%91%E6%8C%87offer/%E9%9D%A2%E8%AF%95%E9%A2%9803.md) |
| 面试题04 | 二维数组中的查找 | Java | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/%E5%89%91%E6%8C%87offer/%E9%9D%A2%E8%AF%95%E9%A2%9804.md) |
| 面试题05 | 替换空格 | Java、Python | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/%E5%89%91%E6%8C%87offer/%E9%9D%A2%E8%AF%95%E9%A2%9805.md) |
| 面试题06 | 从尾到头打印链表 | C++、Python | [题解笔记](https://github.com/yearing1017/Algorithm_Note/blob/master/%E5%89%91%E6%8C%87offer/%E9%9D%A2%E8%AF%95%E9%A2%9806.md) |


<a id="data-structure"></a>
## 〽️ 数据结构

### 顺序结构

#### 顺序栈（Sequence Stack）

[SqStack.cpp](DataStructure/SqStack.cpp)

顺序栈数据结构和图片

```cpp
typedef struct {
	ElemType *elem;
	int top;
	int size;
	int increment;
} SqStack;
```

![](https://raw.githubusercontent.com/huihut/interview/master/images/SqStack.png)

#### 队列（Sequence Queue）

队列数据结构

```cpp
typedef struct {
	ElemType * elem;
	int front;
	int rear;
	int maxSize;
}SqQueue;
```

##### 非循环队列

非循环队列图片

![](https://raw.githubusercontent.com/huihut/interview/master/images/SqQueue.png)

`SqQueue.rear++`

##### 循环队列

循环队列图片

![](https://raw.githubusercontent.com/huihut/interview/master/images/SqLoopStack.png)

`SqQueue.rear = (SqQueue.rear + 1) % SqQueue.maxSize`

#### 顺序表（Sequence List）

[SqList.cpp](DataStructure/SqList.cpp)

顺序表数据结构和图片

```cpp
typedef struct {
	ElemType *elem;
	int length;
	int size;
	int increment;
} SqList;
```

![](https://raw.githubusercontent.com/huihut/interview/master/images/SqList.png)


### 链式结构

[LinkList.cpp](DataStructure/LinkList.cpp)

[LinkList_with_head.cpp](DataStructure/LinkList_with_head.cpp)

链式数据结构

```cpp
typedef struct LNode {
    ElemType data;
    struct LNode *next;
} LNode, *LinkList; 
```

#### 链队列（Link Queue）

链队列图片

![](https://raw.githubusercontent.com/huihut/interview/master/images/LinkQueue.png)

#### 线性表的链式表示

##### 单链表（Link List）

单链表图片

![](https://raw.githubusercontent.com/huihut/interview/master/images/LinkList.png)

##### 双向链表（Du-Link-List）

双向链表图片

![](https://raw.githubusercontent.com/huihut/interview/master/images/DuLinkList.png)

##### 循环链表（Cir-Link-List）

循环链表图片

![](https://raw.githubusercontent.com/huihut/interview/master/images/CirLinkList.png)

### 哈希表

[HashTable.cpp](DataStructure/HashTable.cpp)

#### 概念

哈希函数：`H(key): K -> D , key ∈ K`

#### 构造方法

* 直接定址法
* 除留余数法
* 数字分析法
* 折叠法
* 平方取中法

#### 冲突处理方法

* 链地址法：key 相同的用单链表链接
* 开放定址法
    * 线性探测法：key 相同 -> 放到 key 的下一个位置，`Hi = (H(key) + i) % m`
    * 二次探测法：key 相同 -> 放到 `Di = 1^2, -1^2, ..., ±（k)^2,(k<=m/2）`
    * 随机探测法：`H = (H(key) + 伪随机数) % m`

#### 线性探测的哈希表数据结构

线性探测的哈希表数据结构和图片

```cpp
typedef char KeyType;

typedef struct {
	KeyType key;
}RcdType;

typedef struct {
	RcdType *rcd;
	int size;
	int count;
	bool *tag;
}HashTable;
```

![](https://raw.githubusercontent.com/huihut/interview/master/images/HashTable.png)

### 递归

#### 概念

函数直接或间接地调用自身

#### 递归与分治

* 分治法
    * 问题的分解
    * 问题规模的分解
* 折半查找（递归）
* 归并排序（递归）
* 快速排序（递归）

#### 递归与迭代

* 迭代：反复利用变量旧值推出新值
* 折半查找（迭代）
* 归并排序（迭代）

#### 广义表

##### 头尾链表存储表示

广义表的头尾链表存储表示和图片

```cpp
// 广义表的头尾链表存储表示
typedef enum {ATOM, LIST} ElemTag;
// ATOM==0：原子，LIST==1：子表
typedef struct GLNode {
    ElemTag tag;
    // 公共部分，用于区分原子结点和表结点
    union {
        // 原子结点和表结点的联合部分
        AtomType atom;
        // atom 是原子结点的值域，AtomType 由用户定义
        struct {
            struct GLNode *hp, *tp;
        } ptr;
        // ptr 是表结点的指针域，prt.hp 和 ptr.tp 分别指向表头和表尾
    } a;
} *GList, GLNode;
```

![](https://raw.githubusercontent.com/huihut/interview/master/images/GeneralizedList1.png)

##### 扩展线性链表存储表示

扩展线性链表存储表示和图片

```cpp
// 广义表的扩展线性链表存储表示
typedef enum {ATOM, LIST} ElemTag;
// ATOM==0：原子，LIST==1：子表
typedef struct GLNode1 {
    ElemTag tag;
    // 公共部分，用于区分原子结点和表结点
    union {
        // 原子结点和表结点的联合部分
        AtomType atom; // 原子结点的值域
        struct GLNode1 *hp; // 表结点的表头指针
    } a;
    struct GLNode1 *tp;
    // 相当于线性链表的 next，指向下一个元素结点
} *GList1, GLNode1;
```

![](https://raw.githubusercontent.com/huihut/interview/master/images/GeneralizedList2.png)

### 二叉树

[BinaryTree.cpp](DataStructure/BinaryTree.cpp)

#### 性质

1. 非空二叉树第 i 层最多 2<sup>(i-1)</sup> 个结点 （i >= 1）
2. 深度为 k 的二叉树最多 2<sup>k</sup> - 1 个结点 （k >= 1）
3. 度为 0 的结点数为 n<sub>0</sub>，度为 2 的结点数为 n<sub>2</sub>，则 n<sub>0</sub> = n<sub>2</sub> + 1
4. 有 n 个结点的完全二叉树深度 k = ⌊ log<sub>2</sub>(n) ⌋ + 1 
5. 对于含 n 个结点的完全二叉树中编号为 i （1 <= i <= n） 的结点
    1. 若 i = 1，为根，否则双亲为 ⌊ i / 2 ⌋
    2. 若 2i > n，则 i 结点没有左孩子，否则孩子编号为 2i
    3. 若 2i + 1 > n，则 i 结点没有右孩子，否则孩子编号为 2i + 1

#### 存储结构

二叉树数据结构

```cpp
typedef struct BiTNode
{
    TElemType data;
    struct BiTNode *lchild, *rchild;
}BiTNode, *BiTree;
```

##### 顺序存储

二叉树顺序存储图片

![](https://raw.githubusercontent.com/huihut/interview/master/images/SqBinaryTree.png)

##### 链式存储

二叉树链式存储图片

![](https://raw.githubusercontent.com/huihut/interview/master/images/LinkBinaryTree.png)

#### 遍历方式

* 先序遍历
* 中序遍历
* 后续遍历
* 层次遍历

#### 分类

* 满二叉树
* 完全二叉树（堆）
    * 大顶堆：根 >= 左 && 根 >= 右
    * 小顶堆：根 <= 左 && 根 <= 右
* 二叉查找树（二叉排序树）：左 < 根 < 右
* 平衡二叉树（AVL树）：| 左子树树高 - 右子树树高 | <= 1
* 最小失衡树：平衡二叉树插入新结点导致失衡的子树：调整：
    * LL型：根的左孩子右旋
    * RR型：根的右孩子左旋
    * LR型：根的左孩子左旋，再右旋
    * RL型：右孩子的左子树，先右旋，再左旋

### 其他树及森林

#### 树的存储结构

* 双亲表示法
* 双亲孩子表示法
* 孩子兄弟表示法

#### 并查集

一种不相交的子集所构成的集合 S = {S1, S2, ..., Sn}

#### 平衡二叉树（AVL树）

##### 性质

* | 左子树树高 - 右子树树高 | <= 1
* 平衡二叉树必定是二叉搜索树，反之则不一定
* 最小二叉平衡树的节点的公式：`F(n)=F(n-1)+F(n-2)+1` （1 是根节点，F(n-1) 是左子树的节点数量，F(n-2) 是右子树的节点数量）

平衡二叉树图片

![](https://raw.githubusercontent.com/huihut/interview/master/images/Self-balancingBinarySearchTree.png)

##### 最小失衡树

平衡二叉树插入新结点导致失衡的子树

调整：

* LL 型：根的左孩子右旋
* RR 型：根的右孩子左旋
* LR 型：根的左孩子左旋，再右旋
* RL 型：右孩子的左子树，先右旋，再左旋

#### 红黑树

[RedBlackTree.cpp](DataStructure/RedBlackTree.cpp)

##### 红黑树的特征是什么？

1. 节点是红色或黑色。
2. 根是黑色。
3. 所有叶子都是黑色（叶子是 NIL 节点）。
4. 每个红色节点必须有两个黑色的子节点。（从每个叶子到根的所有路径上不能有两个连续的红色节点。）（新增节点的父节点必须相同）
5. 从任一节点到其每个叶子的所有简单路径都包含相同数目的黑色节点。（新增节点必须为红）

##### 调整

1. 变色
2. 左旋
3. 右旋

##### 应用

* 关联数组：如 STL 中的 map、set

##### 红黑树、B 树、B+ 树的区别？

* 红黑树的深度比较大，而 B 树和 B+ 树的深度则相对要小一些
* B+ 树则将数据都保存在叶子节点，同时通过链表的形式将他们连接在一起。

#### B 树（B-tree）、B+ 树（B+-tree）

B 树、B+ 树图片

![B 树（B-tree）、B+ 树（B+-tree）](https://i.stack.imgur.com/l6UyF.png)

##### 特点

* 一般化的二叉查找树（binary search tree）
* “矮胖”，内部（非叶子）节点可以拥有可变数量的子节点（数量范围预先定义好）

##### 应用

* 大部分文件系统、数据库系统都采用B树、B+树作为索引结构

##### 区别

* B+树中只有叶子节点会带有指向记录的指针（ROWID），而B树则所有节点都带有，在内部节点出现的索引项不会再出现在叶子节点中。
* B+树中所有叶子节点都是通过指针连接在一起，而B树不会。

##### B树的优点

对于在内部节点的数据，可直接得到，不必根据叶子节点来定位。

##### B+树的优点

* 非叶子节点不会带上 ROWID，这样，一个块中可以容纳更多的索引项，一是可以降低树的高度。二是一个内部节点可以定位更多的叶子节点。
* 叶子节点之间通过指针来连接，范围扫描将十分简单，而对于B树来说，则需要在叶子节点和内部节点不停的往返移动。

> B 树、B+ 树区别来自：[differences-between-b-trees-and-b-trees](https://stackoverflow.com/questions/870218/differences-between-b-trees-and-b-trees)、[B树和B+树的区别](https://www.cnblogs.com/ivictor/p/5849061.html)

#### 八叉树

八叉树图片

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Octree2.png/400px-Octree2.png)

八叉树（octree），或称八元树，是一种用于描述三维空间（划分空间）的树状数据结构。八叉树的每个节点表示一个正方体的体积元素，每个节点有八个子节点，这八个子节点所表示的体积元素加在一起就等于父节点的体积。一般中心点作为节点的分叉中心。

##### 用途

* 三维计算机图形
* 最邻近搜索


<a id="algorithm"></a>
## 📝 常用算法总结

### 排序

排序算法 | 平均时间复杂度 | 最差时间复杂度 | 空间复杂度 | 数据对象稳定性
---|---|---|---|---
[冒泡排序](Sort_Algorithm/BubbleSort.h) | O(n<sup>2</sup>)|O(n<sup>2</sup>)|O(1)|稳定
[选择排序](Sort_Algorithm/SelectionSort.h) | O(n<sup>2</sup>)|O(n<sup>2</sup>)|O(1)|数组不稳定、链表稳定
[插入排序](Sort_Algorithm/InsertSort.h) | O(n<sup>2</sup>)|O(n<sup>2</sup>)|O(1)|稳定
[快速排序](Sort_Algorithm/QuickSort.h) | O(n*log<sub>2</sub>n) |  O(n<sup>2</sup>) | O(log<sub>2</sub>n) | 不稳定
[堆排序](Sort_Algorithm/HeapSort.cpp) | O(n*log<sub>2</sub>n)|O(n*log<sub>2</sub>n)|O(1)|不稳定
[归并排序](Sort_Algorithm/MergeSort.h) | O(n*log<sub>2</sub>n) | O(n*log<sub>2</sub>n)|O(n)|稳定
[希尔排序](Sort_Algorithm/ShellSort.h) | O(n*log<sup>2</sup>n)|O(n<sup>2</sup>)|O(1)|不稳定
[计数排序](Sort_Algorithm/CountSort.cpp) | O(n+m)|O(n+m)|O(n+m)|稳定
[桶排序](Sort_Algorithm/BucketSort.cpp) | O(n)|O(n)|O(m)|稳定
[基数排序](Sort_Algorithm/RadixSort.h) | O(k*n)|O(n<sup>2</sup>)| |稳定

> * 均按从小到大排列
> * k：代表数值中的 “数位” 个数
> * n：代表数据规模
> * m：代表数据的最大值减最小值

### 排序算法解析
- [简单选择排序](http://yearing1017.cn/2019/06/05/%E5%85%AB%E5%A4%A7%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95-%E7%AE%80%E5%8D%95%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F/)
- [直接插入排序](http://yearing1017.cn/2019/05/30/%E5%85%AB%E5%A4%A7%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95-%E7%9B%B4%E6%8E%A5%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F/)
- [快速排序](http://yearing1017.cn/2019/05/31/%E5%85%AB%E5%A4%A7%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F/)
- [希尔排序](http://yearing1017.cn/2019/05/31/%E5%85%AB%E5%A4%A7%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95-%E5%B8%8C%E5%B0%94%E6%8E%92%E5%BA%8F/)
- [冒泡排序](https//yearing1017.cn/2019/05/29/%E5%85%AB%E5%A4%A7%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95-%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F/)
- [Dijkstra算法笔记](http://yearing1017.cn/2019/10/29/Dijkstra%E7%AE%97%E6%B3%95%E5%AE%9E%E7%8E%B0/)
  
  
## 💡 算法知识积累
- 学习算法必读系列
  - [学习算法和刷题的框架思维](https://github.com/yearing1017/Algorithm_Note/blob/master/fuck-algorithm/学习算法和数据结构的高效方法.md)
