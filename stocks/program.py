from __future__ import annotations
from collections import deque
from dataclasses import dataclass

from typing import Callable, Generic, List, Optional, Sequence, Tuple
from datastructures.iavltree import IAVLTree, K, V
from datastructures.avltree import AVLTree, K, V

#from dataclasses import dataclass
#from datastructures intervaltree import IntervalTree
#from datastructures avltree import AVLTree


class IntervalTree:
    def __init__(self, starting_sequence: Optional[Sequence[Tuple[str, Stock]]] = None) -> None:
        self._stock_tree: AVLTree[str, IntervalNode] = AVLTree()
        if starting_sequence:
            for symbol, stock in starting_sequence:
                self.insert(symbol, stock.low, stock.high, stock.price)

    def insert(self, key: str, low: int, high: int, price: float) -> None:
        stock = Stock(low, high, key, price)

        existing_node = self._stock_tree.search(key)
        if existing_node is not None:
            # Update existing stock
            existing_node.stock.price = price  
            existing_node.add_interval(low, high)  
        else:
            # Insert new stock
            new_node = IntervalNode(stock)
            new_node.add_interval(low, high)
            self._stock_tree.insert(key, new_node)
        





@dataclass(order=True)
class Stock:
    symbol: str
    name: str
    low: int
    high: int
@dataclass(order=True)
class Stock:
    low: int
    high: int
    symbol: str
    price: float

class IntervalNode:
    def __init__(self, stock: Stock) -> None:
        self.stock: Stock = stock
        # AVL tree to manage intervals
        self._intervals: AVLTree[int, Tuple[int, int]] = AVLTree() 

    def add_interval(self, low: int, high: int) -> None:
      	# Insert the interval into the AVL tree
        self._intervals.insert(low, (low, high))  

 
class StockManager:
    def __init__(self) -> None:
        self._interval_tree = IntervalTree()

        stocks = [
            Stock("GOOGL", 'Alphabet Inc.',173,213)
        ]

        for stock in stocks:
            #idk make the tree


class IntervalNode:
    def __init__(self, stock: Stock) -> None:
        self.stock: Stock = stock
        # AVL tree to manage intervals
        self._intervals: AVLTree[int, Tuple[int, int]] = AVLTree() 

    def add_interval(self, low: int, high: int) -> None:
      	# Insert the interval into the AVL tree
        self._intervals.insert(low, (low, high))  



def main():
    tree = AVLTree()
    print("Hi!!!")

if __name__ == "__main__":
    main()