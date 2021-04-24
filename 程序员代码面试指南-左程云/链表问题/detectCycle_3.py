'''
输入两个链表，找出它们的第一个公共结点。
两个链表长度分别为L1+C、L2+C， C为公共部分的长度，按照楼主的做法： 
第一个人走了L1+C步后，回到第二个人起点走L2步；
第2个人走了L2+C步后，回到第一个人起点走L1步。 
当两个人走的步数都为L1+L2+C时就两个家伙就相爱了
'''
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        cur1 = pHead1
        cur2 = pHead2
        while cur1 != cur2:
            cur1 = cur1.next if cur1 else pHead2
            cur2 = cur2.next if cur2 else pHead1
        return cur1