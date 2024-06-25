from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None = None, value: str | None = None, props: dict | None = None):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if (self.value == None):
            raise ValueError()
        elif (self.tag == None):
            return self.value
        else:
            return f"<{self.tag}{" " + self.props_to_html() if self.props else ""}>{self.value}</{self.tag}>"
