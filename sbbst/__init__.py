from __future__ import print_function, absolute_import, unicode_literals, division

# Tree Node with different things that helps to build the AVL Tree
class TreeNode():
    # It instantiates the class
    def __init__ (self, val):
        self.val = val
        self.place = 0
        self.height = 1
        self.left = None
        self.right = None

# Self Balancing Binary Search Tree based on the type of AVL Trees
class sbbst():
    # It instantiates the class O(1)
    def __init__(self, valslist = None):
        self.head = None
        self.N = 0
        self.count = 0
        self.sizes = []
        self.sumsizes = []
        self.listInOrder = []
        if type(valslist) == list:
            for val in valslist:
                self.head = self.insertNode(self.head, val)

    # It return True if the val is found, False otherwhise O(logN)
    def search(self, node, val):
        if not node:
            return False
        else:
            if node.val < val:
                return self.search(node.right, val)
            elif val < node.val:
                return self.search(node.left, val)
            else:
                return True

    # It inserts a node and updates the head node O(logN)
    def insert(self, val):
        self.head = self.insertNode(self.head, val)
    
    # It inserts a node with a value and returns the node of the modified subtree O(logN)
    def insertNode(self, node, key):
        # Step 1 - Perform normal BST
        if not node:
            self.N += 1
            return TreeNode(key)
        
        elif key < node.val:
            node.left = self.insertNode(node.left, key)
        else:
            node.right = self.insertNode(node.right, key)
        
        # 2: Update the height of the node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        # 3: Get the balance factor
        balance = self.getBalance(node)
        # 4: If the node is unbalanced, try out the 2 cases
        if balance > 1: # Case 1: Left (Left/Right)
            if key > node.left.val:
                node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1: # Case 2: Right (Left/Right)
            if key < node.right.val:
                node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        # Return the result node
        return node

    # It deletes a node with a certain value and updates the head node O(logN)
    def delete(self, val):
        self.head = self.deleteNode(self.head, val)

    # It deletes a node with a certain value and returns the node of the modified subtree O(logN)
    def deleteNode(self, node, key):
        # 1: Standard BST delete
        if not node:
            return node

        elif key < node.val:
            node.left = self.deleteNode(node.left, key)
        elif key > node.val:
            node.right = self.deleteNode(node.right, key)

        else: # key == node.val            
            if node.left is None:
                self.N -= 1
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                self.N -= 1
                temp = node.left
                node = None
                return temp
            else: # node.left and node.right
                temp = self.getMinValueNode(node.right)
                node.val = temp.val
                node.right = self.deleteNode(node.right, temp.val)

        # Return None if there is no more nodes
        if node is None:
            return node
        # 2: Update the height of the node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        # 3: Get the balance factor
        balance = self.getBalance(node)
        # 4: If the node is unbalanced, try out the 2 cases
        if balance > 1: # Case 1: Left (Left/Right)
            if self.getBalance(node.left) < 0:
                node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1:# Case 2: Right (Right/Left)
            if self.getBalance(node.right) > 0:
                node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        # Return the result node
        return node 
    
    # It rotates the tree to the left and returns the node O(1)
    def leftRotate(self, node):
        rnode = node.right
        T = rnode.left
        # Perform rotation
        rnode.left = node
        node.right = T
        # Update heights
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        rnode.height = 1 + max(self.getHeight(rnode.left), self.getHeight(rnode.right))
        # Return the new node
        return rnode

    # It rotates the tree to the right and returns the node O(1)
    def rightRotate(self, node):
        lnode = node.left
        T = lnode.right
        # Perform rotation
        lnode.right = node
        node.left = T
        # Update heights
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        lnode.height = 1 + max(self.getHeight(lnode.left), self.getHeight(lnode.right))
        # Return the new node
        return lnode

    # It returns the height of a node O(1)
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    # It returns the balance of the node O(1)
    def getBalance(self, node): 
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    # It returns the min Node O(logN)
    def getMinValueNode(self, node):
        if node is None or node.left is None:
            return node
        return self.getMinValueNode(node.left)

    # It returns the min value of the Tree O(logN + K)
    def kthsmallest(self, K):
        if K < 0:
            print('There are not enough elements in the Tree')
            return None
        elif self.N//2+1 < K:
            return self.kthlargest(self.N+1-K)
        else:
            stack = []
            node = self.head
            while(stack or node):
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    if K == 1:
                        return node.val
                    else:
                        K -= 1
                    node = node.right
    
    # It returns the max value of the Tree O(losgN + K)
    def kthlargest(self, K):
        if K < 0:
            print('There are not enough elements in the Tree')
            return None
        elif self.N//2+1 < K:
            return self.kthsmallest(self.N+1-K)
        else:
            stack = []
            node = self.head
            while(stack or node):
                if node:
                    stack.append(node)
                    node = node.right
                else:
                    node = stack.pop()
                    if K == 1:
                        return node.val
                    else:
                        K -= 1
                    node = node.left

    # It returns the min value of the Tree O(logN + K)
    def getMinVal(self, node=-1):
        if node == -1:
            if self.head == None:
                print('No elements in the Tree')
                return float('inf')
            else:
                node = self.head
        if node.left:
            return self.getMinVal(node.left)
        else:
            return node.val

    # It returns the max value of the Tree O(logN)
    def getMaxVal(self, node=-1):
        if node == -1:
            if self.head == None:
                print('No elements in the Tree')
                return float('-inf')
            else:
                node = self.head
        if node.right:
            return self.getMaxVal(node.right)
        else:
            return node.val

    # It returns the number of elements in the Tree O(1)
    def getSize(self):
        return self.N
    
    # It returns the height of the Tree O(1)
    def getHeightTree(self):
        if self.head == None:
            return 0
        return self.head.height

    # It returns a list in pre Order of the Tree O(N)
    def preOrder(self, node=-1):
        if node == -1:
            node = self.head
        if node:
            return [node.val] + self.preOrder(node.left) + self.preOrder(node.right)
        else:
            return []

    # It returns a list in Order of the Tree O(N)
    def inOrder(self, node=-1):
        if node == -1:
            node = self.head
        if node:
            return self.inOrder(node.left) + [node.val] + self.inOrder(node.right)
        else:
            return []

    # It returns a list in post Order of the Tree O(N)
    def postOrder(self, node=-1):
        if node == -1:
            node = self.head
        if node:
            return self.postOrder(node.left) + self.postOrder(node.right) + [node.val]
        else:
            return []

    # It updates the place of each node and get the list of nodes in Order O(N)
    def getListInOrder(self, node=-1):
        if node == -1:
            self.count = 0
            node = self.head
            self.listInOrder = []
        if node:
            self.getListInOrder(node.left)
            self.listInOrder.append(node.val)
            node.place = self.count
            self.count += 1
            self.getListInOrder(node.right)

    # It updates the lists of the size of each value of nodes O(N)
    def lenNodes(self):
        self.sizes = []
        self.sumsizes = []
        for x in self.listInOrder:
            self.sizes.append(len(str(x)))
        past = 1
        for x in self.sizes:
            self.sumsizes.append(past)
            past += x
        self.sumsizes.append(past)

    # It returns the full draw of the tree in 2dimensions O(N)
    def __str__(self):
        self.getListInOrder()
        self.lenNodes()
        if self.head == None:
            return 'No elements in the Tree'

        outstr = '\n'
        queue = [self.head]
        while queue:
            aux = []
            past, nextpast = 0, 0
            line, nextline = '', ''
            for q in queue:
                if q.left and q.right:
                    aux.append(q.left)
                    aux.append(q.right)
                    # Print of the _ and the values of the nodes
                    line += ' '*(self.sumsizes[q.left.place+1]-past) + '_'*(self.sumsizes[q.place]-self.sumsizes[q.left.place+1]) + str(q.val) + '_'*(self.sumsizes[q.right.place]-self.sumsizes[q.place+1])
                    past = self.sumsizes[q.right.place]
                    # Print of the arms of the Tree
                    nextline += ' '*(self.sumsizes[q.left.place+1]-nextpast-1) + '/' + ' '*(self.sumsizes[q.right.place]-self.sumsizes[q.left.place+1]) + '\\' + ' '*(self.sizes[q.right.place]-1)
                    nextpast = self.sumsizes[q.right.place+1]
                elif q.left:
                    aux.append(q.left)
                    # Print of the _ and the values of the nodes
                    line += ' '*(self.sumsizes[q.left.place+1]-past) + '_'*(self.sumsizes[q.place]-self.sumsizes[q.left.place+1]) + str(q.val)
                    past = self.sumsizes[q.place+1]
                    # Print of the arms of the Tree
                    nextline += ' '*(self.sumsizes[q.left.place+1]-nextpast-1) + '/'
                    nextpast = self.sumsizes[q.left.place+1]
                elif q.right:
                    aux.append(q.right)
                    # Print of the _ and the values of the nodes
                    line += ' '*(self.sumsizes[q.place]-past)+str(q.val)+'_'*(self.sumsizes[q.right.place]-self.sumsizes[q.place+1])
                    past = self.sumsizes[q.right.place]
                    # Print of the arms of the Tree
                    nextline += ' '*(self.sumsizes[q.right.place]-nextpast) + '\\' + ' '*(self.sizes[q.right.place]-1)
                    nextpast = self.sumsizes[q.right.place+1]
                else:
                    line += ' '*(self.sumsizes[q.place]-past)+str(q.val)
                    past = self.sumsizes[q.place+1]
            # Add the lines to the output string
            outstr += line + '\n' + nextline + '\n'
            queue = aux
        return outstr[:-1]

