class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        new_node = Node(value)
        node = self.get_node(index-1) # index번째에 넣기 위해서는 index-1번쨰를 가져와야 가능
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

        return "index 번째 Node 뒤에 value 를 추가하세요!"


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)

linked_list.add_node(1,6)
linked_list.print_all()