import unittest
import PDFTools


class TestPDFTools(unittest.TestCase):
    input_true_test_file_name = '1.pdf'
    input_false_test_file_name = 'false.pdf'

    input_test_dir = '/'
    input_test_extension = '.pdf'

    def test_is_file_exist(self):
        self.assertTrue(PDFTools.PDFTools.is_file_exist(self, self.input_true_test_file_name))
        self.assertFalse(PDFTools.PDFTools.is_file_exist(self, self.input_false_test_file_name))


if __name__ == "__main__":
    unittest.main()