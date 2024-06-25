import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode('a', None, None, {
                        "href": "https://a.com", "target": "_blank"})
        node2 = HTMLNode()
        node3 = HTMLNode(None, None, None, 'incorrect type')
        self.assertEqual(node.props_to_html(),
                         'href="https://a.com" target="_blank"')
        self.assertEqual(node2.props_to_html(), None)
        self.assertRaises(TypeError, node3.props_to_html)


if __name__ == "__main__":
    unittest.main()
