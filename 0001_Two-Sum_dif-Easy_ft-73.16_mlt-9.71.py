"""
Необходимо найти индиексы элементов в массиве nums, сумма которых равна target
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Сложность O(n)

        Проходим по каждому элементу исходного списка и добавляем в словарь запись с ключом,
        равным разности текущего элемента и target, и индексом этого элемента.

        Когда значение очередного элемента встречается в ключах словаря,
        выводим индекс этого элемента и значение по ключу.

        """
        remain_values = {}
        
        for i in range(len(nums)):
            if nums[i] in remain_values:
                return [i, remain_values[nums[i]]]
            else:
                remain_values[target - nums[i]] = i