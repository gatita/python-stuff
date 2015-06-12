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

    def test_append_no_prior_content(self):
        page = Element()
        t1 = "One night--it was on the twentieth of March, 1888--I was \
            returning from a journey to a patient (for I had now returned to \
            civil practice), when my way led me through Baker Street."

        t2 = "As I passed the well-remembered door, which must always be \
             associated in my mind with my wooing, and with the dark incidents \
             of the Study in Scarlet, I was seized with a keen desire to see \
             Holmes again, and to know how he was employing his extraordinary \
             powers."

        page.append(t1)
        page.append(t2)

        self.assertEqual(page.children, [t1, t2])

    def test_append_with_prior_content(self):
        page = Element(content="Test Content")
        t1 = "One night--it was on the twentieth of March, 1888--I was \
            returning from a journey to a patient (for I had now returned to \
            civil practice), when my way led me through Baker Street."

        page.append(t1)
        self.assertEqual(page.children, ["Test Content", t1])

    def test_append_non_string(self):
        page = Element()
        page.append(2)
        self.assertEqual(page.children, [2])




# if __name__ == '__main__':
#     unittest.main()

suite = unittest.TestLoader().loadTestsFromTestCase(TestElementClass)
unittest.TextTestRunner(verbosity=2).run(suite)

