#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    直接插入排序法
"""

import time
import random

def main():
    """
        主函数
    """
    arraytest = [3,4,2,4,4,10,7,5,3,2,1,5,6,7,0]
    intsert_sort_1(arraytest)
    print(arraytest)
    array = []
    for i in range(10000):
        array.append(random.randint(1, 1000000))
    # array = list(set(array))
    array1 = array[:]
    array2 = array[:]
    array3 = array[:]
    array4 = array[:]
    array5 = array[:]
    # result1 = InsertSort(array1)
    result2 = insert_sort(array2)
    result3 = ShellSort(array3)
    result4 = InsertSort_1(array4)
    result5 = InsertSort_1(array5)
    # print("插入排序计算时间{:.5f}".format(result1))
    print("简单排序计算时间{:.5f}".format(result2))
    print("希尔排序计算时间{:.5f}".format(result3))
    print("二分插入排序时间{:.5f}".format(result4))
    print("二分简单排序时间{:.5f}".format(result5))


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
        # 当循环停止时的j就是 temp >= lis[j]的位置，将temp插入j后面即可
        list[j+1] = temp
    toc = time.process_time()
    t = toc - tic
    return t

def BinarySearch(list, end, value):
    """
        使用二分查找，优化直接插入排序
        直插表前面部分列表是有序的，可以用二分查找省去逐一比较时间
    """
    low = 0
    high = end
    while low <= high:
        middle = (low + high)//2
        if list[middle] > value:
            high = middle - 1
        else:
            low = middle + 1
    return low


def InsertSort_1(list):
    """
        直接插入排序法
        将列表分为两部分，第一部分为有序列表，第二部分为无序列表，
        初始时，有序列表只有第一个元素，无序列表从第二个元素起，
        将无序列表的元素依次拿出按大小插入到有序列表中，
        当无序列表中元素为0时结束排序。
    """
    tic = time.process_time()

    # 从第二个元素起开始，
    for i in range(1, len(list)):


        # 有序列表为[0,j],无序表为[i,len(list)]
        """
            将temp与有序列表从后向前比较。
            若temp小于list[j]则将list[j]的值后移一位，
            后移的目的是为将来插入temp提供空间，
            j自减1，继续比较
        """
        index = BinarySearch(list, i - 1, list[i])
        if i != index:
            j = i - 1

        # 将要排的数保存起来，指向temp
            temp = list[i]
            while j >= index :
                list[j+1] = list[j]
                j -= 1
        # 当循环停止时的j就是 temp >= lis[j]的位置，将temp插入j后面即可
            list[index] = temp
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


def insert_sort(list):
    """
        直接插入排序简单版
    """
    tic = time.process_time()
    for i in range(1, len(list)):
        for j in range(0, i):
            if list[i] < list[j]:
                list.insert(j, list[i])
                list.pop(i+1)
                break
    toc = time.process_time()
    t = toc - tic
    return t


def intsert_sort_1(list):
    """
        二分查找改进版
    """
    tic = time.process_time()
    for i in range(1, len(list)):
        index = BinarySearch(list, i-1, list[i])
        if i != index:
            list.insert(index, list[i])
            list.pop(i+1)

    toc = time.process_time()
    t = toc - tic
    return t


if __name__ == main():
    main()


