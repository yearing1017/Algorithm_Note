# LeetCode
- 此文用来记录自己在leetcode上的simple题集解决方案。
- 希望能够鞭策自己每天刷一道题，日积月累，即使是simple型。

## 1. 两数之和

- 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

- 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

  > 示例:
  >
  > 给定 nums = [2, 7, 11, 15], target = 9
  >
  > 因为 nums[0] + nums[1] = 2 + 7 = 9
  > 所以返回 [0, 1]

- **思路：两个for循环暴力**

```
int* twoSum(int* nums, int numsSize, int target) {
  static int a[2]={0};
  for (int i = 0; i < numsSize - 1; i++)
  {
    for (int j = i+1; j < numsSize; j++)
    {
      if (nums[i] + nums[j] == target)
      {
        a[0] = i;
        a[1] = j;
        return a;
      }
    }
  }
  return 0;
}
```

## 7. 整数反转

- **题目描述**

  - 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

  > 输入: 123
  > 输出: 321
  >
  > 输入: -123
  > 输出: -321
  >
  > 输入: 120
  > 输出: 21

  - 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

- 通过循环将数字x的每一位拆开，在计算新值时每一步都判断是否溢出。

  - 溢出条件有两个，**一个是大于整数最大值MAX_VALUE，另一个是小于整数最小值MIN_VALUE，**设当前计算结果为ans，下一位为pop。

  - **从ans * 10 + pop > MAX_VALUE这个溢出条件来看:**
    当出现 ans > MAX_VALUE / 10 且 还有pop需要添加 时，则一定溢出;
    当出现 ans == MAX_VALUE / 10 且 pop > 7 时，则一定溢出，7是2^31 - 1的个位数;

    **不知道最后一位是7可以这样思考：`pop > Integer.MAX_VALUE%10`**

  - **从ans * 10 + pop < MIN_VALUE这个溢出条件来看:**
    当出现 ans < MIN_VALUE / 10 且 还有pop需要添加 时，则一定溢出
    当出现 ans == MIN_VALUE / 10 且 pop < -8 时，则一定溢出，8是-2^31的个位数

  - **不知道最后一位是-8可以这样思考：`pop < Integer.MIN_VALUE%10`**

```java
class Solution {
    public int reverse(int x) {
         int res = 0;
         while(x!=0){
             int pop = x%10;
             if(res > Integer.MAX_VALUE/10 || (res==Integer.MAX_VALUE/10 && pop > Integer.MAX_VALUE%10))
                 return 0;
             if(res < Integer.MIN_VALUE/10 || (res==Integer.MIN_VALUE/10 && pop < Integer.MIN_VALUE%10))
                 return 0;
             res = res*10 + pop;
             x /=10;
         }
        return res;
    }
}
```

## 9. 回文数

- 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

> 示例 1:
> 输入: 121
> 输出: true
>
> 示例 2:
> 输入: -121
> 输出: false
> 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
>
> 示例 3:
> 输入: 10
> 输出: false
> 解释: 从右向左读, 为 01 。因此它不是一个回文数。

- **进阶:**

  你能不将整数转为字符串来解决这个问题吗？

- 代码如下：

```java
class Solution {
    public boolean isPalindrome(int x) {
        int sum = 0;
        int temp = x;
        if(x<0){
            return false;
        }
        if(x==0){
            return true;
        }
        else{
            while(x!=0){
                int a = x%10;
                sum = sum *10 + a;
                x/=10;
            }
            return sum==temp;
        }
    }
}
```

## 13. 罗马数字转数字

