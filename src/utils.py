from leafnode import LeafNode


class Utils(object):

    @staticmethod
    def text_node_to_html_node(text_node):
        text_type = text_node.text_type
        if text_type is "text":
            return LeafNode(None, text_node.text)
        elif text_type is "bold":
            return LeafNode("b", text_node.text)
        elif text_type is "italic":
            return LeafNode("i", text_node.text)
        elif text_type is "code":
            return LeafNode("code", text_node.text)
        elif text_type is "link":
            return LeafNode("a", text_node.text, {"href": ""})
        elif text_type is "image":
            return LeafNode("img", "", {"src": "", "alt": ""})
        else:
            raise Exception("Invalid text type")
