import unittest

def compress(input):
    i = 0
    output = []
    while i < len(input):
        output.append(input[i])
        j = 1
        while len(input) > (i+j) and input[i] == input[i+j]:
            j += 1
        output.append(str(j))
        i += j
    if len(output) >= len(input):
        return input 
    return ''.join(output)

class TestCompression(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(compress('aaabbbbc'), 'a3b4c1')
        self.assertEqual(compress('aaa'), 'a3')
    
    def test_advanced(self):
        self.assertEqual(compress('aaZZZZzzzYyyooooooXxxxx'), 'a2Z4z3Y1y2o6X1x4')
    
    def test_returninput(self):
        self.assertEqual(compress('ABC'), 'ABC')

if __name__ == '__main__':
    unittest.main()
