import unittest

from codetobetest import sum

class TestSum(unittest.TestCase):

    def test_sum(self):
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result,6)

    
if __name__=='__main__':
    unittest.main()

    