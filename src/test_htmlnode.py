import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq1(self):
        props = {"href": "https://www.google.com", "target": "_blank",}
        html_node = HTMLNode(props=props)

        result = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(html_node.props_to_html(), result)
    
    def test_eq2(self):
        html_node = HTMLNode("p", "hello world")

        self.assertTrue(html_node.tag == "p", html_node.value == "hello world")
    

class TestLeafNode(unittest.TestCase):
    def test_paragraph_tag(self):
        leaf_node = LeafNode("p", "This is a paragraph of text.")

        self.assertEqual(leaf_node.to_html(), "<p>This is a paragraph of text.</p>")
    
    def test_anchor_tag(self):
        leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(leaf_node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_value_error(self):
        leaf_node = LeafNode("a", None)

        with self.assertRaises(ValueError, msg="All leaf nodes must have a value!"):
            leaf_node.to_html()


class TestParentNode(unittest.TestCase):
    def test_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

        self.assertEqual(node.to_html(), result)
    
    def test_children_error(self):
        node = ParentNode("p", None)
        
        with self.assertRaises(ValueError, msg="Invalid HTML: no childer"):
            node.to_html()
    
    def test_tag_error(self):
        node = ParentNode(None, [LeafNode(None, "Normal text")])
        
        with self.assertRaises(ValueError, msg="Invalid HTML: no tag"):
            node.to_html()
    
    def test_child(self):
        node = ParentNode("p", [LeafNode(None, "Normal text")])
        
        
        self.assertEqual(node.tag, "p")
        self.assertIsInstance(node.children, list)


if __name__ == "__main__":
    unittest.main()