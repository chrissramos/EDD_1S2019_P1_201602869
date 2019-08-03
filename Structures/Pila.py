class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.next = None

class Pila:
    def __init__(self):
        self.head = None

    def add(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def print_pila(self):
        if self.head is None:
            print("Pila vacia")
        else:
            temp = self.head
            while temp.next is not None:
                print("[", temp.x, " ,", temp.y, "]", end='')
                print('->', end='')
                temp = temp.next
            print("[", temp.x, " ,", temp.y, "]")


pila = Pila()
pila.add(Node(1, 2))
pila.add(Node(3, 4))
pila.add(Node(5, 6))
pila.print_pila()
pila.add(Node(7, 8))
pila.print_pila()

