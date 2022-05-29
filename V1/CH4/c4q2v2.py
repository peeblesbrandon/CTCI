# [1, 2, 3, 4, 5, 6, 8, 45, 59, 60]

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createMinimalBST(nums):
    return _createMinimalBST(nums, 0, len(nums) - 1)

def _createMinimalBST(nums, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    root = Node(nums[mid])
    root.left = _createMinimalBST(nums, start, mid - 1)
    root.right = _createMinimalBST(nums, mid + 1, end)
    return root


if __name__ == "__main__":
    nums = [1, 2, 3, 5, 6, 9, 12, 33, 35, 58, 60]
    print(createMinimalBST(nums).val)