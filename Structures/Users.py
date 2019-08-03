from graphviz import Digraph
class Node:
    #Remember that we do not need to declare our class attributes
    #in Python, only assign those attributes through our constructor
    def __init__(self, name):   #constructor of class Node
        self.name = name          #assign the value sent as a parameter to our class atribute
        self.next = None      #assign the pointer link to None (null)
        self.previous = None


class CircularLinkedList:
    def __init__(self):         #constructor of class CricularLinkedList
        self.head = None        #start our list empty, hence our head is None (null)

    #ADD method
    def add(self,node):
        if self.head is None:   #verify if our CircularLinkedList is empty
            self.head = node    #if is empty assign the first node to our head
            self.head.next = node    #by definition a CircularLinkedList next-link points to itself
            self.head.previous = node
        else:
            temp = self.head
            while temp.next is not self.head:    #iterate through our list until-
                temp = temp.next                 #-we reach the end of it
            temp.next = node                     #assign the pointer link of the last element to our new element
            node.next = self.head                #assign the next-link of the last node to the head of the CircularLinkedList
            node.previous = temp
            self.head.previous = node

    #PRINT method
    def print_list(self):
        if self.head is None:               #verify if our CircularLinkedList is empty
            print('The list is empty')      #print a warning
        else:
            temp = self.head
            while temp.next is not self.head:    #iterate our list printing each element-
                print(temp.name,end='')            #-as we go
                print('->',end='')
                temp = temp.next
            print(temp.name,end='')                #print the las element in order to avoid [1->2->3->] the last link pointing tu None (null)
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


list = CircularLinkedList()     #create a new CircularLinkedList
list.add(Node("juan"))       #add element 1
list.add(Node("pedro"))       #add element 2
list.add(Node("lucas"))       #add element 3
list.add(Node("Peter"))
list.add(Node("Ludovico"))
list.add(Node("Chriss"))
list.add(Node("Maik"))
list.add(Node("Zlatan"))
#list.print_list()       #print the list
list.graph()