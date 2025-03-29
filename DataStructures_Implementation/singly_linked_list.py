class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end = "->")
            current = current.next
        print("End of list")
    
    def insert_at_position(self, data, position):
        if position < 0 or position > self.size:
            raise IndexError("Position out of range")
            
        new_node = Node(data)
        if position == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                self.size += 1
            else:
                new_node.next = self.head
                self.head = new_node
                self.size += 1
        elif position == self.size:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
        else:
            prev = self.head
            for _ in range(position-1):
                if prev is None:
                    raise IndexError("Invalid position")
                prev = prev.next
            if prev is None:
                raise IndexError("Invalid position")
            new_node.next = prev.next
            prev.next = new_node
            self.size += 1
    
    def delete_at_position(self, position):
        if not self.head:
            raise ValueError("List is empty")
        if position < 0 or position >= self.size:
            raise IndexError("Position out of range")
            
        if position == 0:
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
        else:
            prev = self.head
            for _ in range(position-1):
                if prev is None:
                    raise IndexError("Invalid position")
                prev = prev.next
            if prev.next is None:
                raise IndexError("Invalid position")
            prev.next = prev.next.next
            if position == self.size - 1:
                self.tail = prev
            self.size -= 1


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_position(50, 0)
    sll.insert_at_position(10, 1)
    sll.insert_at_position(20, 2)
    sll.insert_at_position(40,1)
    sll.traverse()
    sll.delete_at_position(2)
    sll.traverse()
    sll.delete_at_position(2)
    sll.traverse() 
    sll.delete_at_position(0)
    sll.traverse()