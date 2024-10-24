
from __future__ import annotations  
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
        self._key = key  
        self._value = value  
        self._left = left  
        self._right = right  
        self._height = 1
        self._balance_factor = 0

    def __str__(self) -> str:
        output = f'K: {self._key} V: {self._value} Height: {self._height}'
        output += ' L: ' +  f'{self._left._key}' if self._left else 'None'
        output += ' R: ' + f'{self._right._key}' if self._right else 'None'

        return output
    
    def __repr__(self) -> str:
        return str(self)

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
        self._root = None
        self.size = 0 
        if starting_sequence: 
            for key, value in starting_sequence:
                self.insert(key, value)
    
    def _balance_factor(self, node: AVLNode) -> int:
        return self._node_height(node._left) - self._node_height(node._right) if node else 0

    def rotate_right(self, node: AVLNode) -> AVLNode:
        new_root = node._left

        if not new_root:
            raise Exception("new_root must exist")
        right_subtree = new_root._right
        new_root._right = node
        node._left = right_subtree

        node._height = 1 + max( 
            self._node_height(node._left),
            self._node_height(node._right)
        )
        new_root._height = 1 + max( 
            self._node_height(new_root._left),
            self._node_height(new_root._right)
        )

        return new_root
    def rotate_left(self, node: AVLNode) -> AVLNode:
        new_root=node._right
        if not new_root:
            raise Exception("new_root should exist")#make sure new_root exists( is not none) before you continue
        new_left_subtree = new_root._left
        new_root.left = node
        node._right = new_left_subtree
        node._height = 1 + max(self._node_height(node._left), self._node_height(node._right))
        new_root._height = 1 + max(self._node_height(new_root._left), self._node_height(new_root._right))

        return new_root

    
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

    def search(self, key: K) -> V | None:
        return self.search_helper(self._root, key)

    def search_helper(self, node: Optional[AVLNode], key: K) -> Optional[V]:
        if node is None:  
            return None
        elif node._key == key: 
            return node._value
        elif key < node._key:
            self.search_helper(node._left, key)
        else: 
            self.search_helper(node._right, key)


    def delete(self, key: K) -> None:
        #once a node is deleted, then you have to check the balance factor to make sure
        #that it is in the set. If not, then call another function to balance it?
        #should search be used to find the node before trying to delete it?
        self.root = self.delete_helper(self.root, key)

    def delete_helper(self, node: Optional[AVLNode], key: K) -> AVLNode | None:

        if node is None:  
            raise KeyError(f"Key {key} not found")

        elif key < node.key:  
            node._left = self.delete_helper(node._left, key)

        elif key > node.key:  
            node._right = self.delete_helper(node._right, key)

        else:  
            if node._left is None and node._right is None:  
                return None  
            elif node._left is None:  
                node = node._right
            elif node._right is None:  
                node = node._left
            else:
                successor = self.find_min(node._right)
                node._key = successor.key 
                node._value = successor.value
                node._right = self.delete_helper(
                    node._right, successor._key)  

        node.height = 1 + max(node._left._height if node._left else 0,
                          node._right._height if node._right else 0) - 1

        if (node._left._height if node._left else 0) - (node._right._height if node._right else 0) > 1:
            left_child = node._left  
            right_child = node._right

            if (left_child._left._height if left_child._left else 0) - (left_child._right._height if left_child._right else 0) >= 0:
                return self.rotate_right(node)
            else:  
                node._left = self.rotate_left(left_child)
                return self.rotate_right(node)

        elif (node._left._height if node._left else 0) - (node._right._height if node._right else 0) < -1:
            left_child = node._left
            right_child = node._right
            if (right_child._left._height if right_child._left else 0) - (right_child._right._height if right_child._right else 0) <= 0:
                return self.rotate_left(node)
            else:
                node._right = self.rotate_right(right_child)
                return self.rotate_left(node)

        return node


    def find_min(self, node: AVLNode) -> AVLNode:
        while node._left is not None:
            node = node._left 
        return node


    def inorder(self, visit: Optional[Callable[[V], None]] = None) -> List[K]:
        keys = []  
        self.inorder_helper(self._root, keys)
        return keys

    def inorder_helper(self, node: Optional[AVLNode], keys: List[K]) -> None:
        if node is None:  
            return None

        self.inorder_helper(node._left, keys)

        keys.append(node._key)  

        self.inorder_helper(node._right, keys)


    def preorder(self, visit: Optional[Callable[[V], None]] = None) -> List[K]:
        keys = [] 
        self.preorder_helper(self._root, keys)
        return keys

    def preorder_helper(self, node: Optional[AVLNode], keys: List[K]) -> None:
        if node is None: 
            return None
        keys.append(node._key) 
        self.preorder_helper(node._left, keys)  
        self.preorder_helper(node._right, keys)  

    def postorder(self, visit: Optional[Callable[[V], None]] = None) -> List[K]:
        keys = [] 
        self.postorder_helper(self._root, keys)
        return keys

    def postorder_helper(self, node: Optional[AVLNode], keys: List[K]) -> None:
        if node is None:  
            return None
        self.postorder_helper(node._left, keys)
        self.postorder_helper(node._right, keys)
        keys.append(node._key)

    """def bforder(self, visit: Optional[Callable[[V], None]] = None) -> List[K]:
        keys = []  
        queue = []  
        self.bforder_helper(queue, self._root, keys)
        return keys

    def bforder_helper(self, queue:  List[Optional[AVLNode]], node: Optional[AVLNode], keys: List[K]) -> None:
        if node is not None:  
            queue.append(node)
        
        while queue:  
            current = queue[0]  
            keys.append(current._key)  
            queue = queue[1:]  
            
            if current._left is not None:  
                queue.append(current._left)
            if current._right is not None:  
                queue.append(current._right)"""


    def size(self) -> int:
        return self.size_helper(self.root)

    def size_helper(self, node: Optional[AVLNode]) -> int:
        if node is None: 
            return 0

        return 1 + self.size_helper(node._left) + self.size_helper(node._right)


    def __str__(self) -> str:
        def draw_tree(node: Optional[AVLNode], level: int = 0) -> None:
            if not node:
                return
            draw_tree(node._right, level + 1)
            level_outputs.append(f'{" " * 4 * level} -> {str(node._value)}')
            draw_tree(node._left, level + 1)
        level_outputs: List[str] = []
        draw_tree(self._root)
        return '\n'.join(level_outputs)


    def __repr__(self) -> str:
        descriptions = ['Breadth First: ',
                        'In-order: ', 'Pre-order: ', 'Post-order: ']
        traversals = [self.bforder(), self.inorder(),
                      self.preorder(), self.postorder()]
        return f'{"\n".join([f'{desc} {"".join(str(trav))}' for desc, trav in zip(descriptions, traversals)])}\n\n{str(self)}'

    def inorder(self, visit: Callable[[V], None] | None = None) -> List[K]:
        def _inorder(node: Optional[AVLNode]) -> AVLNode:
            if not node: 
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