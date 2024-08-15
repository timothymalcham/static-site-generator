import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_with_all_args(self):
        node = TextNode("This is a text node", "bold", "myurl.com")
        node2 = TextNode("This is a text node", "bold", "myurl.com")
        self.assertTrue(node == node2)

    def test_missing_url(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.url, None)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold", "myurl.com")
        node2 = TextNode("This is a text node too!", "italic", "myurl.com")
        self.assertFalse(node == node2)


if __name__ == "__main__":
    unittest.main()
