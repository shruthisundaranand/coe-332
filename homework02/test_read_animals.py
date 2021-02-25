import unittest
from read_animals import breeding

class TestReadAnimals(unittest.TestCase):

    def test_breeding(self):
        self.assertEqual(breeding(child_head), breeding(parent_1['head:']))
        self.assertEqual(breeding(child_body), breeding(parent_2['body:']))
        self.assertTrue(breeding(child_arms), breeding(parent_1['arms:'] + pare\
nt_2['arms:']))

if __name__ == '__main__':
    unittest.main()









