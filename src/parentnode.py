from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag = None, children = None, props = None):
        return super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag")

        if self.children is None or len(self.children) == 0:
            raise ValueError("No children found")

        opening_tag = f"<{self.tag}>"
        closing_tag = f"</{self.tag}>"

        children_to_html = ""

        for child in self.children:
            children_to_html += child.to_html()

        return f"{opening_tag}{children_to_html}{closing_tag}"
