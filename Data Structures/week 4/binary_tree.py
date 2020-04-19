class BinaryTree:
    def __init__(self, rootObj):
        # the root object of a tree can be a reference to any object
        self.key = rootObj 
        self.leftChild  = None
        self.rightChild = None
       
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else: # a node with an existing left child
            # insert a node and push the existing child down one level in the tree
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild # attach the orignal left child to t
            self.leftChild = t # replace the original left child with the new node
        
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self, obj):
        self.key = obj
        
    def getRootVal(self):
        return self.key
    

def buildTree():
    tree = BinaryTree('a')
    tree.insertLeft('b')
    tree.insertRight('c')
    tree.getLeftChild().insertRight('d')
    tree.getRightChild().insertLeft('e')
    tree.getRightChild().insertRight('e')
    return tree

ttree = buildTree()

ttree.getRightChild().getRootVal()
ttree.getLeftChild().getRightChild().getRootVal()
ttree.getRightChild().getLeftChild().getRootVal()



