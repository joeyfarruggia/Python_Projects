#Create a Binary Search Tree (BST)
class Node:
    def __init__(self, key):
        self.left = None #left child of the node
        self.right = None #right child of the node
        self.val = key #key value of the node

class BST:
    def __init__(self):
        self.root = None #root of the BST

    #Insert a new node with the given key value into the BST
    def insert(self, key):
        if self.root is None:
            self.root = Node(key) #if the tree is empty, set the root to the new node
        else:
            self._insert_recursively(self.root, key) #otherwise, insert recursively

    def _insert_recursively(self, node, key):
        if key < node.val: #if the key is less than the current node's value
            if node.left is None:
                node.left = Node(key) #insert as left child
            else:
                self._insert_recursively(node.left, key) #recur on the left subtree
        else: #if the key is greater than or equal to the current node's value
            if node.right is None:
                node.right = Node(key) #insert as right child
            else:
                self._insert_recursively(node.right, key) #recur on the right subtree
    
    def search(self, key):
        return self._search_recursively(self.root, key) #search for the key starting from the root

    def _search_recursively(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_recursively(node.left, key)
        return self._search_recursively(node.right, key)
    
#Test the Binary Search Tree
bst = BST()

#Insert nodes
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)

#Search for a key
print(bst.search(7).val) #Output: 7
print(bst.search(4)) #Output: None (not found)