import unittest

from textnode import TextNode, text_type_bold, text_type_italic


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("Alpha", text_type_bold)
        node2 = TextNode("Alpha", text_type_italic)
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("Alpha", text_type_bold)
        self.assertEqual(node.text_type, "bold")
    
    def test_eq4(self):
        node = TextNode("Alpha", text_type_italic)
        self.assertEqual(node.url, None)


if __name__ == "__main__":
    unittest.main()