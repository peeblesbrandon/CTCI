import unittest

def isOneAway(s1, s2):
    if abs(len(s1)-len(s2)) > 1:
        return False
    i, j, edits = 0, 0, 0
    while i < len(s1):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            edits += 1              # increment num of edits required
            if len(s1) > len(s2):
                i += 1
            elif len(s2) > len(s1):
                j += 1
            else: 
                i += 1
                j += 1
        if edits > 1:
            return False 
    return True

class TestEditDistance(unittest.TestCase):
    def test_same(self):
        self.assertTrue(isOneAway('python', 'python'))

    def test_oneAway(self):
        self.assertTrue(isOneAway('python', 'pythn'))
        self.assertTrue(isOneAway('pythn', 'python'))
        self.assertTrue(isOneAway('pyth0n', 'python'))
    
    def test_moreThanOne(self):
        self.assertFalse(isOneAway('python', 'pith0n'))
        self.assertFalse(isOneAway('py', 'python'))

if __name__ == '__main__':
    unittest.main()
            