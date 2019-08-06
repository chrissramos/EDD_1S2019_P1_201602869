from graphviz import Digraph
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

    def delete(self):
        if self.head is None:
            print("Pila Vacia")
        else:
            temp = self.head
            temp2 = self.head.next
            temp.next = None
            self.head = temp2

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

    def graph(self):
        g = Digraph('G', filename='Pila', format='png', node_attr={'shape': 'record'}, graph_attr={'rankdir':'LR'})
        temp = self.head
        text = ''
        contador = 0
        text = '|'
        while temp.next is not None:
            #print('Estamos en:', '<f', contador, '>', temp.x, ',', temp.y, '|')
            text = text + "<f" + str(contador) + ">" + '(' + str(temp.x) + "," + str(temp.y) + ')' + "|"
            contador = contador + 1
            temp = temp.next
        print('Estamos en:', '<f', contador, '>', temp.x, ',', temp.y, '|')
        text = text + "<f" + str(contador) + ">" + '(' + str(temp.x) + "," + str(temp.y) + ')'
        print(text)
        g.node('struct1', text)
        g.view()


pila = Pila()
pila.add(Node(1, 2))
pila.add(Node(3, 4))
pila.add(Node(5, 6))
pila.add(Node(7, 8))
pila.add(Node(9, 10))

#pila.print_pila()
pila.graph()

#pila.print_pila()
#pila.add(Node(9,10))
#pila.print_pila()
#pila.delete()
#pila.print_pila()
#pila.delete()
#pila.print_pila()


