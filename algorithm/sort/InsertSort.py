#!/usr/bin/python3
# -*- encoding=utf-8 -*-

"""
    直接插入排序
"""

def main():
    list_str = input("请输入数组，用空格隔开:").split(" ")
    list_int = [int(i) for i in list_str]
    print("排序前:", list_int)
    print("排序后:", InsertSort(list_int))

def InsertSort(list):
    for i in range(1,len(list)):
        for j in range(0,i):
            if list[i] < list[j]:
                list.insert(j,list[i])
                list.pop(i+1)
                break
    return list

if __name__ == main():
    main()
