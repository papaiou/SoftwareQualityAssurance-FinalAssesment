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


    def test_new_surveyResponse_errors(self):
        os.system("echo \"ns\nfoo\n3\n20\n14\n3\nnsr\n0\n2\nyes\n1\n\nfooResponse\n0\n6\nyes\n1\n5\n3\nnsr\n1\nfooResponse\nfooResponse2\n2\n2\n2\ne\" | python3 ./../main.py > .unittest11.tmp")
        self.assertEqual(self.content(".unittest11.tmp"), self.content(".unittest11_res.txt"))
        os.remove(".unittest11.tmp")

    def test_get_surveyResponse_error(self):
        os.system("echo \"gsr\nns\nfoo\n3\n20\n14\n3\ngsr\n1\nnsr\n1\nfooResponse\n2\n2\n2\ngsr\n0\n2\nyes\n1\n0\n2\nyes\n1\nnsr\n1\nfooResponse2\n1\n1\n1\ngsr\n1\n2\nns\nbar\n5\n15\n6\n7\n8\n2\nnsr\n2\nfooResponse\n4\n4\n4\n4\n4\ngsr\n2\n1\ne\" | python3 ./../main.py > .unittest12.tmp")
        self.assertEqual(self.content(".unittest12.tmp"), self.content(".unittest12_res.txt"))
        os.remove(".unittest12.tmp")

    def test_get_surveyResponse_error(self):
        os.system("echo \"gsr\nns\nfoo\n3\n20\n14\n3\ngsr\nnsr\n1\nfooResponse\n2\n2\n2\ngsr\n0\n2\nyes\n1\n0\n2\nyes\n1\nnsr\n1\nfooResponse2\n1\n1\n1\ngsr\n1\n2\nns\nbar\n5\n15\n6\n7\n8\n2\nnsr\n2\nfooResponse\n4\n4\n4\n4\n4\ngsr\n2\n1\ne\" | python3 ./../main.py > .unittest13.tmp")
        self.assertEqual(self.content(".unittest13.tmp"), self.content(".unittest13_res.txt"))
        os.remove(".unittest13.tmp")

    def test_survey_stats(self):
        os.system("echo \"ss\nns\nfoo\n3\n20\n14\n3\nss\n0\n2\nyes\n1\nnsr\n1\nfooResponse\n2\n3\n4\nnsr\n1\nfoo2\n1\n3\n5\nss\n1e\" | python3 ./../main.py > .unittest14.tmp")
        self.assertEqual(self.content(".unittest14.tmp"), self.content(".unittest14_res.txt"))
        os.remove(".unittest14.tmp")

    def test_question_stats(self):
        os.system("echo \"qs\nns\nfoo\n3\n20\n14\n3\nqs\n0\n2\nyes\n1\nnsr\n1\nfooResponse\n2\n3\n4\nnsr\n1\nfoo2\n1\n3\n5\nqs\n1\n0\n4\nyes\n2\nqs\n1\n1\nqs\n1\n3e\" | python3 ./../main.py > .unittest15.tmp")
        self.assertEqual(self.content(".unittest1R.tmp"), self.content(".unittest15_res.txt"))
        os.remove(".unittest15.tmp")
    
    def test_help(self):
        os.system("echo \"h\n3e\" | python3 ./../main.py > .unittest16.tmp")
        self.assertEqual(self.content(".unittest16.tmp"), self.content(".unittest16_res.txt"))
        os.remove(".unittest16.tmp")
    
    def test_question_stats(self):
        os.system("echo \"a\nQuestion 1\n\nQuestion 21\ne\" | python3 ./../main.py > .unittest17.tmp")
        self.assertEqual(self.content(".unittest17.tmp"), self.content(".unittest17_res.txt"))
        os.remove(".unittest17.tmp")


if __name__ == '__main__':
    unittest.main()