# It returns the head of the Tree that was build with the plane Tree "s"
def getTree(s):
    if type(s) == str:
        if ',' in s:
            key = ','
            s.replace(' ','')
        else:
            key = ' ' 
        aux = s.split(key)
        key = 'null' if 'null' in aux else ('None' if 'None' in aux else '-1')
        mylist = [None if x == key else int(x) for x in aux]
    elif type(s) == list and 0 < len(s) and type(s[0]) == int:
        mylist = s if None in s else [None if x == -1 else int(x) for x in s]
    else:
        print('Wrong format for the input')
        return None
    # Stars building the tree
    head = TreeNode(mylist[0])
    queue = [head]
    i = 1
    while queue:
        aux = []
        for q in queue:
            if mylist[i] != None:
                q.left = TreeNode(mylist[i])
                aux.append(q.left)
            i += 1
            if mylist[i] != None:
                q.right = TreeNode(mylist[i])
                aux.append(q.right)
            i += 1
        queue = aux
    return head

# It returns the full draw of the tree in 2dimensions O(N)
def getStr(head):
    if head == None:
        return 'No elements in the Tree'
    # Gets the in-order list of the values and its place
    listInOrder, stack = [], []
    node = head
    count = 0
    while(stack or node):
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            listInOrder.append(node.val)
            node.place = count
            count += 1
            node = node.right
    # Gets the sizes of each node
    sizes, sumsizes = [], []
    for x in listInOrder:
        sizes.append(len(str(x)))
    past = 1
    for x in sizes:
        sumsizes.append(past)
        past += x
    sumsizes.append(past)
    # Builds the output string
    outstr = '\n'
    queue = [head]
    while queue:
        aux = []
        past, nextpast = 0, 0
        line, nextline = '', ''
        for q in queue:
            if q.left and q.right:
                aux.append(q.left)
                aux.append(q.right)
                # Print of the _ and the values of the nodes
                line += ' '*(sumsizes[q.left.place+1]-past) + '_'*(sumsizes[q.place]-sumsizes[q.left.place+1]) + str(q.val) + '_'*(sumsizes[q.right.place]-sumsizes[q.place+1])
                past = sumsizes[q.right.place]
                # Print of the arms of the Tree
                nextline += ' '*(sumsizes[q.left.place+1]-nextpast-1) + '/' + ' '*(sumsizes[q.right.place]-sumsizes[q.left.place+1]) + '\\' + ' '*(sizes[q.right.place]-1)
                nextpast = sumsizes[q.right.place+1]
            elif q.left:
                aux.append(q.left)
                # Print of the _ and the values of the nodes
                line += ' '*(sumsizes[q.left.place+1]-past) + '_'*(sumsizes[q.place]-sumsizes[q.left.place+1]) + str(q.val)
                past = sumsizes[q.place+1]
                # Print of the arms of the Tree
                nextline += ' '*(sumsizes[q.left.place+1]-nextpast-1) + '/'
                nextpast = sumsizes[q.left.place+1]
            elif q.right:
                aux.append(q.right)
                # Print of the _ and the values of the nodes
                line += ' '*(sumsizes[q.place]-past)+str(q.val)+'_'*(sumsizes[q.right.place]-sumsizes[q.place+1])
                past = sumsizes[q.right.place]
                # Print of the arms of the Tree
                nextline += ' '*(sumsizes[q.right.place]-nextpast) + '\\' + ' '*(sizes[q.right.place]-1)
                nextpast = sumsizes[q.right.place+1]
            else:
                line += ' '*(sumsizes[q.place]-past)+str(q.val)
                past = sumsizes[q.place+1]
        # Add the lines to the output string
        outstr += line + '\n' + nextline + '\n'
        queue = aux
    return outstr[:-1]

# it Returns the Tree in its plane form
def getList(Node):
    treeList = []
    stack = [Node]
    while stack:
        q = stack.pop()
        if q:
            treeList.append(q.val)
            stack.append(q.right)
            stack.append(q.left)
        else:
            treeList.append(None)
    return treeList
