
from __future__ import annotations  
from dataclasses import dataclass
from collections import deque
from typing import Callable, Generic, List, Optional, Sequence, Tuple
from datastructures.iavltree import IAVLTree, K,V

#command dot or control dot to get the code actions
#need to get python 12
#create a class called AVLTree that implememts the IAVLTree interface
#from iavltree.py
#implement all interface functions definced in IAVLTree

# datastructures.avltree.AVLNode
"""class AVLNode(Generic[K, V]): #creating a class for our AVL nodes, which take a generic (aka not specific) key and value pairs. 


    def __init__(self, key: K, value: V, left: Optional[AVLNode]=None, right: Optional[AVLNode]=None):

        self._key = key  # Initializing the key of the node


        self._value = value  # Initializing the value of the node


        self._left = left  # Initializing the left child


        self._right = right  # Initializing the right child


        self._height = 1  # Setting the initial height of the node


    @property

    def key(self) -> K: #Defining a getter for the key

        return self._key


    @key.setter

    def key(self, new_key: K) -> None: #setter for the key

         self._key = new_key
"""



class AVLNode(Generic[K, V]):
    def __init__(self, key: K, value: V, left: Optional[AVLNode]= None, right: Optional[AVLNode]=None): 
        self._key = key  # Initializing the key of the node


        self._value = value  # Initializing the value of the node


        self._left = left  # Initializing the left child


        self._right = right  # Initializing the right child


        self._height = 1

        self._balance_factor = 0

    @property
    def key(self) -> K: 
        return int(self._key)
    @key.setter
    def key(self, new_key: K) -> None: #setter for the key
         self._key = new_key
    @property
    def value(self) -> V: 
        return self._value
    @property
    def left(self) -> Optional[AVLNode]: 
        return self._left
    @left.setter
    def left(self, left: Optional[AVLNode]) -> None: 
        self._left = left
    @property
    def right(self) -> Optional[AVLNode]: 
        return self._right
    @right.setter
    def right(self, right: Optional[AVLNode]) -> None: 
        self._right = right
    @property
    def height(self) -> int: 
        return self.height
    @height.setter
    def height(self, height: int) -> None: 
        self.height = height
    @property
    def balance_factor(self) -> int: 
        return self._balance_factor
    @balance_factor.setter
    def balance_factor(self, balance_factor:int) -> None: 
        self.balance_factor = balance_factor


