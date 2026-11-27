import unittest
from basics.data_types import describe
from basics.operators import add
from conditionals.compare_numbers import compare
from conditionals.marks_pass_fail import classify_mark
from conditionals.rcb_example import match_message
from conditionals.simple_if_else import choose_message
from conditionals.status_input import status_message
from exercises.product_sum_ratio import product_to_sum_ratio
from exercises.student_score import score_out_of_ten

class PracticeTests(unittest.TestCase):
    def test_basics(self):
        self.assertEqual(describe("hello"), "str")
        self.assertEqual(add(2, 3), 5)

    def test_compare(self):
        self.assertEqual(compare(5, 2), "5 is greater")
        self.assertEqual(compare(2, 5), "5 is greater")
        self.assertEqual(compare(4, 4), "Both numbers are equal")

    def test_mark_boundaries(self):
        self.assertEqual(classify_mark(34), "Fail")
        self.assertEqual(classify_mark(35), "Pass")
        with self.assertRaises(ValueError):
            classify_mark(101)

    def test_conditionals(self):
        self.assertEqual(choose_message(True), "Yes")
        self.assertEqual(match_message("WIN"), "Ee sala cup namdhe!")
        self.assertEqual(status_message("finished"), "The task is finished.")

    def test_arithmetic_validation(self):
        self.assertAlmostEqual(product_to_sum_ratio(2, 3, 4), 24 / 9)
        with self.assertRaises(ZeroDivisionError):
            product_to_sum_ratio(1, -1, 0)
        self.assertEqual(score_out_of_ten(80), 8)
        with self.assertRaises(ValueError):
            score_out_of_ten(101)

if __name__ == "__main__":
    unittest.main()
