import unittest
from analyze_sorting_performance import *

bubble_sorted_arr, insertion_sorted_arr, selection_sorted_arr, merge_sorted_arr, quick_sorted_arr, builtin_sorted_arr = run_analyzer()

class TestSorting(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sorted_arr, sorted(bubble_sorted_arr))

    def test_insertion_sort(self):
        self.assertEqual(insertion_sorted_arr, sorted(insertion_sorted_arr))

    def test_selection_sort(self):
        self.assertEqual(selection_sorted_arr, sorted(selection_sorted_arr))

    def test_merge_sort(self):
        self.assertEqual(merge_sorted_arr, sorted(merge_sorted_arr))

    def test_quick_sort(self):
        self.assertEqual(quick_sorted_arr, sorted(quick_sorted_arr))

    def test_builtin_sort(self):
        self.assertEqual(builtin_sorted_arr, sorted(builtin_sorted_arr))

if __name__ == '__main__':
    unittest.main()
