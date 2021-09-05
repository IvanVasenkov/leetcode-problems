"""
Дано два массива, надо найти медиану массива, который получится если их объединить и отсотртировать.
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        Сложность по времени - O(n)
        """

        #Медиана в отсотрированном массиве равна среднему элементу, если количество элементов нечетное,
        #а если четное, то сумме средних элементов пополам
        def find_median(l):
            if len(l)%2 == 0:
                return (l[len(l)//2] + l[len(l)//2 - 1])/2.0
            else:
                return l[len(l)//2]
                
        #Для того, чтобы после слияния элементы остались отсортированными используем слияние как в merge sort
        def merge(nums1, nums2):
            c1 = 0
            c2 = 0
            merged = []
            while 1:
                if c1 == len(nums1):
                    merged += nums2[c2:]
                    break
                elif c2 == len(nums2):
                    merged += nums1[c1:]
                    break
                else:
                    if nums1[c1] > nums2[c2]:
                        merged.append(nums2[c2])
                        c2 += 1
                    else:
                        merged.append(nums1[c1])
                        c1 += 1
            return merged
            
                
        if len(nums1) == 0:
            return find_median(nums2)
        elif len(nums2) == 0:
            return find_median(nums1)
        else:
            merged_ans = merge(nums1, nums2)
            return find_median(merged_ans)