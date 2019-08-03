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

    def print_list(self):
        if self.head is None:
            print("cola vacia")
        else:
            temp = self.head
            while temp.next is not None:
                print("[", temp.name, ",", temp.score, "]", end='')
                print("->", end='')
                temp = temp.next
            print("[", temp.name, ",", temp.score, "]","->NULL")



cola = Cola()
cola.add(Node("randall",100))
cola.add(Node("lucas",20))
cola.add(Node("pedro",30))
cola.add(Node("luis",25))
cola.add(Node("Manola",200))
cola.add(Node("Colocha",2000))

cola.print_list()

input()
