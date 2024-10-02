

from typing import Callable, Generic, List
from datastructures.iavltree import IAVLTree, K,V

#command dot or control dot to get the code actions
#need to get python 12
#create a class called AVLTree that implememts the IAVLTree interface
#from iavltree.py
#implement all interface functions definced in IAVLTree

class AVLTree(IAVLTree[K,V], Generic[K,V]):
    def insert(self, key: K, value: V) -> None:
        raise NotImplementedError

    def search(self, key: K) -> V | None:
        raise NotImplementedError

    def delete(self, key: K) -> None:
        raise NotImplementedError

    def inorder(self, visit: Callable[[V], None] | None = None) -> List[K]:
        raise NotImplementedError

    def preorder(self, visit: Callable[[V], None] | None = None) -> List[K]:
        raise NotImplementedError

    def postorder(self, visit: Callable[[V], None] | None = None) -> List[K]:
        raise NotImplementedError

    def bforder(self, visit: Callable[[V], None] | None = None) -> List[K]:
        raise NotImplementedError

    def size(self) -> int:
        raise NotImplementedError
