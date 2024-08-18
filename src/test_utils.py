import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from utils import Utils
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_raw_text_node_to_html_node(self):
        text_node = TextNode("This is a text node", "text")
        html_node = Utils.text_node_to_html_node(text_node)
        expected = HTMLNode(None, "This is a text node", None, None)
        self.assertEqual(html_node.tag, expected.tag)
        self.assertEqual(html_node.value, expected.value)
        self.assertEqual(html_node.children, expected.children)
        self.assertEqual(html_node.props, expected.props)

    def test_bold_text_node_to_html_node(self):
        text_node = TextNode("This is a text node", "bold")
        html_node = Utils.text_node_to_html_node(text_node)
        expected = HTMLNode("b", "This is a text node", None, None)
        self.assertEqual(html_node.tag, expected.tag)
        self.assertEqual(html_node.value, expected.value)
        self.assertEqual(html_node.children, expected.children)
        self.assertEqual(html_node.props, expected.props)

    def test_italic_text_node_to_html_node(self):
        text_node = TextNode("This is a text node", "italic")
        html_node = Utils.text_node_to_html_node(text_node)
        expected = HTMLNode("i", "This is a text node", None, None)
        self.assertEqual(html_node.tag, expected.tag)
        self.assertEqual(html_node.value, expected.value)
        self.assertEqual(html_node.children, expected.children)
        self.assertEqual(html_node.props, expected.props)

    def test_split_nodes_delimiter_code(self):
        text_type_text = "text"
        text_type_code = "code"
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = Utils.split_nodes_delimiter([node], "`", text_type_code)
        expected = [
            TextNode("This is text with a ", text_type_text, None),
            TextNode("code block", text_type_code, None),
            TextNode(" word", text_type_text, None)
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_delimiter_bold(self):
        text_type_text = "text"
        text_type_bold = "bold"
        node = TextNode("This is text with a **bold block** word", text_type_text)
        new_nodes = Utils.split_nodes_delimiter([node], "**", text_type_bold)
        expected = [
            TextNode("This is text with a ", text_type_text, None),
            TextNode("bold block", text_type_bold, None),
            TextNode(" word", text_type_text, None)
        ]
        self.assertEqual(new_nodes, expected)

    def test_split_nodes_delimiter_italic(self):
        text_type_text = "text"
        text_type_italic = "italic"
        node = TextNode("This is text with a *italic block* word", text_type_text)
        new_nodes = Utils.split_nodes_delimiter([node], "*", text_type_italic)
        expected = [
            TextNode("This is text with a ", text_type_text, None),
            TextNode("italic block", text_type_italic, None),
            TextNode(" word", text_type_text, None)
        ]
        self.assertEqual(new_nodes, expected)

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = Utils.extract_markdown_images(text)
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(images, expected)

    def test_extract_markdown_images_no_valid_images(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif) and (https://i.imgur.com/fJRm4Vk.jpeg)"
        images = Utils.extract_markdown_images(text)
        expected = []
        self.assertEqual(images, expected)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = Utils.extract_markdown_links(text)
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(links, expected)

    def test_extract_markdown_links_no_valid_links(self):
        text = "This is text with a link ![to boot dev](https://www.boot.dev) and (https://www.youtube.com/@bootdotdev)"
        links = Utils.extract_markdown_links(text)
        expected = []
        self.assertEqual(links, expected)


if __name__ == "__main__":
    unittest.main()
