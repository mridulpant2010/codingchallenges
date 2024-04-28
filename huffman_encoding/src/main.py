import heapq
from collections import Counter


#how to correct the import issue.
def read_file(file_path,file_name):
    #TODO: need to make it parameterized such that it picks the correct.
    with open(file_path, 'r') as f:
        data = f.readline()
        

#TODO: for better structuring of the code it needs to be placed somewhere else. I think we can place 
class InternalNodes:
    def __init__(self,weight,left,right) -> None:
        self.weight=weight
        self.left=left
        self.right=right

    def __lt__(self,other):
        return self.weight < other.weight

class LeafNodes:
    def __init__(self,char,weight):
        self.char=char
        self.weight=weight
        
    def __lt__(self,other):
        return self.weight < other.weight

def build_heap(frequency_map:dict) -> None:
    """function to build the heap based on the logic

    Args:
        frequency_map (dict): Counter of frequency occurrences of a character.

    Returns:
        InternalNodes: root Node of the heap.
    """
    if len(frequency_map) == 0: return None
    he = []
    for k,v in frequency_map.items():
        heapq.heappush(he,LeafNodes(k,v))

    while len(he) > 1:
        first= heapq.heappop(he)
        second = heapq.heappop(he)
        third:InternalNodes = InternalNodes(first.weight + second.weight,first,second)
        heapq.heappush(he,third)
    return he[0]

def encode(root,current_codes,stored_code):
    """encodes the current character until the leaf node is encountered. Assigns 0 to the left node and 1 to the right node. 

    Args:
        root (InternalNode): root of the heap.
        current_codes (str): assigns either 0 or 1 codes to the current node. 
        stored_code (dict): dict mapping with a character as key and the 0/1 frequncy of the character.
    """    
    if isinstance(root,LeafNodes) and root.char is not None:
        stored_code[root.char] = current_codes
        return
    
    encode(root.left,current_codes + '0',stored_code)
    encode(root.right,current_codes + '1',stored_code)
    

#TODO: is the encoding logic correct?
def huffman_encoding(text):
    """given a text encodes a string based on the huffman encoding logic.

    Args:
        text (str): string to encode

    Returns:
        encoded_text: str
        build_node: Node
    """
    if text =='':
        return text,None
    
    dict_mapping = Counter(text)
    build_node = build_heap(dict_mapping)
    codes = {}
    encode(build_node,'',codes)
    print(codes)
    encoded_text = ''.join([codes[char]for char in text])
    return encoded_text,build_node

#INFO: heapq must also be doing some sort of comparison and how does that happen
#how i used to do in my previous code implementation then. Since i have given the class object instead of the value in heap, so how will it do the comparison?


#what is the logic for this ?
#decoding logic needs to be checked for this.
def huffman_decoding(encoded_text,root):
    """generates the encoded string to a 

    Args:
        encoded_text (str): encoded text generated from the 
        root (InternalNode): root of the heap.

    Returns:
        decoded_text: returns the actual decoded string.
    """
    decoded_text = ""
    current_node:InternalNodes=root
    for bits in encoded_text:
        if bits=='0':
            current_node=current_node.left
        else:
            current_node=current_node.right
            
        if isinstance(current_node,LeafNodes):
            decoded_text+=current_node.char
            current_node=root
    return decoded_text