import re
from textnode import (TextNode, text_types, text_type_text,
                      text_type_image, text_type_link)


def split_nodes_delimiter(old_nodes: list['TextNode'], delimiter: str, text_type: str):
    if text_type not in text_types:
        raise TypeError("Invalid text type")

    new_nodes = []
    for node in old_nodes:
        if (node.text_type != text_type_text):
            new_nodes.append(node)
        else:
            current_node_split = []
            split_string_delimiter(
                node.text, delimiter, current_node_split, text_type)
            new_nodes.extend(current_node_split)
    return new_nodes


def split_nodes_images(old_nodes: list['TextNode']):
    output = []
    for node in old_nodes:
        split_node_img_or_link(node, text_type_image, output)

    return output


def split_nodes_links(old_nodes: list['TextNode']):
    output = []
    for node in old_nodes:
        split_node_img_or_link(node, text_type_link, output)

    return output


def split_string_delimiter(t: str, d: str, a: list['TextNode'], text_type: str):
    s = t.split(d, 2)
    if (len(s)) == 1:
        if (s[0] != ""):
            a.append(TextNode(s[0], text_type_text))
    elif len(s) == 2:
        raise Exception(f'string or chunk: "{t}" is missing a tag "{d}"')
    else:
        if (s[0] != ""):
            a.append(TextNode(s[0], text_type_text))
        if (s[1] != ""):
            a.append(TextNode(s[1], text_type))
        split_string_delimiter(s[2], d, a, text_type)


def extract_markdown_images(text: str):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str):
    return re.findall(r"(?<!\!)\[([^\]]+)\]\(([^\)]+)\)", text)


def split_node_img_or_link(node: TextNode, text_type: str, output_list: list[TextNode]):
    if (text_type not in [text_type_image, text_type_link]):
        raise ValueError("split_node requires image or link")

    found_items = extract_markdown_images(
        node.text) if text_type == text_type_image else extract_markdown_links(node.text)

    if len(found_items) == 0:
        output_list.append(node)
    else:
        for item in found_items:
            item_node = TextNode(item[0], text_type, item[1])
            delimiter = f"{"!" if text_type == text_type_image else ""}[{item[0]}]({
                item[1]})"
            split_text = node.text.split(delimiter, 1)
            if split_text[0] == '' or split_text[0].isspace():
                output_list.extend(
                    [item_node, TextNode(split_text[1], text_type_text)])
            elif split_text[1] == '' or split_text[1].isspace():
                output_list.extend(
                    [TextNode(split_text[0], text_type_text), item_node])
            else:
                output_list.extend([TextNode(split_text[0], text_type_text), item_node, TextNode(
                    split_text[1], text_type_text)])
