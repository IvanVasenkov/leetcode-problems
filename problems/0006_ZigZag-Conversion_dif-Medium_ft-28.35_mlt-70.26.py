"""
Вывести с заданным количеством строк в виде зиг зага заданное слово
Например, для "PAYPALISHIRING" с количеством строк = 3

P   A   H   N
A P L S I I G
Y   I   R

Ответ должен содержать последовательно строчки без пробелов сверху вниз

Вывод:
"PAHNAPLSIIGYIR"
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Если посмотреть на строки, то можно догадаться, что элементы, входящие в строку,
        можно описать некой функцией.

        В итоге, понял что на самом деле описывется системой уравнений вида:
            r + 2*n*i

            -r + 2*n*i
        , где r - номер строки, n - количество строк, i - итерация (очерредной виток зиг зага)
        """

        def generate_string_members(num_iter, num_rows, row):
            
            #Для нулевой и последней строки достаточно одного уравнения r + 2*n*i
            #Генеруем не символы, а индексы элементов, на которых стоят буквы очередной строки в исходной строке
            if row == 0 or row == num_rows:
                return [row+2*num_rows*i for i in range(num_iter)]
            else:
                members = []
                for i in range(num_iter):

                    #Всегда сначала добавляется номер элемента из уравнеия, в котором положительное r
                    members.append(row+2*num_rows*i)

                    #Тут i + 1, потому, что отрицательные элементы точно не нужны, а если будет перебор, то отфильтруем в конце
                    members.append(-row+2*num_rows*(i + 1))
                    
            return members
        

        #Если необходимо вывести в одну строку, то просто выодим исходную строку
        if numRows == 1:
            return s
        else:
            ans = ''
            s_len = len(s)

            #подсчет необходимого количества итераций
            num_iter = s_len//(2*numRows - 2) + 1


            for i in range(numRows):
                for l in generate_string_members(num_iter , numRows - 1, i):

                    #Проверка на вхождение элемента в строку
                    if l > -1 and l < s_len:
                        ans += s[l]
        
            return ans