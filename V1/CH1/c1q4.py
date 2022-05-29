import unittest

def isPalinPerm(str):
    if not str:
        return False
    str = str.lower()
    letters = {}
    # load hash table
    for char in str:
        if char in letters:
            letters[char] += 1
        else:
            if char.isalpha():
                letters[char] = 1
    # check number of chars with odd frequencies
    odds = 0
    for val in letters.values():
        if val % 2 != 0:
            odds += 1
        if odds > 1:
            return False
    return True

class TestMain(unittest.TestCase):
    def test_basic(self):
        self.assertTrue(isPalinPerm('bob'))
    
    def test_spaces(self):
        self.assertTrue(isPalinPerm('race car'))
        self.assertFalse(isPalinPerm('xyza zzyx'))

    def test_capital(self):
        self.assertTrue(isPalinPerm('mAdaM '))

    def test_nonletters(self):
        self.assertTrue(isPalinPerm('tact%coa'))
        self.assertFalse(isPalinPerm('ush%#kns#* adfh487'))

if __name__ == '__main__':
    unittest.main()
