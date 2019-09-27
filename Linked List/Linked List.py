###--------------- Implementation of Linked List ---------------###

## Define class: Node, each node has data+next
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None     ## initial the next (pointed) to be None

## Define class: Linked List

class Linkedlist:
    def __init__(self):
        self.head=None     ## initial head to be none
        self.tail=None

    def isempty(self):     ## check if the list is empty or not
        return self.head is None 
    
    def append(self, data):
        node=Node(data)
        if self.head is None:
            self.head=node
            self.tail=node
        else: 
            self.tail.next=node  ## move the pointer to point to node
            self.tail=node       ## move the tail to node
    
    def insert(self,data, pos):
        node=Node(data)
        curnode=self.head
        curindx=0
        while curindx<pos-1:    ## move the current node to pos-1
            curnode=curnode.next
            curindx +=1
        node.next=curnode.next
        curnode.next=node

        if node.next is None:
            self.tail=node

    def travesal(self):         ## travese linked list
        if not self.head:
            return
        cur=self.head
        yield cur.data
        while cur.next:
            cur=cur.next
            yield cur.data

    def delete(self,pos):    ## delete the data in postition:pos
        if not self.head:
            return
        curnode=self.head 
        curindx=0
        while curindx<pos-1:
            curnode=curnode.next
            if curnode is None:
                raise Exception("list length is less than the deleting postion")
            curindx +=1
        if pos==0:
            self.head=curnode.next
            curnode=curnode.next
            return 
        deletenode=curnode.next
        curnode.next=deletenode.next
    
    def size(self):         ## calculate the size of the linked list
        if not self.head:   ## empty list
            return 0
        curnode=self.head
        count=1
        while curnode.next is not None:
            curnode=curnode.next
            count +=1
        return count


      
if __name__ == '__main__':
    ll = Linkedlist()
    print(Linkedlist.size(ll))
    print(Linkedlist.isempty(ll))
    
    for i in range(10):
        ll.append(i)

    print(Linkedlist.size(ll))

    Linkedlist.append(ll,4)               ## append
    Linkedlist.append(ll,5)

    print(Linkedlist.isempty(ll))

    Linkedlist.insert(ll,3,2)             ## insert          
    
    for node in Linkedlist.travesal(ll):
        print('node is {0}'.format(node))

    Linkedlist.delete(ll,0)

    for node in Linkedlist.travesal(ll):
        print('node is {0}'.format(node))

    print(Linkedlist.size(ll))



## Question: can some node to be none in the linked list?

