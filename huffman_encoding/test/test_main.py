import os
import sys
import unittest
from collections import Counter

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
# print(parent_dir)
from src.main import (
    InternalNodes,
    LeafNodes,
    build_heap,
    encode,
    huffman_decoding,
    huffman_encoding,
)


# from src.models import InternalNodes, LeafNodes
class TestCompression(unittest.TestCase):
    text_str = """Hello World"""

    def test_build_heap(self):
        # test case 1: test build_heap with the empty frequency map.
        frequency_map_empty = {}
        root_empty = build_heap(frequency_map_empty)
        self.assertIsNone(root_empty)

        # test case 2:
        dict_mapping = Counter(self.text_str)
        node = build_heap(dict_mapping)
        self.assertEqual(type(node), InternalNodes)

    def test_encode(self):

        # test case 1: test encode with a Leaf node.
        leaf_nodes = LeafNodes("a", 5)
        codes = {}
        encode(leaf_nodes, "", codes)
        self.assertEqual(codes["a"], "")

        # test case 2: test encode with with an internal node.
        left = LeafNodes("a", 5)
        right = LeafNodes("b", 3)
        codes = {}
        encode(left, "0", codes)
        encode(right, "1", codes)
        self.assertEqual(codes["a"], "0")
        self.assertEqual(codes["b"], "1")

    def test_huffman_encoding(self):

        # test case 1: test with an empty string
        empty_string, empty_node = huffman_encoding("")
        self.assertEqual(empty_string, "")
        self.assertIsNone(empty_node)

        # dict_mapping = Counter(self.text_str)
        # node:InternalNodes = build_heap(dict_mapping)
        encoded_text, root = huffman_encoding(self.text_str)
        self.assertEqual(type(encoded_text), str)
        self.assertEqual(type(root), InternalNodes)

    def test_huffman_decoding(self):
        # decide how many test cases can be formed.
        # case1: when the encoded text is '' and root is None.
        encoded_text = ""
        root = None
        decoded_text = huffman_decoding(encoded_text, root)
        self.assertEqual(decoded_text, "")

        # case2: when the encoded text is not and root exists.
        encoded_text, root = huffman_encoding(self.text_str)
        decoded_text = huffman_decoding(encoded_text, root)
        self.assertEqual(decoded_text, self.text_str)


if __name__ == "__main__":
    unittest.main()