- 罗马数字包含以下七种字符: `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

> 字符          数值
> I             1
> V             5
> X             10
> L             50
> C             100
> D             500
> M             1000

- 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 

- 通常情况下，罗马数字中小的数字在大的数字的右边。但也
- 存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
  - I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
  - X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
  - C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

- 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

> 示例 1:
>
> 输入: "III"
> 输出: 3
> 示例 2:
>
> 输入: "IV"
> 输出: 4
> 示例 3:
>
> 输入: "IX"
> 输出: 9
> 示例 4:
>
> 输入: "LVIII"
> 输出: 58
> 解释: L = 50, V= 5, III = 3.
> 示例 5:
>
> 输入: "MCMXCIV"
> 输出: 1994
> 解释: M = 1000, CM = 900, XC = 90, IV = 4.

- **思路：**
  - 从一开始判断num（后面的）是否比prenum（前面的）小，如果小，证明要加prenum。
  - 如果大，则要减去prenum，num和prenum移动位置。一直到最后一个数。
  - 最后的prenum肯定要加上。

- 代码：

```java
class Solution {
    public int romanToInt(String s) {
        int sum = 0;
        int prenum = Solution.getValue(s.charAt(0));
        for(int i=1; i<s.length(); i++){
            int num = Solution.getValue(s.charAt(i));
            if(num < prenum || num == prenum){
                sum += prenum;
            }
            else{
                sum -= prenum;
            }
            prenum = num;
        }
        sum = sum + prenum;
        return sum;
    }
    public static int getValue(char a){
        switch(a) {
            case 'I': return 1;
            case 'V': return 5;
            case 'X': return 10;
            case 'L': return 50;
            case 'C': return 100;
            case 'D': return 500;
            case 'M': return 1000;
            default: return 0;
        }
    }
}
```

## 14. 最长公共前缀

- 编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 `""`。

> 示例 1:
>
> 输入: ["flower","flow","flight"]
> 输出: "fl"
> 示例 2:
>
> 输入: ["dog","racecar","car"]
> 输出: ""
> 解释: 输入不存在公共前缀。

- **说明:** 所有输入只包含小写字母 `a-z` 。

- **自己的思路，有点麻烦，最终结果是：**

> 执行用时 :1 ms, 在所有 java 提交中击败了93.91%的用户
>
> 内存消耗 :37.8 MB, 在所有 java 提交中击败了71.58%的用户

- **记录一下自己的思路：**
  - 首先排除一些最容易想到的特例：
  - 如果没有字符串，则返回空；
  - 如果只有一个字符串，则返回第一个字符串；
  - 遍历所有的字符串，找出最短的字符串，首先设定strs[0]是最短的，再往下依次取代；
  - 遍历过程中，若发现有一个空串，则返回空；
  - 找到最短字符串之后，将其余的串一个字符一个字符与之比较，找一个最短的长度。
  - 一开始设定min_num很大，如果找不到j来代替这个值，说明字符串都相等。
  - 最后一步就是根据上述两种情况进行截取。
- 代码：

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
         if(strs.length == 0){
             return "";
         }
         if(strs.length == 1){
             return strs[0];
         }
         int min_length = strs[0].length();
         int flag = 0;//标记最短串的位置
         int min_num = Integer.MAX_VALUE; //记录最短的相同串的长度
         //循环遍历出最短字符串
         for(int i=0; i<strs.length; i++){
             if(strs[i].length()==0){
                 return "";
             }
             if(strs[i].length() < min_length){
                 min_length = strs[i].length();
                 flag = i;
             }
             else{
                 continue;
             }
         }
         //对每个字符串与strs[flag]相比较
         for(int i=0; i<strs.length; i++){
             if(flag==i){
                 continue;
             }
             for(int j=0;j<min_length;j++){
                 if(strs[flag].charAt(j)!=strs[i].charAt(j)){
                     if(j<min_num){
                         min_num = j;
                     }
                 }
             }
         }
         if(min_num != Integer.MAX_VALUE){
             return strs[flag].substring(0,min_num);
         }else{
             return strs[flag];
         }
    }
}
```

- **官方题解：**

```java
public String longestCommonPrefix(String[] strs) {
   if (strs.length == 0) return "";
   String prefix = strs[0];
   for (int i = 1; i < strs.length; i++)
       while (strs[i].indexOf(prefix) != 0) {
           prefix = prefix.substring(0, prefix.length() - 1);
           if (prefix.isEmpty()) return "";
       }        
   return prefix;
}
```

## 20. 有效的括号

- 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
- 有效字符串需满足：
  - 左括号必须用相同类型的右括号闭合。
  - 左括号必须以正确的顺序闭合。
  - 注意空字符串可被认为是有效字符串。

> 示例 1:
>
> 输入: "()"
> 输出: true
> 示例 2:
>
> 输入: "()[]{}"
> 输出: true
> 示例 3:
>
> 输入: "(]"
> 输出: false
> 示例 4:
>
> 输入: "([)]"
> 输出: false
> 示例 5:
>
> 输入: "{[]}"
> 输出: true

- **思路记录：栈的典型应用**
  - 首先要把对应的括号进行匹配，python可用字典，java这里用的是hashmap。
  - 从开始遍历字符串，将字符串转换为字符数组，对每个字符进行判断：
  - 若为左边的起始括号，例如"("、"["、"{"，直接push进栈；
  - 若为右边的结束括号，则要进行判断，若栈为空，则直接返回false，因为栈里面没有与之匹配的元素了
  - 若栈不空，但是取出top元素，不与对应的map中的值对应，则不匹配，返回false；
  - 注意上面一步，已经取出了栈顶元素，匹配则返回true，不匹配则返回false，所以在遍历完：
  - 有两种情况：1.偶数，遍历完且匹配成功，栈空；2.奇数，栈不空，但是有不匹配的；
  - 所以此时返回stack.isEmpty();对应上面的两种情况。
- **代码：**

