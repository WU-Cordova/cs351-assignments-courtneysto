# datastructures.ibinarysearchtree.IBinarySearchTree

"""
This module defines a Binary Search Tree interface. 
This file lists the stipulations and more information on the methods and their expected behavior.
YOU SHOULD NOT MODIFY THIS FILE.
"""

from abc import abstractmethod
from functools import total_ordering
from typing import Any, Callable, Protocol, TypeVar, Generic, Optional, List


@total_ordering
class Comparable(Protocol):
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...
        
K = TypeVar('K', bound=Comparable)  # Key type for ordering the nodes
V = TypeVar('V')  # Value type for storing associated data


class IAVLTree(Protocol, Generic[K, V]):
    """ A binary search tree is a binary tree data structure where nodes are ordered based on keys, 
    and each node stores an associated value. The left subtree contains only nodes with keys less 
    than the node's key, and the right subtree contains only nodes with keys greater than or equal
    to the node's key. Implementations of this interface should maintain the binary search tree 
    properties. Examples of binary search trees include AVL trees, red-black trees, and splay trees.
    """

    @abstractmethod
    def insert(self, key: K, value: V) -> None:
        """Inserts a key-value pair into the binary search tree.

            Args:
                key (K): The key used to order the nodes in the tree.
                value (V): The value associated with the key.
        """
        pass
    
    @abstractmethod
    def search(self, key: K) -> Optional[V]:
        """Searches for a key in the binary search tree and returns the associated value if found.

        Args:
            key (K): The key to search for.

        Returns:
            Optional[V]: The value associated with the key if found, or None if the key is not present.
        """
        pass

    @abstractmethod
    def delete(self, key: K) -> None:
        """Deletes a key and its associated value from the binary search tree.

        Args:
            key (K): The key to delete.

        Raises:
            KeyError: If the key is not present in the tree.
        """
        pass

    @abstractmethod
    def inorder(self, visit: Optional[Callable[[V], None]]=None) -> List[K]:
        """Returns the inorder traversal of the binary search tree, containing the keys in sorted order.

        Args:
            visit (Optional[Callable[[V], None]]): A function to call on each value during the traversal.        
        
        Returns:
            List[K]: The list of keys in inorder traversal.
        """
        pass

    @abstractmethod
    def preorder(self, visit: Optional[Callable[[V], None]]=None) -> List[K]:
        """Returns the preorder traversal of the binary search tree.

        Args:
            visit (Optional[Callable[[V], None]]): A function to call on each value during the traversal.        
        
        Returns:
            List[K]: The list of keys in preorder traversal.
        """
        pass

    @abstractmethod
    def postorder(self, visit: Optional[Callable[[V], None]]=None) -> List[K]:
        """Returns the postorder traversal of the binary search tree.

        Returns:
            List[K]: The list of keys in postorder traversal.
        """
        pass

    @abstractmethod
    def bforder(self, visit: Optional[Callable[[V], None]]=None) -> List[K]:
        """Returns the keys in the binary search tree in breadth-first order.

        Args:
            visit (Optional[Callable[[V], None]]): A function to call on each value during the traversal.        
        
        Returns:
            List[K]: The list of keys in breadth-first order.
        """
        pass

    @abstractmethod
    def size(self) -> int:
        """Returns the number of nodes in the binary search tree.

        Args:
            visit (Optional[Callable[[V], None]]): A function to call on each value during the traversal.        
        
        Returns:
            int: The number of nodes in the tree.
        """
        pass
