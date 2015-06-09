import unittest

from html_render import Element

class TestElementClass(unittest.TestCase):

    def test_create_element_no_content(self):
        page = Element()
        self.assertEqual(page.tag, 'html')
        self.assertEqual(page.indent, '    ')
        self.assertFalse(page.children)

    def test_create_element_content(self):
        page = Element(content="Test Content")
        self.assertEqual(page.children, ["Test Content"])





# if __name__ == '__main__':
#     unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestElementClass)
unittest.TextTestRunner(verbosity=2).run(suite)