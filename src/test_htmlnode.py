import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_default_values_when_created(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.children)
        self.assertIsNone(node.value)
        self.assertIsNone(node.tag)

    def test_props_to_html_none_passed(self):
        node = HTMLNode("p", "Text inside the <p>", None, None)
        props_to_html = node.props_to_html()
        self.assertEqual(props_to_html, "")

    def test_props_to_html_multiple_passed(self):
        node = HTMLNode("a", "Link text", None, {"href": "https://www.google.com", "target": "_blank",})
        props_to_html = node.props_to_html()
        self.assertEqual(props_to_html, "href=\"https://www.google.com\" target=\"_blank\"")


if __name__ == "__main__":
    unittest.main()
