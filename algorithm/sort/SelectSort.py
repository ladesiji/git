# -*- encoding=utf-8 -*-

"""
    选择排序。
    每次从无序数组中选择一个最小的数放到前面
"""
import heapq

def SelectSort(array):
    """
        选择排序
    """
    for i in range(len(array)):
        index = i
        for j in range(i+1, len(array)):
            if array[j] < array[index]:
                index = j
        if index != i:
            array[i], array[index] = array[index], array[i]


def HeapSort(array):
    """
        堆排序。
    """
    n = len(array)//2
    for i in range(n):
        start = n-i-1
        end =len(array)-1
        HeapAdjust(array,start,end)
        # print(array,start,end)
    print(array)
    for i in range(len(array)):
        array[0], array[len(array)-1-i] = array[len(array)-1-i], array[0]
        HeapAdjust(array,0,len(array)-2-i)
        print(array,0,len(array)-2-i)



def HeapAdjust(array, start, end):
    """
        调整以start为子父节点的子树.
        此函数调用一次只调整父节点start一个，保证父节点调整后是合规的。
        前提条件是子节点的树是合规的树，如果父节点大于子节点，就不用做调整了。
    """
    temp = array[start]
    i = start
    j = 2 * i + 1
    while j <= end:
        # i 为父节点，j 和 j+1 为两个子节点，这里的if 保证j是两个子节点中最大的一个
        if (j < end) and (array[j] < array[j+1]):
            j += 1
        # 父节点小于子节点，将子节点值换给父节点
        if temp < array[j]:
            array[i] = array[j]
            i = j
            j = 2*i + 1
        # 父节点不小于子节点，认为该子树是合规的，不需要调整
        else:
            break
    array[i] = temp




def main():
    array = [1,2,3,4,5,6,7,8,9,0]
    array2 = [1,2,3,4,5,6,7,8,9]

    HeapSort(array)

    print(array)


if __name__ == main():
    main()