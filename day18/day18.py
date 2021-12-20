# For finding number to explode on left, traverse tree upwards. Keep going up and keep track of the previous
# node you were at. Find when the previous node was the _right_ node for the first time, then start traversing
# down the left path of that node until you find a right node literal value. That is what we're adding to.
# Assume we will never have no_nested_pairs <= 4, won't eve be more than 4.
import json
import math


class PairNode:
    def __init__(self, parent, val):
        self.parent = parent; self.left = None; self.right = None; self.val = val


def is_num(e):
    return type(e) is int


def get_inp(pair, node):
    if not is_num(pair[0]):
        node.left = PairNode(node, None)
        get_inp(pair[0], node.left)
    else:
        node.left = PairNode(node, pair[0])
    if not is_num(pair[1]):
        node.right = PairNode(node, None)
        get_inp(pair[1], node.right)
    else:
        node.right = PairNode(node, pair[1])


def printPostorder(root_n):
    if root_n:
        printPostorder(root_n.left)
        printPostorder(root_n.right)
        print("x" if root_n.val is None else root_n.val)


def add_snails(input, old_root):
    right_side = PairNode(None, None)
    get_inp(input, right_side)
    new_root = PairNode(None, None)
    new_root.left = old_root; new_root.right = right_side
    old_root.parent = new_root; right_side.parent = new_root
    return new_root


def find_leftmost(node, prev_node, ascend=True):
    if node:
        if not ascend:
            if node.right:
                return find_leftmost(node.right, node, False)
            elif node.left:
                return find_leftmost(node.left, node, False)
            else:
                return node

        if node.left and node.left is not prev_node:
            # Now we start descending down the tree to find the node closest to the left
            return find_leftmost(node.left, node, False)

        return find_leftmost(node.parent, node)


def find_rightmost(node, prev_node, ascend=True):
    if node:
        if not ascend:
            if node.left:
                return find_rightmost(node.left, node, False)
            elif node.right:
                return find_rightmost(node.right, node, False)
            else:
                return node

        if node.right and node.right is not prev_node:
            # Now we start descending down the tree to find the node closest to the left
            return find_rightmost(node.right, node, False)

        return find_rightmost(node.parent, node)


def explode(node, depth=0):
    if node and depth <= 4:
        if depth == 4 and node.val is None:  # If we don't check for None, it could just be a literal, not a pair.
            left_found = find_leftmost(node.parent, node)
            if left_found:
                left_found.val += node.left.val
            right_found = find_rightmost(node.parent, node)
            if right_found:
                right_found.val += node.right.val
            node.left = None; node.right = None
            node.val = 0

        explode(node.left, depth+1)  # Leftmost pairs explode first
        explode(node.right, depth+1)


def split(node):
    if node:
        if node.val and node.val >= 10:
            node.left = PairNode(node, node.val//2)
            node.right = PairNode(node, math.ceil(node.val/2))
            node.val = None
            return True
        if split(node.left):
            return True
        if split(node.right):
            return True
    return False

def get_magnitude(node):
    if node:
        if node.val is not None:
            return node.val
        return get_magnitude(node.left) * 3 + get_magnitude(node.right) * 2


if __name__ == "__main__":
    with open("input") as file:
        root = PairNode(None, None)
        get_inp(json.loads(file.readline().rstrip()), root)

        explode(root)
        while split(root):
            explode(root)

        while line := file.readline().rstrip():
            root = add_snails(json.loads(line), root)
            explode(root)
            while split(root):
                explode(root)

        print("Part 1 sln:", get_magnitude(root))

    # Try em all for part 2, this problem hurt my head enough.
    with open("input") as file:
        lines = [line.rstrip() for line in file.readlines()]

        max_mag = 0
        for i, line1 in enumerate(lines):
            for j, line2 in enumerate(lines):
                if i == j:
                    continue
                root = PairNode(None, None)
                get_inp(json.loads(line1), root)

                explode(root)
                while split(root):
                    explode(root)

                root = add_snails(json.loads(line2), root)
                explode(root)
                while split(root):
                    explode(root)
                max_mag = max(get_magnitude(root), max_mag)

        print("Part 2 sln:", max_mag)
