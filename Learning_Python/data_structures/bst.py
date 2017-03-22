class Node:
    def __init__(self,key):
        if key is not None:
            self.key = key
            self.left = None
            self.right = None
        
def insertNode(node,key):
    if node is None:
        node = Node(key)
    elif node.key > key:
        if node.left is None:
            node.left = Node(key)
        else:
            insertNode(node.left, key)
    else:
        if node.right is None:
            node.right = Node(key)
        else:
            insertNode(node.right,key)
    return node
            
def inorderPrint(node):
    if node:
        inorderPrint(node.left)
        print(node.key),
        inorderPrint(node.right)
        
def PredecessorSuccessor(root, key):
    global pre 
    global suc
    if root.key == key:
        if root.left:
            temp = root.left
            while(temp.right):
                temp = temp.right
            pre = temp.key
        if root.right:
            temp = root.right
            while(temp.left):
                temp = temp.left
            suc = temp
    elif root.key > key:
        suc = root.key
        PredecessorSuccessor(root.left, key)
    elif root.key < key:
        pre = root.key
        PredecessorSuccessor(root.right, key)
        
# def CheckIfBST(root, mini,maxi):
#     BST = True
#     if root.key < mini or root.key > maxi:
#         BST = False
#     else:
#         if root.left:
#             BSTleft = CheckIfBST(root.left, mini,root.key - 1)
#         else:
#             BSTleft = True
#         if root.right:
#             BSTright = CheckIfBST(root.right, root.key + 1 ,maxi)
#         else:
#             BSTright = True
#         BST = (BSTleft and BSTright)
            
   # return BST


def CheckIfBST(root, mini,maxi):
    return not ((root.key < mini or root.key > maxi)
        or (root.left and not CheckIfBST(root.left, mini,root.key - 1))
        or (root.right and not CheckIfBST(root.right, root.key + 1 ,maxi)))
        
        
def LowestCommonAncestor(node, node1, node2):
    if node1.key > node.key and node2.key > node.key:
        return LowestCommonAncestor(node.right, node1, node2)
    if node1.key < node.key and node2.key < node.key:
        return LowestCommonAncestor(node.left, node1, node2)
    return node.key
    
def kthSmallest(root, k):
    global count
    if count > k or count < 0:
        print("Invalid value of k")
    else:
        if root.left and count < k:
            kthSmallest(root.left, k)
        count +=1 
        if count == k:
            print(root.key)
        if root.right and count < k:
            kthSmallest(root.right, k)
            
def BSTtoList(root,lst):
    if root.left:
        BSTtoList(root.left,lst)
    lst.insert(0,(root.key))
    if root.right:
        BSTtoList(root.right,lst)
    
#Merge 2 binary search trees with limited space           
def Merge2Trees(tree1, tree2):
    global list1, list2
    BSTtoList(tree1,list1)
    BSTtoList(tree2,list2)
    count_list1 = len(list1)
    count_list2 = len(list2)
    n=0 
    m=0
    root1 = None
    root2 = None
    while n < count_list1:
        if len(list1) > 0 and len(list2) > 0:
            if list1[-1] < list2[-1]:
                key = list1.pop()
            else:
                key = list2.pop()
        elif len(list1) > 0:
            key = list1.pop()
        else:
            key = list2.pop()
        root1 = insertNode(root1,key)
        n+=1
    
    while m < count_list2:
        if len(list1) > 0 and len(list2) > 0:
            if list1[-1] < list2[-1]:
                key = list1.pop()
            else:
                key = list2.pop()
        elif len(list1) > 0:
            key = list1.pop()
        else:
            key = list2.pop()
        root2 = insertNode(root2,key)
        m+=1
    
    print("inorder traversal of tree1- "),
    inorderPrint(root1)
    
    print("inorder traversal of tree2- "),
    inorderPrint(root2)
    
def SwapIncorrectNodes(root):
    global first, last
    if root:
        SwapIncorrectNodes(root.left)
        if root.key == first:
            root.key = last
        elif root.key == last:
            root.key = first
        SwapIncorrectNodes(root.right)
    
def find(root, prev):
    global first, last
    if root.left:
        find(root.left, prev)
    if prev is not None:
        if prev > root.key:
            if first is None:
                first = prev
            last = root.key
    prev = root.key
    if root.right:
        find(root.right, prev)
        
class DLLnode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLLhead:
    def __init__(self):
        self.head = None
        
    def insert(self,new_data):
        new_node = DLLnode(new_data)
        if self.head is None:
            self.head = DLLnode(new_data)
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
    def insertafter(self,prev_node, new_data):
        if prev_node:
            new_node = DLLnode(new_data)
            new_node.prev = prev_node
            if prev_node.next:
                temp = prev_node.next
                new_node.next = temp
                temp.prev = new_node
            else:
                self.appenddata(new_data)
                # prev_node.next = new_node
                # new_node.prev = prev_node
        else:
            self.insert(new_data)
            
        
    def appenddata(self,new_data):
        new_node = DLLnode(new_data)
        if self.head:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last
        else:
            self.head = new_node
            
    def printDLL(self):
        node = self.head
        print "\nDLL Traversal in forward direction"
        while(node is not None):
            print(node.data),
            last = node
            node = node.next
 
        print "\nDLL Traversal in reverse direction"
        while(last is not None):
            print(last.data),
            last = last.prev
    
first = None
last = None
list1 = []
list2 = []
count = 0    
pre = None
suc = None
root = None
root = insertNode(root,50)
root = insertNode(root,17)
root = insertNode(root, 72)
root = insertNode(root, 12)
root = insertNode(root, 23)
root = insertNode(root, 54)
root = insertNode(root, 76)
root = insertNode(root, 67)
root = insertNode(root, 9)
root = insertNode(root, 14)
root = insertNode(root, 19)
PredecessorSuccessor(root, 19)
print("inorder traversal - "),
inorderPrint(root)
print("\n")
print("Predecessor of 19 is " + str(pre) + " and successor of 19 is " + str(suc))

root1 = Node(3)
root1.right = Node(5)
root1.left = Node(2)
root1.left.right = Node(4)
root1.left.left = Node(1)

BST = CheckIfBST(root, -4294967296, 4294967296)
print ("BST for root is " + str(BST))
BST = CheckIfBST(root1, -4294967296, 4294967296)
print ("BST for root1 is " + str(BST))

LCA = LowestCommonAncestor(root, Node(23), Node(12))
print ("LCA is - " + str(LCA) )

print("Kth smallest element where k = 3 is"),
kthSmallest(root, 3)

Merge2Trees(root, root1)

root3 = Node(6)
root3.left = Node(10)
root3.right = Node(2)
root3.left.left = Node(1)
root3.left.right = Node(3)
root3.right.left = Node(7)
root3.right.right = Node(12)

print("\n")
find(root3, None)
SwapIncorrectNodes(root3)
print("inorder traversal - "),
inorderPrint(root3)

llist = DLLhead()
llist.insert(2)
llist.insert(1)
llist.insertafter(llist.head.next,3)
llist.appenddata(4)
llist.appenddata(5)
llist.appenddata(6)
llist.appenddata(7)
llist.printDLL()








