class Node:
    #Remember that we do not need to declare our class attributes
    #in Python, only assign those attributes through our constructor
    def __init__(self, id):   #constructor of class Node
        self.id = id          #assign the value sent as a parameter to our class atribute
        self.next = None      #assign the pointer link to None (null)


class CircularLinkedList:
    def __init__(self):         #constructor of class CricularLinkedList
        self.head = None        #start our list empty, hence our head is None (null)

    #ADD method
    def add(self,node):
        if self.head is None:   #verify if our CircularLinkedList is empty
            self.head = node    #if is empty assign the first node to our head
            self.head.next = node    #by definition a CircularLinkedList next-link points to itself
        else:
            temp = self.head
            while temp.next is not self.head:    #iterate through our list until-
                temp = temp.next                 #-we reach the end of it
            temp.next = node                     #assign the pointer link of the last element to our new element
            node.next = self.head                #assign the next-link of the last node to the head of the CircularLinkedList

    #PRINT method
    def print_list(self):
        if self.head is None:               #verify if our CircularLinkedList is empty
            print('The list is empty')      #print a warning
        else:
            temp = self.head
            while temp.next is not self.head:    #iterate our list printing each element-
                print(temp.id,end='')            #-as we go
                print('->',end='')
                temp = temp.next
            print(temp.id,end='')                #print the las element in order to avoid [1->2->3->] the last link pointing tu None (null)
            print('->',end='')
            temp = temp.next
            print(temp.id)


list = CircularLinkedList()     #create a new CircularLinkedList
list.add(Node(1))       #add element 1
list.add(Node(2))       #add element 2
list.add(Node(3))       #add element 3
list.print_list()       #print the list