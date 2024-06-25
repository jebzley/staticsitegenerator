import unittest
from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text", {"class": "egg"}),
                LeafNode(None, "Normal text"),
            ],
            {"class": "egg"}
        )

        node2 = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]
                ),
                LeafNode("a", "Link", {"href": "https://a.com"})
            ]
        )

        node3 = ParentNode(
            "div",
            [
                ParentNode(
                    "div",
                    [
                        ParentNode(
                            "div",
                            [
                                LeafNode("p", "Text"),
                            ],
                            {"id": "2"}
                        ),
                    ],
                    {"id": "1"}
                ),
            ],
            {"id": "0"}
        )

        node4 = ParentNode(None, [LeafNode("b", "Bold text")])
        node5 = ParentNode(None, [LeafNode("b", "Bold text")])

        self.assertEqual(node1.to_html(
        ), '<p class="egg"><b>Bold text</b>Normal text<i class="egg">italic text</i>Normal text</p>')
        self.assertEqual(node2.to_html(
        ), '<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><a href="https://a.com">Link</a></div>')
        self.assertEqual(node3.to_html(
        ), '<div id="0"><div id="1"><div id="2"><p>Text</p></div></div></div>')
        self.assertRaises(ValueError, node4.to_html)
        self.assertRaises(ValueError, node5.to_html)


if __name__ == "__main__":
    unittest.main()
