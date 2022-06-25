class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0


    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node!= None:
                print(current_node.data, end= ' ')
                current_node = current_node.next
        print()


    def append(self, data):
        new_node = Node(data)
        if self.head == None: #If linked list is empty, we make head and tail both equal to the new node
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        else: #Else, we make the previous pointer of the new node point to the present tail.
            new_node.previous = self.tail
            self.tail.next = new_node #Then we make the next pointer of the present tail point to the new node thus establishing a two way link between the present tail and the new node
            self.tail = new_node #Finally we update the tail to be equal to the new node
            self.length += 1
            return

    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        else:
            new_node.next = self.head #We make the next of the new node point to the present head
            self.head.previous = new_node #We establish a two-way link by making the previous of the present head point to the new node
            self.head = new_node #Finally we update the head
            self.length += 1
            return


    def insert(self, position, data):
        if position == 0:
            self.prepend(data) #Inserting at position 0 is equivalent to prepending. So instead of repeating code, we simple call the prepend method
            return
        if position >= self.length:
            if position > self.length:
                print('This position is not available. Inserting at the end of the list')
            self.append(data) #Similarly, inserting ata position >= the length of the list is equivalent to 

l=DoublyLinkedList()
l.append(22)
l.print_list()