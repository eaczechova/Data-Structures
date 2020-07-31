"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # make a new BSTNode with a value
        if value < self.value:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # checks if the node we are on is True that is equal to target
        if self.value == target:
            return True
        if target > self.value:
            # if None there is nothing greater than target value in the entire tree
            if self.right is None:
                return False
            else: 
                return self.right.contains(target)

        if target < self.value:
            if self.left is None:
                return False
            else: 
                return self.left.contains(target)
        # if value is greater to target we go to the block on the right of BST
        

    # Return the maximum value found in the tree
    def get_max(self):
        # starting from the root and going to the right until hit None gives max number
        # if there is nothing to the right root is the highest number since left is lower 
        # than the root value we don't check
        if self.right is None:
           return self.value
        max_val = self.right.get_max()
        return max_val

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # accepts callback function only
        # call the function on the current value
        fn(self.value)
        # if the base case has children on the left
        if self.left is not None:
            self.left.for_each(fn)
         # if the base case has children on the right
        if self.right is not None:
            self.right.for_each(fn)

    # # Part 2 -----------------------

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self):
    #     pass

    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self):
    #     pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
