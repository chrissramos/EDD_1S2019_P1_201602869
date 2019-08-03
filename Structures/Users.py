from graphviz import Digraph
class Node:

    def __init__(self, name):
        self.name = name
        self.next = None
        self.previous = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    #ADD method
    def add(self, node):
        if self.head is None:
            self.head = node
            self.head.next = node
            self.head.previous = node
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head
            node.previous = temp
            self.head.previous = node

    #PRINT method
    def print_list(self):
        if self.head is None:
            print('The list is empty')
        else:
            temp = self.head
            while temp.next is not self.head:
                print(temp.name,end='')
                print('->',end='')
                temp = temp.next
            print(temp.name,end='')
            print('->',end='')
            temp = temp.next
            print(temp.name)

    def graph(self):
        g = Digraph('G', filename='circular', format='png')
        temp = self.head
        while temp.next is not self.head:
            g.edge(temp.name, temp.next.name)
            g.edge(temp.next.name, temp.name)
            temp = temp.next
        g.edge(temp.name, self.head.name)
        g.edge(self.head.name, temp.name)
        g.view()


list = CircularLinkedList()
list.add(Node("juan"))
list.add(Node("pedro"))
list.add(Node("lucas"))
list.add(Node("Peter"))
list.add(Node("Ludovico"))
list.add(Node("Chriss"))
list.add(Node("Maik"))
list.add(Node("Zlatan"))
list.print_list()
list.graph()