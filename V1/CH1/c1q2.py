class Solution:
    def isPermHash(self, s1, s2):
        if len(s1) != len(s2):
            return False
        hashMap = {}
        # load s1 to hashmap
        for char in s1:
            if char in hashMap:
                hashMap[char] += 1
            else:
                hashMap[char] = 1
        # check s2 against hashmap
        for char in s2:
            if not char in hashMap:
                return False
            elif hashMap[char] > 1:
                hashMap[char] -= 1
            else:
                del hashMap[char]
        # if a permutation, hashmap should be empty
        if hashMap:
            return False
        return True
        
    def isPermArr(self, s1, s2):
        if len(s1) != len(s2):
            return False
        chars = [0] * 128 # if assuming ASCII
        for char in s1:
            chars[ord(char)] += 1
        for char in s2:
            chars[ord(char)] -= 1
            if chars[ord(char)] < 0:
                return False
        return True

if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.isPermHash('hello', 'elohl'))
    print(mySolution.isPermArr('new york', 'wne kroy'))
