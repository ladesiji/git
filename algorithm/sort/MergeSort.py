"""
    归并排序。
    核心思想是分治法迭代处理。
    将列表分为两部分，每一部分再分为两部分，一直分到只有一个元素为止
    然后可以将每一个部分都可以看做一个有序有列表，
    将有序的列表按大小合并，达到排序效果
"""
def merge_sort(array):
    """
        先分割函数，直到只有一个元素为止
    """
    if len(array) <= 1:
        return array
    else:
        mid = len(array) // 2
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        # 调用合并函数，将分割后的有序表合并
        return (Merge(left, right))


def Merge(left, right):
    """
        合并两个有序数组
    """
    l, r = 0, 0
    result = []
    # 循环依次比较两个有序表的元素，将小的添加进新的结果中，并将指针加1
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # 将比较完后有序表中剩余的
    result += left[l:]
    result += right[r:]
    return result


def main():
    """
        测试函数
    """
    array = [4, 6, 9, 1, 2, 6, 5, 7, 2]
    array = merge_sort(array)
    print(array)


if __name__ == '__main__':
    main()

