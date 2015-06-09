import unittest

from html_render import Element

class TestElementRender(unittest.TestCase):

    def test_create_element(self):
        page = Element()
        self.assertEqual(page.tag, 'html')
        self.assertEqual(page.indent, '    ')




# if __name__ == '__main__':
#     unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestElementRender)
unittest.TextTestRunner(verbosity=2).run(suite)