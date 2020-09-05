import unittest


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def createMinimalBST(array):
    return createMinBST(array, 0, len(array) - 1)


def createMinBST(array, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    newNode = Node(array[mid])
    newNode.left = createMinBST(array, start, mid - 1)
    newNode.right = createMinBST(array, mid + 1, end)
    return newNode


def getHeight(rootNode):
    if not rootNode:
        return 0
    return max(getHeight(rootNode.left) + 1, getHeight(rootNode.right) + 1)


class Test(unittest.TestCase):
    def test_setCorrectRoot(self):
        input = [0, 2, 3, 5, 20, 22, 51, 65, 80, 81, 97, 99]
        self.assertEqual(createMinimalBST(input).value, 22)

    def test_minimalHeight(self):
        input = [0, 2, 3, 5, 20, 22, 51, 65, 80, 81, 97, 99]
        self.assertEqual(getHeight(createMinimalBST(input)), 4)
        input = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(getHeight(createMinimalBST(input)), 3)
        input = []
        self.assertEqual(getHeight(createMinimalBST(input)), 0)

    def test_emptyArray(self):
        input = []
        self.assertIsNone(createMinimalBST(input))


if __name__ == '__main__':
    unittest.main()
