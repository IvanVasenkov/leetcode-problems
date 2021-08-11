# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Необходимо просуммировать два значения, представленных в виде однонаправленных списков.
Все значения указаны задом наперед, верунть ответ нужно также
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Сложность по времени  O(n)
        Просто реализуем метод сложения как учат складывать в столбик в школе
        """
        res = ListNode()
        head = res
        owerflow = 0
        while l1 or l2 or owerflow:
            if l1:
                first_part = l1.val
                l1 = l1.next
            else:
                first_part = 0
            if l2:
                second_part = l2.val
                l2 = l2.next
            else:
                second_part = 0
            digit_sum = first_part + second_part + owerflow
            if digit_sum > 9:
                owerflow = 1
                head.next = ListNode(digit_sum%10)
            else:
                owerflow = 0
                head.next = ListNode(digit_sum)
            head = head.next
        return res.next