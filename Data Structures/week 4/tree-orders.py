# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    def inOrderRecursive(i,result):
          if self.left[i] != -1:
            inOrderRecursive(self.left[i],self.result)
          result.append(self.key[i])
          if self.right[i] != -1:
            inOrderRecursive(self.right[i],self.result)
    inOrderRecursive(0, self.result)         
    return self.result

  def preOrder(self):
    self.result = []
    def preOrderRecursive(i,result):
          result.append(self.key[i])
          if self.left[i] != -1:
            preOrderRecursive(self.left[i], self.result)
          if self.right[i] != -1:
            preOrderRecursive(self.right[i], self.result)
    preOrderRecursive(0, self.result)
    return self.result
            
            
  def postOrder(self):
    self.result = []
    def postOrderRecursive(i,result):
          if self.left[i] != -1:
            postOrderRecursive(self.left[i], self.result)
          if self.right[i] != -1:
            postOrderRecursive(self.right[i], self.result)
          result.append(self.key[i])
    postOrderRecursive(0, self.result)
    return self.result       
			    
def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
