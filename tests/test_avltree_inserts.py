import pytest

from datastructures.avltree import AVLTree

class TestAVLInserts():
    @pytest.fixture
    def avltree(self) -> AVLTree:
        tree = AVLTree[int, int]()
        for node in [8, 9, 10, 2, 1, 5, 3, 6, 4, 7]:
            tree.insert(node, node)
        return tree
    
    def test_insert_bforder(self, avltree: AVLTree) -> None: assert avltree.bforder() == [5, 3, 8, 2, 4, 6, 9, 1, 7, 10]
    def test_insert_inorder(self, avltree: AVLTree) -> None: assert avltree.inorder() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def test_insert_preorder(self, avltree: AVLTree) -> None: assert avltree.preorder() == [5, 3, 2, 1, 4, 8, 6, 7, 9, 10]
    def test_insert_postorder(self, avltree: AVLTree) -> None: assert avltree.postorder() == [1, 2, 4, 3, 7, 6, 10, 9, 8, 5]
