"""
@author grtsinry43
@date 2024/12/19 07:58
@description 热爱可抵岁月漫长
"""

list1 = [1, 3, 5, 2, 8, 7, 4]

print("通过调用包")

from util.sort import heap_sort

print(heap_sort(list1))

from util.sort import bubble_sort

print(bubble_sort(list1))

from util.sort import quick_sort

print(quick_sort(list1))

print("通过调用类")

from class_util.SortBaseClass import SortClassImplFinal

print(SortClassImplFinal.heap_sort(list1))
print(SortClassImplFinal.bubble_sort(list1))
print(SortClassImplFinal.quick_sort(list1))
