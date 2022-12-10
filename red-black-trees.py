import sys
import random 

global Red
global Black

#initialise red and black values 
Red = 1
Black = 0

#node creation
class Node():
    def __init__(self, value):
        self.value = value   # value of node
        self.colour = Red    # new node must be RED  → note: Red = 1, Black = 0
        self.parent = None   # parent of node 
        self.left = None     # left child of node
        self.right = None    # right child of node
# Define red black tree 
class RBT():
    global NUL
    def __init__(self):
        self.NUL = Node(0)
        self.NUL.left = None
        self.NUL.right = None
        self.NUL.colour = 0
        self.root = self.NUL

    # preorder
    def pre_order(self, node):
        if node != NUL:
            print(node.item + " ")
            self.pre_order(node.left)
            self.pre_order(node.right)
    # postorder
    def post_order(self, node):
        if node != NUL:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.item + " ")
    
    # search operation of red black tree
    def searchTree(self, node, key):
        if node == NUL or key == node.value:
            return node 
    
    """ 
    Balances insert operation of red black tree overflowing nodes from bottom to top
    """
    def balanceInsert(self, new_node):
        while new_node.parent.colour == Red:                       # while parent = red
            if new_node.parent == new_node.parent.parent.right:    # if parent subtree == right child
                uncle = new_node.parent.parent.left                # left child of grandparent
                """ if colour of left child of grandparent i.e uncle node == RED
                    set grandchildren of grandparent node as BLACK
                """
                if uncle.colour is Red:
                    uncle.colour == 0
                    new_node.parent.colour = 0
                    new_node.parent.parent.colour = Red            # Set grandparent node as RED
                    new_node = new_node.parent.parent              # Repeat parent node to remove conflicts
                else:
                    if new_node == new_node.parent.left:           # if newnode left child of parent
                        new_node = new_node.parent                 # Call right rotation
                        self.rotateRight(new_node)
                    new_node.parent.colour = 0
                    new_node.parent.parent.colour = Red
                    self.rotateLeft(new_node.parent.parent)
            else:                                                  # If parent is left child of parent 
                uncle = new_node.parent.parent.right               # Then Right child of grandparent
                """ If colour of right child of granparent i.e uncle node == RED
                    set grandchildren of grandparent node as BLACK
                """                                                   
                if uncle.colour is Red:                                   
                    uncle.colour = 0
                    new_node.parent.colour = 0
                    new_node.parent.parent.colour = Red           # Set granparent node as RED
                    new_node = new_node.parent.parent             # Repeat node to remove conflicts
                else: 
                    if new_node == new_node.parent.right:         # if newnode right child of its parent
                        new_node = new_node.parent
                        self.rotateLeft(new_node)                 # Call left rotation on parent
                    new_node.parent.colour = 0
                    new_node.parent.parent.colour = Red
                    self.rotateRight(new_node.parent.parent)      # Call right rotation on grandparent
            # if statement for root balance
            if new_node == self.root:                             # When newnode reaches root, break loop
                break
        self.root.colour = Black                                  # Set root colour == Black

    # Tree output 
    def printTree(self, node, space, last):
        if node != self.NUL:
            sys.stdout.write(space) # returns length of the string of space indentation
            if last:
                sys.stdout.write("R----")
                space += "     "
            else:
                sys.stdout.write("L----")
                space += "|    "
            
            v_colour = "RED" if node.colour == 1 else "BLACK"
            print(str(node.value) + "(" + v_colour + ")")
            self.printTree(node.left, space, False)
            self.printTree(node.right, space, True)

    def preorder(self):
        self.pre_order(self.root)

    def postorder(self):
        self.post_order(self.root)

    def search(self, new_node):
        return self.searchTree(self.root, new_node)

    def min(self, node):
        while node.left != self.NUL:
            node = node.left
        return node

    def max(self, node):
        while node.right != self.NUL:
            node = node.right
        return node
    
    # left rotation
    def rotateLeft(self, x):
        y = x.right # y is equivalent to right child of x
        # switch to y's left child from x's right child
        x.right = y.left
        if y.left != self.NUL:
            y.left.parent = x
        # y's new parent was x's parent
        y.parent = x.parent
        """ 
        Parent set to point y instead of x to check whether we're at the root 
        """
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            # x was positioned left of its parent
            x.parent.left = y
        else:
            # x positioned on the right
            x.parent.right = y
        # Apply x on y's left 
        y.left = x
        x.parent = y

    # right rotation
    def rotateRight(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NUL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    
    # Insertion of Red Black Tree
    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.value = key
        node.left = self.NUL
        node.right = self.NUL
        node.colour = Red   # root colour set to RED

        y = None
        x = self.root

        while x != self.NUL: # searches position for new node
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        # y is set as the parent of node 
        node.parent = y
        # if parent is NUL, then it identifies as root
        if y == None:
            self.root = node
        # Check whether its in right or left node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node
        # Root node always set to BLACK
        if node.parent == None:
            node.colour = 0
            return
        """ If parent of node is root, perfect. 
            Otherwise, insertion is balanced by using function call.
        """
        if node.parent.parent == None:
            return

        self.balanceInsert(node)

    def get_root(self):
        return self.root

    def print_tree(self):
        self.printTree(self.root, "", True)

# Executes main function
if __name__ == "__main__":
    bst = RBT()
    # test with dummy data given  
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