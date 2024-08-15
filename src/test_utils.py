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

if __name__ == "__main__":
    unittest.main()
