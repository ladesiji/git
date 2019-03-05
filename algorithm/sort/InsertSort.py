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
    array = []
    for i in range(10000):
        array.append(random.randint(1, 1000000))
    # array = list(set(array))
    array1 = array[:]
    array2 = array[:]
    array3 = array[:]
    result1 = InsertSort(array1)
    result2 = insert_sort(array2)
    result3 = ShellSort(array3)
    print("插入排序计算次数{},{}".format(result1[0], result1[1], result1[2]))
    print("简单排序计算次数{},{}".format(result2[0], result2[1], result2[2]))
    print("希尔排序计算次数{},{}".format(result3[0], result3[1], result3[2]))


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
    return [log, t, list]


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
    return [log, t, list]


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
    return [log, t, list]


if __name__ == main():
    main()