```java
class Solution {
    public boolean isValid(String s) {
        int len = s.length();
        if(len == 0){
            return true;
        }
        //HashMap 键值对
        HashMap<Character,Character> map = new HashMap();
        map.put(')','(');
        map.put(']','[');
        map.put('}','{');

        Stack<Character> stack = new Stack();

        for(char ch: s.toCharArray()){
            if(ch=='('||ch=='['||ch=='{'){
                stack.push(ch);
            }

            if((ch==')'||ch==']'||ch=='}') &&(stack.isEmpty() || stack.pop()!=map.get(ch))){
                return false;
            }
        }
        return stack.isEmpty();
    }
}
```

## 21. 合并两个有序链表

- 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

> 示例：
>
> 输入：1->2->4, 1->3->4
> 输出：1->1->2->3->4->4

- **思路解析：**
  - 创建了一个新的结点，根据比较两个链表元素的大小进行插入到新的结点之后。
  - 谁小谁就链接到后面，且新建的p结点和l1、l2结点的指针都向后移动。
  - 如果有一条链表到头了，那就将新的p结点指针指向没空的另一条链表剩余元素。
- **代码：**

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1 == null){
            return l2;
        }
        if(l2 == null){
            return l1;
        }
        ListNode p = new ListNode(0);
        ListNode head = p;//存下来p的位置，后面要移动
        while(l1!=null && l2!=null){
            if(l1.val<=l2.val){
                p.next = l1;
                p = p.next;
                l1 = l1.next;
            }else{
                p.next = l2;
                p = p.next;
                l2 = l2.next;
            }
        }
        if(l1==null){
            p.next = l2;
        }else{
            p.next = l1;
        }

        return head.next;
    }
}
```

## 26. 删除排序数组中的重复项

- 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

> 示例 1:
>
> 给定数组 nums = [1,1,2], 
>
> 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
>
> 你不需要考虑数组中超出新长度后面的元素。
> 示例 2:
>
> 给定 nums = [0,0,1,1,1,2,2,3,3,4],
>
> 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
>
> 你不需要考虑数组中超出新长度后面的元素。

- **思路分析：**
  - 两个指针i和j，从头开始遍历，j首先固定不变，i在变化，直到找到不相等的元素；
  - 因为已经是排好序的数组，所以肯定相等的元素都相邻；
  - 找到不相等的元素，使i对应的该元素赋值到之前的相等的某个元素上，那个元素就是相等的第2个。
  - 例如：1，1，2就将2赋给第二个1。1，1，1，2就将2赋给第二个1。
  - 最后j的位置就在不重复的倒数第二个位置，所以返回j+1。
- **代码：**

```python
class Solution {
    public int removeDuplicates(int[] nums) {
        int j=0;
        for(int i=0; i<nums.length; i++){
            if(nums[i] != nums[j]){
                j = j+1;
                nums[j] = nums[i];
            }
        }
        return j+1;
    }
}
```

## 27. 移除元素

- 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
- 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
- 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

> 示例 1:
>
> 给定 nums = [3,2,2,3], val = 3,
>
> 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
>
> 你不需要考虑数组中超出新长度后面的元素。
> 示例 2:
>
> 给定 nums = [0,1,2,2,3,0,4,2], val = 2,
>
> 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
>
> 注意这五个元素可为任意顺序。
>
> 你不需要考虑数组中超出新长度后面的元素。

- **思路分析**
  - 遍历数组nums，每次取出的数字变量为num，同时设置一个下标ans
  - 在遍历过程中如果出现数字与需要移除的值不相同时，则进行拷贝覆盖nums[ans] = num，ans自增1
  - 如果相同的时候，则跳过该数字不进行拷贝覆盖，最后ans即为新的数组长度
  - 这种思路在移除元素较多时更适合使用，最极端的情况是全部元素都需要移除，遍历一遍结束

- **代码**

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int loc = 0;
        for(int num: nums){
            if(num!= val){
                nums[loc] = num;
                loc++;
            }
        }
        return loc;
    }
}

```

### 35. 搜索插入位置

- 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
- 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。你可以假设数组中无重复元素。

> 示例 1:
>
> 输入: [1,3,5,6], 5
> 输出: 2
> 示例 2:
>
> 输入: [1,3,5,6], 2
> 输出: 1
> 示例 3:
>
> 输入: [1,3,5,6], 7
> 输出: 4
> 示例 4:
>
> 输入: [1,3,5,6], 0
> 输出: 0

- 思路：
  - 首先排除两个边界，对极限情况进行考虑
  - 其次考虑中间有大于等于，就返回该索引位置
- 代码如下：

