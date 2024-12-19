"""
@author grtsinry43
@date 2024/12/19 09:21
@description 热爱可抵岁月漫长
"""

class SortBaseClass:
    @staticmethod
    def heap_sort(arr: list):
        """
        堆排序
        :param arr: 待排序的列表
        :return: 排序后的列表
        """

        def heapify(start: int, end: int):
            root = start
            while True:
                child = 2 * root + 1
                if child > end:
                    break
                if child + 1 <= end and arr[child] < arr[child + 1]:
                    child += 1
                if arr[root] < arr[child]:
                    arr[root], arr[child] = arr[child], arr[root]
                    root = child
                else:
                    break

        for start in range(len(arr) // 2 - 1, -1, -1):
            heapify(start, len(arr) - 1)

        for end in range(len(arr) - 1, 0, -1):
            arr[0], arr[end] = arr[end], arr[0]
            heapify(0, end - 1)

        return arr


class SortClassImpl(SortBaseClass):
    @staticmethod
    def bubble_sort(arr: list):
        """
        冒泡排序
        :param arr: 待排序的列表
        :return: 排序后的列表
        """
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class SortClassImplFinal(SortClassImpl):
    @staticmethod
    def quick_sort(arr: list):
        """
        快速排序
        :param arr: 待排序的列表
        :return: 排序后的列表
        """
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return SortClassImplFinal.quick_sort(left) + middle + SortClassImplFinal.quick_sort(right)
