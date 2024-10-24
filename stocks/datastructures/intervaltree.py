from __future__ import annotations

from datastructures import AVLTree
from dataclass import dataclass
from typing import Any, Tuple, Optional, List


"""From what I understand without reading too much, this file is where I create the interval
tree that is then used when I need to sort through the stocks and ranges and stuff. 
So basically, make all of the functions and helper functions in this file, i think
- everything with yellow squigglies may need to be rewritten or maybe something needs 
to be imported or in a diff file."""

@dataclass
class IntervalNode:
    key: Tuple[int,int]  
    value: Any
    left: Optional[IntervalNode] = None
    right: Optional[IntervalNode] = None
    height: int = 1
    max_end: int = 0
    intervals_at_low: AVLTree = AVLTree()




class IntervalTree:
    #if this works, then the interval tree should have all of the same properties
    #as the avl tree, such as insert and delete
    #I need to make sure that the kind of basic things work
    #also I simply need to understand everything, which would help a lot

    def __init__(self):
        self._tree = AVLTree()

    def insert(self,low:int,high:int,value: Any):
        node: IntervalNode = self._tree.search(low)

        if node:
            node.intervals_at_low.insert(high,value)

        else:
            new_node = IntervalNode(key=(low,high),value=value,max_end=high)
            new_node.intervals_at_low.insert(high,value)
            self._tree.insert(low, new_node)

        self._update_max_end(self._tree._root)
    
    def update_max_end(self, node: Optional[IntervalNode]):
        if not node:
            return 0
        left_max = self._update_max_end(node.left)
        right_max = self._update_max_end(node.right)
        max_end = max(left_max, right_max)

        node.max_end = max_end
        return node.max_end
    


    def top_k_stocks(self,k: int) -> List[K]:
        max_price_list: List[Tuple[V,K]] = {}

        def collect_max_price(node: Optional(IntervalNode)):
            if not node:
                return
            max_price_list.append((node._max_end, node.key))
            _collect_max_price(node_left)
            _collect_max_price(node.right)

        _collect_max_price(slef._root)

        max_price_list(sort(reverse=True, key=Lambda x: x[0]))
        return {key for _, key in max_price_list[k]}