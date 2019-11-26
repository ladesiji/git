#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    直接插入排序法
"""

import time
import random
import sys

sys.setrecursionlimit(1000000) #这里设置为一百万

def main():
    """
        主函数
    """
    array = []
    for i in range(5000):
        array.append(random.randint(1, 100000))
    array = list(set(array))
    array1 = array[:]
    array2 = array[:]
    array3 = array[:]
    array4 = array[:]
    array5 = array[:]
    result1 = InsertSort(array1)
    result2 = insert_sort(array2)
    result3 = ShellSort(array3)
    result4 = BubbleSort(array4)
    result5 = QuickSort(array5)

    # print("插入排序计算时间{:.5f},{}".format(result1[0], result1[1]))
    # print("简单排序计算时间{:.5f},{}".format(result2[0], result2[1]))
    # print("希尔排序计算时间{:.5f},{}".format(result3[0], result3[1]))
    # print("冒泡排序计算时间{:.5f},{}".format(result4[0], result4[1]))
    # print("快速排序计算时间{:.5f},{}".format(result5[0], result5[1]))

    print("插入排序计算时间{:.5f},".format(result1))
    print("简单排序计算时间{:.5f},".format(result2))
    print("希尔排序计算时间{:.5f},".format(result3))
    print("冒泡排序计算时间{:.5f},".format(result4))
    print("快速排序计算时间{:.5f},".format(result5))


def InsertSort(list):
    """
        直接插入排序法
        将列表分为两部分，第一部分为有序列表，第二部分为无序列表，
        初始时，有序列表只有第一个元素，无序列表从第二个元素起，
        将无序列表的元素依次拿出按大小插入到有序列表中，
        当无序列表中元素为0时结束排序。
    """
    tic = time.process_time()

    log = 0
    # 从第二个元素起开始，
    for i in range(1, len(list)):
        # 将要排的数保存起来，指向temp
        temp = list[i]
        # 有序列表为[0,j],无序表为[i,len(list)]
        j = i - 1
        """
            将temp与有序列表从后向前比较。
            若temp小于list[j]则将list[j]的值后移一位，
            后移的目的是为将来插入temp提供空间，
            j自减1，继续比较
        """
        while j >= 0 and temp < list[j]:
            list[j+1] = list[j]
            j -= 1
            log += 2
        # 当循环停止时的j就是 temp >= lis[j]的位置，将temp插入j后面即可
        list[j+1] = temp
        log += 3
    toc = time.process_time()
    t = toc - tic
    return t


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
    log = 0
    tic = time.process_time()
    step = len(list) // 2
    while step > 0:
        for i in range(step, len(list)):
            temp = list[i]
            j = i - step
            while j >= 0 and temp < list[j]:
                list[j+step] = list[j]
                j -= step
                log += 2
            list[j+step] = temp
            log += 3
        step = step // 2
    toc = time.process_time()
    t = toc - tic
    return t


def insert_sort(list):
    """
        直接插入排序简单版
    """
    tic = time.process_time()
    log = 0
    for i in range(1, len(list)):
        for j in range(0, i):
            if list[i] < list[j]:
                list.insert(j, list[i])
                list.pop(i+1)
                log = log + 2
                break
    toc = time.process_time()
    t = toc - tic
    return t


def BubbleSort(list):

    tic = time.process_time()
    """
        冒泡排序的核心是交换相邻元素。
        大的向后，小的向前，外层一次循环可以确定一个元素位置
    """

    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    toc = time.process_time()
    t = toc - tic
    return t


def QuickSort(list):
    """
        快速排序，基于冒泡排序的改进版。
        其核心思想是分而治之和迭代

    """
    tic = time.process_time()



    def Insert_Sort(list):
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
        if end - start < 10:
            Insert_Sort(list)
        else:
            index = partition(list, start, end)
            quick_sort(list, start, index-1)
            quick_sort(list, index+1, end)

    quick_sort(list, 0, len(list)-1)
    top = time.process_time()
    t = top - tic
    return t


if __name__ == main():
    main()


