import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        p = LeafNode("p", "This is a paragraph of text")
        a = LeafNode("a", "This is a link", {
                     "href": "https://a.com", "target": "_blank"})
        should_string = LeafNode(None, "This should be a raw string")
        should_error = LeafNode("p", None)
        self.assertEqual(p.to_html(), "<p>This is a paragraph of text</p>")
        self.assertEqual(
            a.to_html(), '<a href="https://a.com" target="_blank">This is a link</a>')
        self.assertEqual(should_string.to_html(),
                         "This should be a raw string")
        self.assertRaises(ValueError, should_error.to_html)


if __name__ == "__main__":
    unittest.main()
