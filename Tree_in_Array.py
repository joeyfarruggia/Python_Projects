#Create a tree and store in an array

#initialize the tree as a list
tree = []

#Function to insert a node in the tree
def insert_node(value):
    tree.append(value)

#Insert some nodes into the tree
insert_node(10)
insert_node(5)
insert_node(15)
insert_node(3)
insert_node(7)
insert_node(12)

#Print the tree
print("Tree stored in an array:", tree)