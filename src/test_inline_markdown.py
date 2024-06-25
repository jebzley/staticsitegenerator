import unittest
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_images, split_nodes_links

from textnode import TextNode, text_type_text, text_type_link, text_type_code, text_type_italic, text_type_image


class TestInlineMarkdown(unittest.TestCase):
    def test_delimiter(self):
        nodes1 = [
            TextNode("this is `some code` get `a load` of this", text_type_text)]
        split1 = split_nodes_delimiter(nodes1, "`", "code")
        expect1 = [TextNode("this is ", "text"), TextNode(
            "some code", text_type_code), TextNode(" get ", text_type_text), TextNode(
            "a load", text_type_code), TextNode(" of this", text_type_text)]
        self.assertEqual(split1, expect1)

        nodes2 = [TextNode("Should return the same node", text_type_code)]
        split2 = split_nodes_delimiter(nodes2, "`", text_type_code)
        self.assertEqual(split2, nodes2)

        nodes3 = [TextNode("`code` not code", text_type_text),
                  TextNode("not code `code`", text_type_text)]
        split3 = split_nodes_delimiter(nodes3, "`", text_type_code)
        expect3 = [TextNode("code", text_type_code), TextNode(" not code", text_type_text), TextNode(
            "not code ", text_type_text), TextNode("code", text_type_code),]
        self.assertEqual(split3, expect3)

        nodes4 = [
            TextNode("_italic_ text is good for being _passive aggressive_", text_type_text)]
        split4 = split_nodes_delimiter(nodes4, "_", text_type_italic)
        expect4 = [TextNode("italic", text_type_italic), TextNode(
            " text is good for being ", text_type_text), TextNode("passive aggressive", text_type_italic)]
        self.assertEqual(split4, expect4)

        nodes5 = [
            TextNode("Attempting to split this one to an *invalid* text type", text_type_text)]
        with self.assertRaises(TypeError):
            split_nodes_delimiter(nodes5, "*", "wrong")

    def test_extract_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        text2 = "This has no (image) but other things that [may] [catch](it)!"
        self.assertEqual(extract_markdown_images(text), [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), (
            "another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")])

        self.assertEqual(extract_markdown_images(text2), [])

    def test_extract_links(self):
        text = "This is text with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/) and [another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/)"
        text2 = "This has no (link) but other things that may ![catch](it)"
        self.assertEqual(extract_markdown_links(text), [("link", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/"), (
            "another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/")])

        self.assertEqual(extract_markdown_links(text2), [])

    def test_split_nodes_images(self):
        nodes1 = [TextNode(
            "img in ![markdown](image.com) the middle", text_type_text)]
        expect1 = [TextNode("img in ", text_type_text), TextNode(
            "markdown", text_type_image, "image.com"), TextNode(" the middle", text_type_text)]
        self.assertEqual(split_nodes_images(nodes1), expect1)

        nodes2 = [TextNode(
            "![markdown](image.com) img at start", text_type_text)]
        expect2 = [TextNode("markdown", text_type_image, "image.com"), TextNode(
            " img at start", text_type_text)]
        self.assertEqual(split_nodes_images(nodes2), expect2)

        nodes3 = [TextNode(
            "img at end ![markdown](image.com)", text_type_text)]
        expect3 = [TextNode(
            "img at end ", text_type_text), TextNode("markdown", text_type_image, "image.com")]
        self.assertEqual(split_nodes_images(nodes3), expect3)

        nodes4 = [TextNode(
            "one ![markdown](image.com)", text_type_text), TextNode(
            "two", text_type_text), TextNode(
            "![ye olde markdowne](pictorial.com) three", text_type_text),]
        expect4 = [TextNode(
            "one ", text_type_text), TextNode("markdown", text_type_image, "image.com"),
            TextNode("two", text_type_text),
            TextNode("ye olde markdowne", text_type_image, "pictorial.com"),
            TextNode(" three", text_type_text)]

        self.assertEqual(split_nodes_images(nodes4), expect4)

    def test_split_nodes_links(self):
        nodes1 = [TextNode(
            "link in [markdown](link.com) the middle", text_type_text)]
        expect1 = [TextNode("link in ", text_type_text), TextNode(
            "markdown", text_type_link, "link.com"), TextNode(" the middle", text_type_text)]
        self.assertEqual(split_nodes_links(nodes1), expect1)

        nodes2 = [TextNode(
            "[markdown](link.com) link at start", text_type_text)]
        expect2 = [TextNode("markdown", text_type_link, "link.com"), TextNode(
            " link at start", text_type_text)]
        self.assertEqual(split_nodes_links(nodes2), expect2)

        nodes3 = [TextNode(
            "link at end [markdown](link.com)", text_type_text)]
        expect3 = [TextNode(
            "link at end ", text_type_text), TextNode("markdown", text_type_link, "link.com")]
        self.assertEqual(split_nodes_links(nodes3), expect3)

        nodes4 = [TextNode(
            "one [markdown](link.com)", text_type_text), TextNode(
            "two", text_type_text), TextNode(
            "[ye olde markdowne](lonk.com) three", text_type_text),]
        expect4 = [TextNode(
            "one ", text_type_text), TextNode("markdown", text_type_link, "link.com"),
            TextNode("two", text_type_text),
            TextNode("ye olde markdowne", text_type_link, "lonk.com"),
            TextNode(" three", text_type_text)]

        self.assertEqual(split_nodes_links(nodes4), expect4)
