from htmlnode import HTMLNode
from typing import List


class ParentNode(HTMLNode):
    def __init__(self, tag: str,  children: list['HTMLNode'], props: dict | None = None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("requires a tag")
        elif self.children == None:
            raise ValueError("requires children")
        else:
            values = "".join([child.to_html() for child in self.children])
            return f"<{self.tag}{" " + self.props_to_html() if self.props else ""}>{values}</{self.tag}>"
