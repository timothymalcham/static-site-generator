import re

from leafnode import LeafNode
from textnode import TextNode


class Utils(object):

    @staticmethod
    def text_node_to_html_node(text_node):
        text_type = text_node.text_type
        if text_type == "text":
            return LeafNode(None, text_node.text)
        elif text_type == "bold":
            return LeafNode("b", text_node.text)
        elif text_type == "italic":
            return LeafNode("i", text_node.text)
        elif text_type == "code":
            return LeafNode("code", text_node.text)
        elif text_type == "link":
            return LeafNode("a", text_node.text, {"href": ""})
        elif text_type == "image":
            return LeafNode("img", "", {"src": "", "alt": ""})
        else:
            raise Exception("Invalid text type")

    @staticmethod
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != "text":
                new_nodes.append(node)
                continue

            chunks = node.text.split(delimiter)
            chunks_length = len(chunks)

            if chunks_length == 1:
                new_nodes.append(node)
                continue

            if chunks_length % 2 == 0:
                raise Exception(f"No opening or closing {delimiter} found in text")

            for i in range(chunks_length):
                # since a split apart string with delimiters will always have an odd number of chunks,
                # each odd numbered chunk will be the part that previously was delimited (i.e. surrounded by **/*/`/etc)
                # even chunks will be the surrounding non-delimited text
                if i % 2 == 0:
                    new_nodes.append(TextNode(chunks[i], "text"))
                else:
                    new_nodes.append(TextNode(chunks[i], text_type))

        return new_nodes

    @staticmethod
    def extract_markdown_images(text):
        matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
        return matches

    @staticmethod
    def extract_markdown_links(text):
        matches = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
        return matches
