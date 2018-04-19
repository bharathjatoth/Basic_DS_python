class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insertend(self,data):
        end = Node(data)
        if self.head is None:
            self.head = end.data
            return
        last = self.head
        while(last.next!=None):
            last = last.next
        last.next = end
    def insertat(self,prev_node,curr_data):
        if prev_node is None:
            print("not a linked list")
        curr = self.head
        if curr.data is prev_node:
            new_node = Node(curr_data)
            new_node.next = curr.next
            curr.next = new_node
        # new_node = Node(curr_data)
        # new_node.next = prev_node.next
        # prev_node.next = new_node
    def printll(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
if __name__=="__main__":
    ll = Linkedlist()
    ll.head = Node(1)
    second = Node(44)
    third = Node(55)
    ll.head.next = second
    second.next = third
    ll.printll()
    ll.insert(3333)
    print("now printing the current version of linked list")
    ll.printll()
    ll.insertend(9999999)
    print("^^^^^^^^^^^")
    ll.printll()
    ll.insertat(44,88888)
    print("(((((((((")
    ll.printll()