```java
class Solution {
    public int searchInsert(int[] nums, int target) {
        int loc = 0;
        if(nums[0]>target){
            return 0;
        }
        if(nums[nums.length-1]<target){
            return nums.length;
        }
        for(int i=0; i< nums.length; i++){
            if(nums[i] >= target){
                loc = i;
                break;
            }
        }
        return loc;
    }
}

```
## 38. 报数

- 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

> 1. 1
>
> 2. 11
>
> 3. 21
>
> 4. 1211
>
> 5. 111221
>
>    
>
>    1 被读作  "one 1"  ("一个一") , 即 11。
>    11 被读作 "two 1s" ("两个一"）, 即 21。
>    21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
>
> 
>
> 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
>
> 注意：整数顺序将表示为一个字符串。
>
>  示例 1:
>
> 输入: 1
> 输出: "1"
>
> 示例 2:
>
> 输入: 4
> 输出: "1211"

- **解题思路**
  - 函数从str='1'开始向后求
  - 使用两个循环，外层循环控制求到第几个数，内存循环求该数
  - 函数中取pre和j两个元素，相当于使用两个指针来判断前面的和后面相邻的是否相等
  - 相等则计数++，计算出有多少该元素，添加count+字符
  - 若不相等，则直接添加1+该字符，并且挪动pre至后方元素，j也随之挪动，count恢复为1
  - 外层每次结束一次循环，求得第n个数
- **代码**

```java
class Solution {
    public String countAndSay(int n) {
        String str = "1";
        for (int i = 2; i <= n; i++) {
            StringBuilder builder = new StringBuilder();
            char pre = str.charAt(0);
            int count = 1;
            for (int j = 1; j < str.length(); j++) {
                char c = str.charAt(j);
                if (c == pre) {
                    count++;
                } else {
                    builder.append(count).append(pre);
                    pre = c;
                    count = 1;
                }
            }
            builder.append(count).append(pre);
            str = builder.toString();
        }
        return str;
    }
}
```

## 53. 最大子序和

- 给定整数数组 `nums` ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

  > 示例:
  >
  > 输入: [-2,1,-3,4,-1,2,1,-5,4],
  > 输出: 6
  > 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

- **解题思路：**
  - 定义一个局部临时sum，初始赋值为0，用来存储当前的局部子序和
  - 定义结果res，初始赋值为nums[0]
  - 因为数组中有正负数，所以要去判断临时sum的大小
  - 若sum>0，说明无论后面的数正负，都要加该数
  - 但是如果当前sum<0，就要舍弃sum，因为会减小后面继续加和。
  - 舍弃sum，就要将当前的sum赋值循环中的num，继续从此数开始加和

- 代码

```java
class Solution {
    public int maxSubArray(int[] nums) {
        int res = nums[0];
        int sum = 0;
        for(int num: nums){
            if(sum>0){
                sum += num;
            }else{
                sum = num;
            }
            res = Math.max(res, sum);
        }
        return res;
    }
}
```

- 更多详细解法：[最大子序和 c++实现四种解法 暴力法、动态规划、贪心法和分治法 图示讲解](https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-cshi-xian-si-chong-jie-fa-bao-li-f/)

## 58. 最后一个单词的长度

- 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
- 如果不存在最后一个单词，请返回 0 。
- 说明：一个单词是指由字母组成，但不包含任何空格的字符串。

> 示例:
>
> 输入: "Hello World"
> 输出: 5

- 解法一思路：
  - 从字符串末尾开始向前遍历，其中主要有两种情况：
  - **第一种情况**，以字符串"Hello World"为例，从后向前遍历直到遍历到头或者遇到空格为止，即为最后一个单词"World"的长度5；
  - **第二种情况**，以字符串"Hello World "为例，需要先将末尾的空格过滤掉，再进行第一种情况的操作，即认为最后一个单词为"World"，长度为5；
  - **所以完整过程为先从后过滤掉空格找到单词尾部，再从尾部向前遍历，找到单词头部，最后两者相减，即为单词的长度**。
  - 时间复杂度：O(n)，n为结尾空格和结尾单词总体长度。

- 代码：

```java
class Solution {
    public int lengthOfLastWord(String s) {
        int end = s.length() - 1;
        while(end >= 0 && s.charAt(end) == ' ') end--;
        if(end < 0) return 0;
        int start = end;
        while(start >= 0 && s.charAt(start) != ' ') start--;
        return end - start;
    }
}
```

- 解法二：
  - 首先使用`strim`函数去除首尾空格
  - 再使用Java的寻找最后一个空格位置函数，末尾-空格位置即单词长度
- 代码：

```java
class Solution {    
    public  int lengthOfLastWord(String s) {
    	//空串
    	s=s.trim();
    	if(s.length()==0){
    		return 0;
    	}
    	int lastEmptyIndex =s.lastIndexOf(" ");
        return s.length()-1-lastEmptyIndex;
    }
}
```
