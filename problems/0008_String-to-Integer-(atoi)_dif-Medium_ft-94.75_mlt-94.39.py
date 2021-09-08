"""
Необходимо преобразовать строку в инт аналогично функции atoi в C.
"""

class Solution:

    #Постарался сделать без функции int(), а с помощью математики

    def myAtoi(self, s: str) -> int:
        #По умолчанию знак +
        sign = True

        #Уберем пробелы
        s = s.strip()

        #Проверка на то, осталось ли вообще число
        if s == "": return 0

        #Проставляем знак
        if s[0] == '-': 
            sign = False
            s = s[1:]
        elif s[0] == "+": 
            s = s[1:]

        #Из строки берем только цифры что идкт в начале
        digits = ""
        for n in s:
            if n >= '0' and n <= '9':
                digits +=n
            else:
                break
        
        #Переменная для формирования и вывода ответа
        ans = 0

        #С конца прибавляем соответственно степеням 10
        for i in range(len(digits)):
            ans += int(digits[-i-1])*10**i
        
        #Проставляем знак
        if not sign : ans *= -1

        #Выполняем проверки на int
        if ans < -2**31 : return -2**31
        if ans > 2**31 - 1: return 2**31 - 1
        return(ans)