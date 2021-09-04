#Complete the following tasks:
#1. Write an add method to BinaryTree
#2. Create an instance of BinaryTree
#3. Add items to BinaryTree
#4. Add a 'exist' method that searches for an item in the tree and returns true if it exists
#5. Add depth-first traversals (pre, in, post)
#6. Add breadth-first traversals (you need to build a queue data structure for this)
#7. Add a display method to visualise the tree
#Ext 1. Add a delete method using 'Hibbard Deletion'
#Ext 2. Create a new class based on this one for normal, multi-branch trees

class Node:
  def __init__(self, item):
    self.item = item
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None
    self.number = 0

  def add(self, item):
    newNode = Node(item)
    if(self.root == None):
      self.root = newNode
    else:
      completed = False
      current = self.root
      while(completed == False):
        if(newNode.item < current.item and current.left != None):
          current = current.left
        elif(newNode.item < current.item and current.left == None):
          current.left = newNode
          newNode.parent = current
          completed = True
        elif(newNode.item > current.item and current.right != None):
          current = current.right
        elif(newNode.item > current.item and current.right == None):
          current.right = newNode
          newNode.parent = current
          completed = True
        elif(newNode.item == current.item):
          completed = True
          self.number -= 1
    self.number += 1


  #only works for deleting nodes with 0 or 1 children
  def delete(self, item):
    find = self.search(item, self.root)
    if(find.left == None and find.right == None):
      if(find.parent.left == find):
        find.parent.left = None
      else:
        find.parent.right = None
    
    elif(find.left == None and find.right != None):
      if(find.parent.left == find):
        find.parent.left = find.right
      else:
        find.parent.right = find.right

    elif(find.left != None and find.right == None):
      if(find.parent.left == find):
        find.parent.left = find.left
      else:
        find.parent.right = find.left

    self.number -= 1

  
  def exist(self, item, root):
    current = root
    if(current.item == item):
      return True
    else:
      if(current.left != None):
        if(self.exist(item, current.left) == True):
          return True
      if(current.right != None):
        if(self.exist(item, current.right) == True):
          return True
    return False


  #Function to search for any item and return its node object
  def search(self, item, root):
    if(self.root == None):
      return

    queue = Queue(self.number)
    queue.push(self.root)
  
    while(queue.head <= queue.tail):
      current = queue.pop()
      if(current.item == item):
        return current

      if(current.left != None):
        queue.push(current.left)
      if(current.right != None):
        queue.push(current.right)
    
    return None
    

  def BFS(self):
    if(self.root == None):
      return

    traversal = []
    queue = Queue(self.number)
    queue.push(self.root)
  
    while(queue.head <= queue.tail):
      current = queue.pop()
      traversal.append(current.item)

      if(current.left != None):
        queue.push(current.left)
      if(current.right != None):
        queue.push(current.right)
         
    return traversal

  
  def preorder(self, root, traversal):
    traversal = traversal
    if root == None:
      return 
    traversal.append(root.item)
    self.preorder(root.left, traversal)
    self.preorder(root.right, traversal)

    return traversal
  
  def inorder(self, root, traversal):
    traversal = traversal
    if(root == None):
      return
    
    self.inorder(root.left, traversal)
    traversal.append(root.item)
    self.inorder(root.right, traversal)

    return traversal

  def postorder(self, root, traversal):
    traversal = traversal
    if(root == None):
      return
    
    self.postorder(root.left, traversal)
    self.postorder(root.right, traversal)
    traversal.append(root.item)
    return traversal

  def display(self, root, space):
    increment = 15
    if(root == None):
      return
    space += increment
    self.display(root.right, space)
    print("")
    for x in range(increment, space):
      print(end = " ")
    print(root.item)

    self.display(root.left, space)




class Queue:
  def __init__(self, capacity):
    self.capacity = capacity
    self.queue = [None]*capacity
    self.head = 0
    self.tail = -1

  def pop(self):
    if(self.tail - self.head >= 0):
      temp = self.queue[self.head % self.capacity]
      self.head += 1
      return temp

  def push(self, item):
    if(self.tail - self.head < self.capacity-1):
      self.tail += 1
      self.queue[self.tail % self.capacity] = item

  



tree = BinaryTree()


#Root is Liverpool
tree.add("Liverpool")

tree.add("Cardiff")
tree.add("Durham")
tree.add("Manchester")
tree.add("Aberdeen")
tree.add("Bath")
tree.add("Narnia")
tree.add("London")
tree.add("Reading")




print(tree.exist("London", tree.root))
print(tree.exist("Eton", tree.root))

print(tree.exist("Reading", tree.root))
print("")

print(tree.search("Reading", tree.root).item)

tree.display(tree.root, 0)
print("")
print("")


print("BFS traversal is: ", end = '')
print(tree.BFS())

traversal = []
print("Preorder traversal is: ", end = '')
print(tree.preorder(tree.root, traversal))

traversal = []
print("Inorder traversal is: ", end = '')
print(tree.inorder(tree.root, traversal))

traversal = []
print("Postorder traversal is: ", end = '')
print(tree.postorder(tree.root, traversal))


tree.delete("Aberdeen")

print("")
print("")
print("")
print("New Tree:")
tree.display(tree.root, 0)

print("")
print("")

print("BFS traversal is: ", end = '')
print(tree.BFS())

traversal = []
print("Preorder traversal is: ", end = '')
print(tree.preorder(tree.root, traversal))

traversal = []
print("Inorder traversal is: ", end = '')
print(tree.inorder(tree.root, traversal))

traversal = []
print("Postorder traversal is: ", end = '')
print(tree.postorder(tree.root, traversal))