class AVLTree(IAVLTree[K,V], Generic[K,V]):

    def __init__(self, starting_sequence: Optional[Sequence[Tuple]]=None):


        self._root = None #initalizes the root


        self.size = 0 #initalizes the size


        if starting_sequence: #if starting pair(?) is provided put those in

            for key, value in starting_sequence:

                self.insert(key, value)
    
    def rotate_right(self, root: AVLNode) -> AVLNode:
        new_root = root.left #make sure new_root exists( is not none) before you continue
        new_right_subtree = new_root.right
        new_root.left = root
        root.right = new_right_subtree
        root.height = 1 + max(new_root.left.height, new_root.right.height) #fix this line
        new_root.height = max(new_root.left.height, new_root.right.height) #fix this line


        """y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y"""
    def rotate_left(self, root: AVLNode) -> AVLNode:
        new_root = root.right #make sure new_root exists( is not none) before you continue
        new_left_subtree = new_root.left
        new_root.left = root
        root.right = new_left_subtree
        root.height = 1 + max(new_root.left.height, new_root.right.height)
        new_root.height = max(new_root.left.height, new_root.right.height)
    
    def _balance_tree(self,node) -> AVLNode:
        #if LL issue:
        if node.balance_factor >1 and node.left.balance_factor >=0:
            return self.rotate_right(node)
        #if RR issue:
        if node.balance_factor < 1 and node.right.balance_factor <= 0:
            return self.rotate_left(node)
        #if LR issue
        """if  (node._left._height if node._left else 0) - (node._right._height if node._right else 0)<0: #if the equation is equal to less than zero, we need to rotate the left child to become the new main node, and then rotate it

            node._left = self.rotate_left(node._left)

            return self.rotate_right(node)"""
        #mine LR
        if node.balance_factor >1 and node._left.balance_factor <=0:
            self.rotate_left(node._left)
            return self.rotate_right(node)
        #if RL issue- double check, I am very unsure
        if node.balance_factor < -1 and node.right.balance_factor :
            self.rotate_right(node._right)
            return self.rotate_left(node)
    
        else:
            return node
            """def _balance_tree(self, node: AVLNode) -> AVLNode:
    
            LL:
            do a right rotation on node, 
            then return node
            RR:
            do a left rotation on node,
            then return node
            LR: 
            do a left rotation on node.left
            do a right rotation on node
            then return node
            RL:
            do a right rotation on node.right
            do a left rotation on node
            then return node

            Else: 
            no rotations needed! 
            just return the node"""

    def _height(self, node: AVLNode) -> int: 
        return node.height if node else 0

    def insert(self, key: K, value: V) -> None:
            # Public method 
        self._root = self._insert(self._root, key, value)

    # Private method (helper)
    def _insert(self, node: Optional[AVLNode], key: K, value: V) -> AVLNode:
    
    #1. base case (node is None)
        #return a new AVLNode
        if node is None:
            return AVLNode(key,value)
        #2. recursive cases
        elif key < node.key:
            node.left = self._insert(node._left, key, value)
        else:
            #traverse right, 
            node.right = self._insert(node._right, key, value)
        
        left_height = node._left._height if node._left is not None else 0
        right_height = node._right._height if node._right is not None else 0
        #3. bookkeeping
            #Update nodes height
        node.height = 1+ max(left_height, right_height)
        
        #4. balance the tree
        return self._balance_tree(node)
        
        
        #return the balanced tree- which could be a list or something else
        
        """#code from geeks for geeks website
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left rotation
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Right rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root"""

                
            
            
        #raise NotImplementedError

    def search(self, key: K) -> V | None:
        
        raise NotImplementedError

    def delete(self, key: K) -> None:
        #once a node is deleted, then you have to check the balance factor to make sure
        #that it is in the set. If not, then call another function to balance it?
        #should search be used to find the node before trying to delete it?


        raise NotImplementedError

    def inorder(self, visit: Callable[[V], None] | None = None) -> List[K]:
        def _inorder(node: Optional[AVLNode]) -> AVLNode:
            if not node: #if the node does not exist
                return
            _inorder(node.left)
            if visit:
                visit(node.value)
            _inorder(node.right) 

        keys: List[K] = []
        _inorder(self._root)
        return keys

    def preorder(self, visit: Callable[[V], None] | None = None) -> List[K]:
        #Returns the preorder traversal of the binary search tree
        def _preorder(node: Optional[AVLNode]) -> AVLNode:
            if not node: #if the node does not exist
                return
            _preorder(node)
            if visit:
                visit(node.value)
            _preorder(node.left)
            _preorder(node.right) 

        keys: List[K] = []
        _preorder(self._root)
        return keys

    def postorder(self, visit: Callable[[V], None] | None = None) -> List[K]:
        #Returns the postorder traversal of the binary search tree
        def _postorder(node: Optional[AVLNode]) -> AVLNode:
            if not node: #if the node does not exist
                return
            _postorder(node.left)
            if visit:
                visit(node.value)
            _postorder(node.right)
            _postorder(node) 

        keys: List[K] = []
        _postorder(self._root)
        return keys
    

    def bforder(self, visit: Callable[[V], None] | None = None) -> List[K]:
        if not self._root:
            return []
        
        keys: List[K] = []
        queue = deque()
        queue.append(self._root)
        while queue:
            node = queue.popleft()
            if visit:
                visit(node.value)
            keys.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return keys

    def size(self) -> int:
       
       
        raise NotImplementedError


    def __str__(self) -> str:
        def draw_tree(node: Optional[AVLNode], level: int=0) -> None:
            if not node:
                return 
            draw_tree(node.right, level + 1)
            level_outputs.append(f'{" " * 4 * level} -> {str(node.value)}')
            draw_tree(node.left, level + 1)
        level_outputs: List[str] = []
        draw_tree(self._root)
        return '\n'.join(level_outputs)