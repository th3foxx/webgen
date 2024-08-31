from textnode import (
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    TextNode
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        parts = old_node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i, part in enumerate(parts):
            if i % 2 == 1:
                new_nodes.append(TextNode(part, text_type))
            elif part:
                new_nodes.append(TextNode(part, text_type_text))

    return new_nodes