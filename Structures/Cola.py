class Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next = None

class Cola:
    def __init__(self):
        self.head = None

    def add(self, node):
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node 





input()
