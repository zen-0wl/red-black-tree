import sys

#node creation
class Node():
    def insideNode(inside, type):
        inside.type = type
        inside.colour = 1
        inside.parent = None
        inside.left = None
        inside.right = None 
        inside.colour = 1
#class for red black tree 
class RBT():
    def insideTree(inside):
        inside.nul = Node(0)
        inside.nul.left = None
        inside.nul.right = None
        inside.nul.colour = 0
        inside.root = inside.nul

    # preorder
    def preorder(inside, node):
        if node != nul:
            print(node.item + " ")
            inside.preorder(node.left)
            inside.preorder(node.right)
    #inorder 
    def inorder(inside, node):
        if node != nul:
            inside.inorder(node.left)
            print(node.item + " ")
            inside.inorder(node.right)
    #postorder
    def postorder(inside, node):
        if node != nul:
            inside.postorder(node.left)
            inside.postorder(node.right)
            print(node.item + " ")
    
