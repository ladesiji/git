"""
    排序算法日常练习 0312
    练习掌握的：插入排序、选择排序、冒泡排序、希尔排序、堆排序、快速排序、归并排序
"""


def insert_sort(array):
    """
        插入排序
    """
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]
        while j >= 0 and array[j] > temp:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = temp


def select_sort(array):
    """
        选择排序
    """
    for i in range(len(array)):
        temp = i
        for j in range(i+1, len(array)):
            if array[j] < array[temp]:
                temp = j
        array[i], array[temp] = array[temp], array[i]


def bubble_sort(array):
    """
        冒泡排序
    """
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def shell_sort(array):
    """
       希尔排序
    """
    step = (len(array)-1) // 2
    while step > 0:
        for i in range(step, len(array), step):
            temp = array[i]
            j = i - step
            while j >= 0 and array[j] > temp:
                array[j+step] = array[j]
                j -= step
            array[j+step] = temp
        step = step // 2


def heap_sort(array):
    """
        堆排序
    """
    i = len(array) // 2 - 1
    while i >= 0:
        heap_adjust(array, i, len(array)-1)
        i -= 1
    j = len(array) - 1
    while j > 0:
        array[0], array[j] = array[j], array[0]
        heap_adjust(array, 0, j-1)
        j -= 1


def heap_adjust(array, start, end):
    """
        最大堆调整
    """
    temp = array[start]
    j = start * 2
    while j <= end:
        if j < end and array[j] < array[j+1]:
            j += 1
        if j <= end and array[j] > temp:
            array[start] = array [j]
        else:
            break
        start = j
        j = j * 2
    array[start] = temp


def quick_sort(array):
    """
        快速排序
    """
    q_sort(array, 0, len(array)-1)


def q_sort(array, start, end):
    """
        快速排序的迭代函数
    """
    if start < end:
        index = partition(array, start, end)
        q_sort(array, start, index-1)
        q_sort(array, index+1, end)


def partition(array, start, end):
    """
       快速排序的分割函数
    """
    base = array[start]
    i, j = start, end
    while i < j:
        while i < j and array[j] >= base:
            j -= 1
        array[i] = array[j]
        while i < j and array[i] <= base:
            i += 1
        array[j] = array[i]
    array[i] = base
    return i


def merge_sort(array):
    """
        归并排序
    """
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return merge(left, right)


def merge(left, right):
    """
        将两个有序表合并
    """
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j +=1
    result += left[i:]
    result += right[j:]
    return result


def main():
    """
        测试函数
    """
    array = [4, 2, 5, 7, 1, 3, 8, 10, 9, 6]
    # insert_sort(array)
    # select_sort(array)
    # bubble_sort(array)
    # shell_sort(array)
    # heap_sort(array)
    # quick_sort(array)
    # array = merge_sort(array)
    print(array)


if __name__ == '__main__':
    main()