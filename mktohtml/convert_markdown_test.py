import unittest
import os
import MarkdownToHTML


class MarkdownToHTML(unittest.TestCase):

    
    def list_all_files(self):
        os.environ["input_ext"] = ".*"
        mk_to_html = MarkdownToHTML()
        list_of_files = mk_to_html.list_all_files()
        self.assertGreater(len(list_of_files), 0)

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
