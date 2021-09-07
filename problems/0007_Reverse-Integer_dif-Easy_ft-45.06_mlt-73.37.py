"""
Необходимо инт преобразовать в инт с цифрами в обратном порядке.
Если в итоге получается больше 32 битового инта со знаком, то вывести 0
Знак сохраняется, ппереворачиваются только цифры. 
"""

class Solution:
    
    #Реализовал решение в котором преобразуем инт к строке, переворачиваем строку и обратно в инт.

    def reverse(self, x: int) -> int:
        negative = False
        if x < 0: negative = True
        x = abs(x)
        x_str = str(x)
        if negative:
            ans_str = '-'
        else:
            ans_str = ''
        ans_str += x_str[::-1]
        ans = int(ans_str)
        if ans >= -2**31 and ans <= 2**31 - 1:
            return int(ans_str)
        else:
            return 0