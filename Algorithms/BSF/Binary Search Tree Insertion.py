### Binary Search Tree Insertion ###

class Node:
    def __init__(self, data):
        self.key=data
        self.left=None
        self.right=None


    


class BinarySearchTree:
    def __init__(self):
        self.root=None  
    
    def insertion(self, curnode,data):
        ## insertion at a curnode
        newnode=Node(data)
        if curnode==None:
            curnode=newnode
        elif data>curnode.key:
            curnode.right=self.insertion(curnode.right,data)
        elif data<curnode.key:
            curnode.left=self.insertion(curnode.left,data)
        return curnode

    def insert(self,data):
        ## insertion to the tree
        newnode=Node(data)
        if self.root==None:
            self.root=newnode
        else:
            self.insertion(self.root,data)
    
    
    def insert2(self,data):
        ## insert iteratively
        newnode=Node(data)
        curnode=self.root

        if curnode==None:
            self.root=newnode

        while curnode is not None:
            if data>curnode.key:
                if curnode.right== None:
                    curnode.right=newnode
                    break
                else:
                    curnode=curnode.right
            if data<curnode.key:
                if curnode.left==None:
                    curnode.left=newnode
                    break
                else:
                    curnode=curnode.left


def preorder(root):
    if root==None:
         return 
    else:
        print(root.key)
    preorder(root.left)
    preorder(root.right)

def Inorder(root):
    if root==None:
        return
    else: 
        Inorder(root.left)
        print(root.key)
        Inorder(root.right)


tree=BinarySearchTree()

arr=[4,3,1,7,2,5]

'''
tree structure: 
     4
    /  \
   3    7
  /    /
 1    5
   \
    2    
'''
for i in range(len(arr)):
    tree.insert(arr[i])

preorder(tree.root)  ## 4, 3, 1 2,7 5
Inorder(tree.root)   ## 1 2 3 4 5 7

tree2=BinarySearchTree()
for i in range(len(arr)):
    tree2.insert2(arr[i])

preorder(tree2.root) ## 4, 3, 1 2,7 5
Inorder(tree2.root)  ## 1 2 3 4 5 7








        


