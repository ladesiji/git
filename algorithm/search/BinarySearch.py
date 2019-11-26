#!/usr/bin/python3
# -*- encoding=utf-8 -*-

"""
    实现二分查找功能
"""

def BinarySearch(list, value):

    low = 0
    high = len(list)-1
    while low <= high:
        middle = (low + high)//2
        if list[middle] > value:
            high = middle - 1
        else:
            low = middle + 1
    return low

list = [1,2,3,3,5,6,7,8,9,10]

print(BinarySearch(list,4))