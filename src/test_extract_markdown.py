import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdownImages(unittest.TestCase):
    def test_link_eq1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)

        self.assertEqual(result[0][0], "rick roll")
        self.assertEqual(result[0][1], r"https://i.imgur.com/aKaOqIh.gif")
    
    def test_link_eq2(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)

        self.assertEqual(result[1][0], "obi wan")
        self.assertEqual(result[1][1], r"https://i.imgur.com/fJRm4Vk.jpeg")


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_link_eq1(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)

        self.assertEqual(result[0][0], "to boot dev")
        self.assertEqual(result[0][1], r"https://www.boot.dev")
    
    def test_link_eq2(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)

        self.assertEqual(result[1][0], "to youtube")
        self.assertEqual(result[1][1], r"https://www.youtube.com/@bootdotdev")