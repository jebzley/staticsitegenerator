import unittest
from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_url(self):
        node = TextNode("a", "bold", "https://a.com")
        node2 = TextNode("a", "bold")
        self.assertEqual(node.url, "https://a.com")
        self.assertEqual(node2.url, None)

    def test_eq(self):
        self.assertEqual(TextNode("A", "bold"), TextNode("A", "bold"))
        self.assertEqual(TextNode("A", "bold", "https://a.com"),
                         TextNode("A", "bold", "https://a.com"))
        self.assertNotEqual(TextNode("A", "bold"), TextNode("B", "bold"))
        self.assertNotEqual(TextNode("A", "bold"), TextNode("A", "medium"))
        self.assertNotEqual(TextNode("A", "bold"),
                            TextNode("A", "bold", "https://a.com"))
        self.assertNotEqual(TextNode("A", "bold", "https://a.com"),
                            TextNode("A", "bold", "https://b.com"))

    def test_repr(self):
        node = TextNode("a", "bold", "https://a.com")
        node2 = TextNode("a", "bold")
        self.assertEqual(f"{node}", "TextNode(a, bold, https://a.com)")
        self.assertEqual(f"{node2}", "TextNode(a, bold, None)")


if __name__ == "__main__":
    unittest.main()
