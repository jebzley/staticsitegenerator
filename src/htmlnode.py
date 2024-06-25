class HTMLNode:
    def __init__(self, tag: str | None = None, value: str | None = None, children: list['HTMLNode'] = None, props: dict | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if (self.props):
            if (type(self.props) != dict):
                raise TypeError()

            return " ".join([f'{item[0]}="{item[1]}"' for item in self.props.items()])

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
