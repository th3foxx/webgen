import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq1(self):
        props = {"href": "https://www.google.com", "target": "_blank",}
        html_node = HTMLNode(props=props)

        result = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(html_node.props_to_html(), result)
    
    def test_eq2(self):
        html_node = HTMLNode("p", "hello world")

        self.assertTrue(html_node.tag == "p", html_node.value == "hello world")


if __name__ == "__main__":
    unittest.main()