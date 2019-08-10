#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    这是一个python的单链表
    数据元素中包含两部分，数据域与指针域。
    链表中第一个元素地址存在头节点，最后一个元素的指针指向NULL

    链表的方法包括初始化链表、清空链表、判断为空、插入、长度、获取元素、
    比较、查找、前一个、后一个、删除、访问、遍历等基本操作
"""

class Node(object):
    """
        创建节点类
    """
    def __init__(self,value,p=None):
        """
            节点初始化
        """
        self.data = value
        self.next = None
class LinkList(object):
    """
        创建链表类
    """
    def __init__(self):
        """
            链表初始化
        """
        self.head = None

    def __getitem__(self, key):
        """
            获取元素
        """
        if self.is_empty():
            print('linklist is empty.')
            return False
        elif key < 0 or key >= self.getlength():
            print('the given key is error')
            return False
        else:
            return self.getitem(key)

    def __setitem__(self, key, value):
        """
            设置节点值
        """
        if self.is_empty():
            print('linklist is empty.')
            return False
        elif key < 0 or key > self.getlength():
            print('the given key is error')
            return False
        else:
            self.delete(key)
            return self.insert(key)
    def initlist(self, data):
        """
            将给定数据初始化到链表
        """
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next
        return True

    def getlength(self):
        """
            获取链表长度
        """
        p = self.head
        length = 0
        while p != None:
            length += 1
            p = p.next
        return length

    def is_empty(self):
        """
            判断链表是否为空
        """
        if self.head.next == None:
            return True
        else:
            return False

    def clear(self):
        """
            清空链表
        """
        self.head = None

    def append(self, item):
        """
            链表末尾添加元素
        """
        q = Node(item)
        if self.head == None:
            self.head = q
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = q

    def getitem(self, index):
        """
            获取指定索引的数据
        """
        if self.is_empty():
            print('linklist is empty.')
            return False
        j = 0
        p = self.head
        while p.next != None and j < index:
            p = p.next
            j += 1
        if j == index :
            return p.data
        else:
            print('target is not exist')
            return False

    def insert(self, index, item):
        """
            指定位置插入
        """
        if self.is_empty() or index < 0 or index >= self.getlength():
            print('linklist is empty.')
            return False
        if index == 0:
            q = Node(item,self.head)
            q.next = self.head
            self.head = q
            return True
        p = self.head
        post = self.head
        j = 0
        while p.next != None and j < index:
            post = p
            p = p.next
            j += 1
        if index == j :
            q = Node(item)
            post.next = q
            q.next = p
        return True

    def delete(self, index):
        """
            删除指定位置元素
        """
        if self.is_empty() or index < 0 or index > self.getlength():
            print("link is empty")
            return False
        if index == 0:
            self.head = self.head.next
            return self.head.data
        p = self.head
        post = self.head
        j = 0
        while p.next != None and j < index:
            post = p
            p = p.next
            j += 1
        if j == index :
            post.next = p.next
            return p.data

    def index(self, value):
        """
            查找value的索引
        """
        if self.is_empty() :
            print("link is empty")
            return False
        if self.head == value:
            return 0
        p = self.head
        i = 0
        while p.next != None and p.data != value:
            p = p.next
            i += 1
        if p.data == value:
            return i
        else:
            print('target is not exit')
            return -1
        
def main():
    l = LinkList()
    l.initlist([1,2,3,4,5])
    print("the 4's data is {}".format(l.getitem(4)))
    l.append(6)
    print("the 6's data is {}".format(l.getitem(5)))

    l.insert(4,40)
    print("the 3's data is {}".format(l.getitem(3)))
    print("the 4's data is {}".format(l.getitem(4)))
    print("the 5's data is {}".format(l.getitem(5)))
    
    print("the 40's index is {}".format(l.index(40)))

    l.delete(5)
    print("the 5's data is {}".format(l.getitem(5)))


if __name__ == '__main__':
    main()
    
