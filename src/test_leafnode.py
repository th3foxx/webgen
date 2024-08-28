import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq1(self):
        leaf_node = LeafNode("p", "This is a paragraph of text.")

        return self.assertEqual(leaf_node.to_html(), "<p>This is a paragraph of text.</p>")
    
    def test_eq2(self):
        leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        return self.assertEqual(leaf_node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_eq3(self):
        leaf_node = LeafNode("a", None)

        with self.assertRaises(ValueError, msg="All leaf nodes must have a value!"):
            leaf_node.to_html()


if __name__ == "__main__":
    unittest.main()