# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        # Uncomment one of the following methods to use
        return self.postorderTraversalRecursive(root)
        # return self.postorderTraversalIterative(root)

    def postorderTraversalRecursive(self, root: TreeNode) -> list:
        result = []
        
        def traverse(node):
            if node:
                traverse(node.left)      # Visit left subtree
                traverse(node.right)     # Visit right subtree
                result.append(node.val)  # Visit the root
        
        traverse(root)
        return result

    def postorderTraversalIterative(self, root: TreeNode) -> list:
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)  # Process the root node
            if node.left:             # Push left child to stack
                stack.append(node.left)
            if node.right:            # Push right child to stack
                stack.append(node.right)
        
        return result[::-1]  # Reverse the result to get postorder

# Test cases
def test_solution():
    solution = Solution()
    
    # Test case 1
    root1 = TreeNode(1)
    root1.right = TreeNode(2, TreeNode(3))
    print(solution.postorderTraversal(root1))  # Expected output: [3, 2, 1]

    # Test case 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root2.right = TreeNode(3, TreeNode(6, TreeNode(7)), TreeNode(8))
    print(solution.postorderTraversal(root2))  # Expected output: [4, 5, 2, 7, 6, 8, 3, 1]

    # Test case 3: Empty tree
    print(solution.postorderTraversal(None))     # Expected output: []

    # Test case 4: Single node
    root4 = TreeNode(1)
    print(solution.postorderTraversal(root4))  # Expected output: [1]

# Run the tests
test_solution()
