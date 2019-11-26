#!/usr/bin/python3
# -*- encoding=utf-8 -*-


import time
import random
import sys
sys.setrecursionlimit(10000)

"""
    冒泡排序，基于冒泡排序的 快速排序，梳排
"""


def main():
    array = []
    for i in range(100000):
        array.append(random.randint(1, 10000000))
    # array = list(set(array))
    array1 = array[:]
    array2 = array[:]
    array3 = array[:]

    # result1 = QuickSort(array1)
    # print("快速排序时间为：{:.5f}", result1)
    result2 = ShellSort(array2)
    print("希尔排序时间为：{:.5f} S".format(result2))
    result3 = q_s(array3)
    print("自快排序时间为：{:.5f} S".format(result3))


def q_s(array):
    tic = time.process_time()
    array.sort()
    toc = time.process_time()
    t = toc - tic
    return t


def BubbleSort(list):
    """
        冒泡排序的核心是交换相邻元素。
        大的向后，小的向前，外层一次循环可以确定一个元素位置
    """
    tic = time.process_time()
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    top = time.process_time()
    t = top - tic
    return t


def InsertSort(list):
    """
        直接插入排序
    """
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while j >= 0 and temp < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = temp
    return list


def QuickSort(list):
    """
        快速排序，基于冒泡排序的改进版。
        其核心思想是分而治之和迭代

    """
    tic = time.process_time()
    quick_sort(list, 0, len(list)-1)
    toc = time.process_time()
    t = toc - tic
    return t


def partition(list, start, end):
    """
        按基准值，将数据分割为前后两个部分，
        返回分割点下标
    """
    i, j = start, end
    base = list[i]
    while i < j:
        # 从后面开始，寻找比基准值小的j，如果值比基准值大，则前移一位
        while i < j and list[j] >= base:
            j -= 1
        # 将找到的比基准值小的值换到前半区
        list[i] = list[j]
        # 从前面开始，寻找比基准值大的i，如果值比基准值小，则前移一位
        while i < j and list[i] <= base:
            i += 1
        # 将找到的比基准值大的值换到后半区
        list[j] = list[i]
    list[i] = base

    return i


def quick_sort(list, start, end):
    """
        将排序列表分割迭代，分割后列表长度大于10，继续分割
        如果分割后长度小于10，则进行插入排序。
    """
    # 如果start >= end 直接返回
    if start >= end:
        return list
    if end - start < 20:
        InsertSort(list)
    else:
        index = partition(list, start, end)
        quick_sort(list, start, index-1)
        quick_sort(list, index+1, end)


def ShellSort(list):
    """
        希尔排序：直接插入排序的优化版
        直接插入排序中如果较小的数位置靠后，在往前插入的过程中需要一个一个比较，相对较慢
        希尔排序通过将全部元素分为几个区域来提升插入排序的性能。
        这样可以让一个元素可以一次性地朝最终位置前进一大步。
        然后算法再取越来越小的步长进行排序，
        算法的最后一步就是普通的插入排序，
        但是到了这步，需排序的数据几乎是已排好的了（此时插入排序较快）
    """
    tic = time.process_time()
    step = len(list) // 2
    while step > 0:
        for i in range(step, len(list)):
            temp = list[i]
            j = i - step
            while j >= 0 and temp < list[j]:
                list[j+step] = list[j]
                j -= step
            list[j+step] = temp
        step = step // 2
    toc = time.process_time()
    t = toc - tic
    return t


if __name__ == main():
    main()