import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_paragraph_tag(self):
        node = LeafNode("p", "Meow meow meow")
        node_to_html = node.to_html()
        self.assertEqual(node_to_html, "<p>Meow meow meow</p>")

    def test_to_html_a_tag(self):
        node = LeafNode("a", "Link", {"href": "thelinkurl.com"})
        node_to_html = node.to_html()
        self.assertEqual(node_to_html, "<a href=\"thelinkurl.com\">Link</a>")

    def test_raw_text_no_tag(self):
        node = LeafNode(None, "This is raw text that is probably a child of something else")
        node_to_html = node.to_html()
        self.assertEqual(node_to_html, "This is raw text that is probably a child of something else")


if __name__ == "__main__":
    unittest.main()
