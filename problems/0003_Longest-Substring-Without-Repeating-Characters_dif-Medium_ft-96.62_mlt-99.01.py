"""
Необходимо найти самую длинную последовательность, в которой нет повторяющихся букв
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Сложность по времени - O(n)
        """

        #Создаем словарь, в котором будем хранить встретившиеся буквы и их позицию в исходной строке
        #Выбран словарь потому, что в него можно всталять за и получать по ключу за константное время
        duplicated = dict()

        #Treshold будет хранить индекс элемента, на котором в последний раз завершилась последовательность 
        #неповторяющихся букв
        treshold = -1
        ans = 0
        
        for i in range(len(s)):

            #Если прошлое повторение буквы случилось раньше, чем treshold, то обновляем начало последовательности
            if duplicated.get(s[i],-1) > treshold: treshold = duplicated[s[i]]
            
            #Обновляем когда последний раз встретилась буква
            duplicated[s[i]] = i
            
            #Проверяем какой длины текущая последовательность и обновляем если стала больше
            if i - treshold > ans: ans = i - treshold
            
        return ans