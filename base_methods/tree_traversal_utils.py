class TreeNode:
    """
    A simple tree node class.

    Attributes:
        val (int): The value of the node.
        left (TreeNode): The left child of the node.
        right (TreeNode): The right child of the node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    """
    Perform an in-order traversal of the tree.

    Args:
        root (TreeNode): The root of the tree.

    Returns:
        A list of node values in the order they were traversed.
    """
    # Example:
    #     1
    #    / \
    #   2   3
    #  /
    # 4
    # Output: [4, 2, 1, 3]
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []


def preorder_traversal(root):
    """
    Perform a pre-order traversal of the tree.

    Args:
        root (TreeNode): The root of the tree.

    Returns:
        A list of node values in the order they were traversed.
    """
    # Example:
    #     1
    #    / \
    #   2   3
    #  /
    # 4
    # Output: [1, 2, 4, 3]
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right) if root else []


def postorder_traversal(root):
    """
    Perform a post-order traversal of the tree.

    Args:
        root (TreeNode): The root of the tree.

    Returns:
        A list of node values in the order they were traversed.
    """
    # Example:
    #     1
    #    / \
    #   2   3
    #  /
    # 4
    # Output: [4, 2, 3, 1]
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val] if root else []
