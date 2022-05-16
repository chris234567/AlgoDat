from typing import List

from tree import Tree, Node


class BinarySearchTree(Tree):   
    
    #region Recursive Implementation

    def recursive_build_binary_search_tree(l: List[int]) -> Tree:
        T = Tree(
            Node(l[0])  # Root
        )

        for k in l[1:]:
            self.recursive_insert(T.root, k)

        return T
    
    def recursive_insert(self, x: Node, key):
        if x.key < key:
            if x.right:
                Bst_recursive.insert(x.right, key)
            else:
                x.right = Node(key)
                x.right.parent = x
        else:
            if x.left:
                Bst_recursive.insert(x.left, key)
            else:
                x.left = Node(key)
                x.left.parent = x

    def recursive_in_order_tree_walk(x: Node) -> None:
        if x:
            Bst_recursive.in_order_tree_walk(x.left)
            print(x.key)
            Bst_recursive.in_order_tree_walk(x.right)

    def recursive_search(x: Node, k: int) -> int:
        if x.key == k:
            return x

        elif x.key < k:
            return Bst_recursive.search(x.right, k)

        else:
            return Bst_recursive.search(x.left, k)


    def recursive_min(x: Node) -> int:
        if not x.left:
            return x

        return Bst_recursive.subtree_min(x.left)

    def recursive_max(x: Node) -> int:
        if not x.right:
            return x

        return Bst_recursive.max(x.right)

    def recursive_predecessor(T: Tree, x: Node) -> int:
        return

    def recursive_successor(T: Tree, x: Node) -> int:
        return

    def recursive_delete(T: Tree, x: Node) -> int:
        return

    #endregion

    #region Iterative Implementation

    def recursive_build_binary_search_tree(l: List[int]) -> Tree:
        T = Tree(
            Node(l[0])  # Root
        )

        for k in l[1:]:
            iterative_insert(T.root, k)

        return T

    def iterative_insert(x: Node, key):
        return

    def iterative_in_order_tree_walk(T: Tree, x: Node) -> None:
        return

    def iterative_search(T: Tree, x: Node) -> int:
        return

    def iterative_min(x: Node) -> int:
        while x.left:
            x = x.left
        
        return x

    def iterative_max(x: Node) -> int:
        while x.right:
            x = x.right
        
        return x

    def iterative_predecessor(T: Tree, x: Node) -> int:
        return

    def iterative_successor(T: Tree, x: Node) -> int:
        return

    def iterative_delete(T: Tree, x: Node) -> int:
        return

    #endregion


tree = Bst_recursive.build_binary_search_tree([6, 3, 9, 1, 4, 7])
bst
Bst_recursive.in_order_tree_walk(tree.root)