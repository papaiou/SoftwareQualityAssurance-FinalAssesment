import unittest
import os

class TestSurveyControllerMethods(unittest.TestCase):

    def content(self, filename):
        with open(filename, 'r') as myfile:
            return myfile.read()


    def test_usage(self):
        os.system("python3 ./../main.py yes > .unittest01.tmp")
        self.assertEqual(self.content(".unittest01.tmp"), self.content(".unittest01_res.txt"))
        os.remove(".unittest01.tmp")

    def test_input_errors_and_exit(self):
        os.system("echo \"hello\nz\nad\nyes\n0210\n\ne\" | python3 ./../main.py > .unittest02.tmp")
        self.assertEqual(self.content(".unittest02.tmp"), self.content(".unittest02_res.txt"))
        os.remove(".unittest02.tmp")

    def test_new_survey_errors(self):
        os.system("echo \"ns\n\nyes\n12\nyes\n0\n2\n0\n21\nyes\n8\n8\n7\ne\" | python3 ./../main.py > .unittest03.tmp")
        self.assertEqual(self.content(".unittest03.tmp"), self.content(".unittest03_res.txt"))
        os.remove(".unittest03.tmp")

    def test_new_survey2(self):
        os.system("echo \"ns\nhello world\n3\n4\n20\n1\ne\" | python3 ./../main.py > .unittest04.tmp")
        self.assertEqual(self.content(".unittest04.tmp"), self.content(".unittest04_res.txt"))
        os.remove(".unittest04.tmp")

    def test_new_survey3(self):
        os.system("echo \"ns\nfoobar\n10\n7\n2\n5\n19\n20\n12\n3\n14\n16\n15\ne\" | python3 ./../main.py > .unittest05.tmp")
        self.assertEqual(self.content(".unittest05.tmp"), self.content(".unittest05_res.txt"))
        os.remove(".unittest05.tmp")

    def test_new_survey4(self):
        os.system("echo \"ns\nsingle question\n1\n7\ne\" | python3 ./../main.py > .unittest06.tmp")
        self.assertEqual(self.content(".unittest06.tmp"), self.content(".unittest06_res.txt"))
        os.remove(".unittest06.tmp")

    def test_list_survey(self):
        os.system("echo \"l\nns\nsingle question\n1\n7\nl\nns\nmultiple question\n10\n7\n2\n5\n19\n20\n12\n3\n14\n16\n15\nl\ne\" | python3 ./../main.py > .unittest07.tmp")
        self.assertEqual(self.content(".unittest07.tmp"), self.content(".unittest07_res.txt"))
        os.remove(".unittest07.tmp")
 
    def test_list_survey2(self):
        os.system("echo \"l\nns\nfoo\n1\n7\nl\nns\nbar\n10\n7\n2\n5\n19\n20\n12\n3\n14\n16\n15\nl\ne\" | python3 ./../main.py > .unittest08.tmp")
        self.assertEqual(self.content(".unittest08.tmp"), self.content(".unittest08_res.txt"))
        os.remove(".unittest08.tmp")

    def test_get_survey(self):
        os.system("echo \"gs\nns\nsingle question\n1\n7\ngs\n1\nns\nmultiple question\n10\n7\n2\n5\n19\n20\n12\n3\n14\n16\n15\ngs\n2\ne\" | python3 ./../main.py > .unittest09.tmp")
        self.assertEqual(self.content(".unittest09.tmp"), self.content(".unittest09_res.txt"))
        os.remove(".unittest09.tmp")

    def test_get_survey2(self):
        os.system("echo \"gs\nns\nfoo\n3\n20\n14\n3\ngs\n0\n2\nyes\n1\nns\nbar\n7\n9\n12\n4\n19\n6\n16\n1\ngs\n2\ne\" | python3 ./../main.py > .unittest10.tmp")
        self.assertEqual(self.content(".unittest10.tmp"), self.content(".unittest10_res.txt"))
        os.remove(".unittest10.tmp")


if __name__ == '__main__':
    unittest.main()
