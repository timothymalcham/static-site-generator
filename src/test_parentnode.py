import unittest

from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_basic_parent_node_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        node_to_html = node.to_html()

        self.assertEqual(node_to_html, "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_more_advanced_parent_node_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode("a", "link", {"href": "thelinkurl.com"}),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        node_to_html = node.to_html()

        self.assertEqual(node_to_html, "<p><b>Bold text</b><a href=\"thelinkurl.com\">link</a><i>italic text</i>Normal text</p>")


    def test_parent_node_to_html_with_nested_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                ParentNode("div", [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ]),
            ],
        )

        node_to_html = node.to_html()

        self.assertEqual(node_to_html, "<p><b>Bold text</b>Normal text<i>italic text</i><div><b>Bold text</b>Normal text<i>italic text</i>Normal text</div></p>")


if __name__ == "__main__":
    unittest.main()
