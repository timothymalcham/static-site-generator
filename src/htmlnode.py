#
# The HTMLNode class represents a "node" in an HTML document tree
# (like a <p> tag and its contents, or an <a> tag and its contents)
# and is purpose-built to render itself as HTML
#
class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("missing value")

        if self.tag is None:
            raise ValueError("missing tag")

        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        attributes = ""

        for k, v in self.props.items():
            attributes += f"{k}=\"{v}\""

        attributes.strip()

        return f"<{self.tag} {attributes}>{self.value}</{self.tag}>"

    def props_to_html(self):
        props_str = ""
        if self.props is None:
            return props_str
        for k, v in self.props.items():
            props_str += f"{k}=\"{v}\" "
        return props_str.strip()

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
