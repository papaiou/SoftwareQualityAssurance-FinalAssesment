import unittest
import os

class TestAddQuestionMethod(unittest.TestCase):

    def content(self, filename):
        with open(filename, 'r') as myfile:
            return myfile.read()

    def test_add_question(self):
        os.system("echo \"a\nQuestion 1\na\nQuestion 21\ne\" | python3 ./../main.py > .unittest16.tmp")
        self.assertEqual(self.content(".unittest16.tmp"), self.content(".unittest16_res.txt"))
        os.remove(".unittest16.tmp")

if __name__ == '__main__':
    unittest.main()