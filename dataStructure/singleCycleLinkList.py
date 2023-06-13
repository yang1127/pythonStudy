# -*-coding:utf-8-*-
class singleNode(object):
    # 节点
    def __init__(self, item):
        # 存储元素
        self.item = item
        # 下一个节点
        self.next = None


class singleCycleLinkList(object):
    def __init__(self, node=None):
        # node为空
        self.__head = None
        # node不为空，传入一个node节点，指向下一个
        if node:
            node.next = node

    # is_empty() 链表是否为空, 只需判断_head为空
    def is_empty(self):
        return self.__head is None

    # length() 链表长度
    def length(self):
        if self.is_empty():
            return 0

        # cur: 游标，记录移动位置
        cur = self.__head
        # count: 记录移动次数，即长度
        count = 1  # 从1开始
        # 只有一个节点时，cur.next == self.__head，即count=1
        while cur.next != self.__head:
            count += 1
            cur = cur.next  # 向后移动
        return count

    # travel() 遍历整个链表
    def travel(self):
        if self.is_empty():
            return

        # cur: 游标，记录移动位置
        cur = self.__head
        while cur.next != self.__head:
            print(cur.item, end=" ")
            cur = cur.next  # 向后移动
        # 退出循环，cur指向尾节点，尾节点需要再打印下
        print(cur.item)

    # add(item) 链表头部添加元素
    def add(self, item):
        # 创建节点，将元素转为节点
        node = singleNode(item)

        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            # cur: 游标，记录移动位置
            cur = self.__head
            # 找到尾部
            while cur.next != self.__head:
                cur = cur.next
            # 将node节点插入
            node.next = self.__head
            self.__head = node
            cur.next = self.__head

    # append(item) 链表尾部添加元素
    def append(self, item):
        # 创建节点，将元素转为节点
        node = singleNode(item)

        # 1、空列表
        if self.is_empty():
            self.__head = node
            node.next = node
        # 2、不为空
        else:
            cur = self.__head
            # 遍历到最后一个节点
            while cur.next != self.__head:
                cur = cur.next
            # 将node.next给self.__head, cur.next指向node
            node.next = self.__head
            cur.next = node

    # insert(pos, item) 指定位置添加元素
    def insert(self, pos, item):
        """  解释参数
        :param pos: 从0开始
        """
        # 创建节点，将元素转为节点
        node = singleNode(item)

        # pos位置小于等于0，头插
        # pos位置大于原链表长度，尾插
        # pos中间位置，count大于pos-1的位置插入
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                pre = pre.next
                count += 1

            # 退出循环，node的先指向pre的next，pre再指向node
            node.next = pre.next
            pre.next = node

    # remove(item) 删除节点
    def remove(self, item):
        if self.is_empty():
            return False

        cur = self.__head
        pre = None

        # 遍历查找
        while cur.next != self.__head:
            if cur.item == item:
                # 判断是否为头节点
                if cur == self.__head:
                    # 头节点
                    # 找尾节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next

                    # 找到
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间节点
                    pre.next = cur.next
                return  # 删除后退出
            else:
                pre = cur
                cur = cur.next

        # 退出循环，cur指向尾节点
        if cur.item == item:
            if cur == self.__head:
                # 只有一个节点
                self.__head = None
            else:
                pre.next = cur.next

    # search(self, item) 查找元素
    def search(self, item):
        if self.is_empty():
            return False
                
        # cur游标
        cur = self.__head

        # 遍历查找
        while cur.next != self.__head:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        # 退出循环，指向尾节点
        if cur.item == item:
            return True
        return False


if __name__ == '__main__':
    sll = singleCycleLinkList()
    # 判断是否为空
    print(sll.is_empty())

    # 长度
    print(sll.length())

    # 前插
    sll.add(9)
    print(sll.travel())

    # 后插
    sll.append(5)
    print(sll.travel())
    sll.append(2)
    print(sll.travel())
    sll.append(6)
    print(sll.travel())

    # 指定插入
    sll.insert(-1, -1)
    print(sll.travel())
    sll.insert(12, 12)
    print(sll.travel())
    sll.insert(1, 1)
    print(sll.travel())

    # 查找
    print("------")
    print(sll.search(2))
    print(sll.search(77))
    print("------")

    # 遍历
    print(sll.travel())

    # 删除
    sll.remove(6)
    print(sll.travel())
