from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        return super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("missing value")

        if self.tag is None:
            return f"{self.value}"

        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        attributes = ""

        for k, v in self.props.items():
            attributes += f"{k}=\"{v}\""

        attributes.strip()

        return f"<{self.tag} {attributes}>{self.value}</{self.tag}>"
