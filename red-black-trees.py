import sys

#node creation
class Node():
    def __init__(inside, type):
        inside.type = type
        inside.colour = 1
        inside.parent = None
        inside.left = None
        inside.right = None 
        inside.colour = 1
#class for red black tree 
class RBT():
    def __init__(inside):
        inside.Tempty = Node(0)
        inside.Tempty.left = None
        inside.Tempty.right = None
        inside.Tempty.colour = 0
        inside.root = inside.Tempty

    # preorder
    def pre_order(inside, node):
        if node != Tempty:
            print(node.item + " ")
            inside.pre_order(node.left)
            inside.pre_order(node.right)
    # inorder 
    def in_order(inside, node):
        if node != Tempty:
            inside.in_order(node.left)
            print(node.item + " ")
            inside.in_order(node.right)
    # postorder
    def post_order(inside, node):
        if node != Tempty:
            inside.post_order(node.left)
            inside.post_order(node.right)
            print(node.item + " ")
    
    # search operation of red black tree
    def searchTree(inside, node, key):
        if node == Tempty or key == node.type:
            return node 
    
    # balance insert operation of red black tree 
    def insertion(inside, i):
        while i.parent.colour == 1:
            if i.parent == i.parent.parent.left:
                x = i.parent.parent.left

                if x.colour == 1:
                    x.colour == 0
                    i.parent.colour = 0
                    i.parent.parent.colour = 1
                    i = i.parent.parent 
                elif i == i.parent.left:
                    i = i.parent
                    inside.rotateRight(i)
                i.parent.colour = 0
                i.parent.parent.colour = 1
                inside.rotateLeft(i.parent.parent)
            else:
                x = i.parent.parent.right 

                if x.colour == 1:
                    x.colour = 0
                    i.parent.colour = 0
                    i.parent.parent.colour = 1
                    i = i.parent.parent
                elif i == i.parent.right:
                    i = i.parent
                    inside.rotateLeft(i)
                i.parent.colour = 0
                i.parent.parent.colour = 1
                inside.rotateRight(i.parent.parent)
            # if statement for root balance
            if i == inside.root:
                break
        inside.root.colour = 0

    # Tree output 
    def printTree(inside, node, indent, last):
        if node != inside.Tempty:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            
            v_colour = "RED" if node.colour == 1 else "BLACK"
            print(str(node.type) + "(" + v_colour + ")")
            inside.printTree(node.left, indent, False)
            inside.printTree(node.right, indent, True)

    def preorder(inside):
        inside.pre_order(inside.root)
    
    def inorder(inside):
        inside.in_order(inside.root)

    def postorder(inside):
        inside.post_order(inside.root)

    def search(inside, i):
        return inside.searchTree(inside.root, i)

    def min(inside, node):
        while node.left != inside.Tempty:
            node = node.left
        return node

    def max(inside, node):
        while node.right != inside.Tempty:
            node = node.right
        return node

    # left rotation
    def rotateLeft(inside, x):
        y = x.right
        x.right = y.left
        if y.left != inside.Tempty:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            inside.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # right rotation
    def rotateRight(inside, x):
        y = x.left
        x.left = y.right
        if y.right != inside.Tempty:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            inside.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    # Insertion of Red Black Tree
    def insert(inside, key):
        node = Node(key)
        node.parent = None
        node.type = key
        node.left = inside.Tempty
        node.right = inside.Tempty
        node.colour = 1

        y = None
        x = inside.root

        while x != inside.Tempty:
            y = x
            if node.type < x.type:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            inside.root = node
        elif node.type < y.type:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.colour = 0
            return

        if node.parent.parent == None:
            return

        inside.insertion(node)

    def get_root(inside):
        return inside.root

    def print_tree(inside):
        inside.printTree(inside.root, "", True)

# Executes main function
if __name__ == "__main__":
    bst = RBT()

    bst.insert(2)
    bst.insert(13)
    bst.insert(7)
    bst.insert(16)
    bst.insert(19)
    bst.insert(9)
    bst.insert(22)
    bst.insert(10)
    bst.insert(14)
    bst.insert(17)

    bst.print_tree()