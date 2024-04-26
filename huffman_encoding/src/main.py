import heapq
from collections import Counter


#how to correct the import issue.
def read_file(file_path,file_name):
    with open(file_path, 'r') as f:
        data = f.readline()
        # TODO: read each character and prepare a frequency map
        '''my approach
        - TODO[primary]: file_path default is the cwd, take file_name as input argument.
        - TODO[optional]: otherwise the first argument is the file_path and the 
        
        split each of the data into a list and iterate over each of the character
        
        better approach
        
        
        '''
        
def build_frequency_map(text:str):
    freq_map = Counter(text)
    return freq_map



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
    he = []
    for k,v in frequency_map.items():
        heapq.heappush(he,LeafNodes(k,v))

    while len(he) > 1:
        first= heapq.heappop(he)
        second = heapq.heappop(he)
        third:InternalNodes = InternalNodes(first.weight + second.weight,first,second)
        heapq.heappush(he,third)
    return he[0]


def huffman_decoding():
    pass

def huffman_encoding():
    pass

#INFO: heapq must also be doing some sort of comparison and how does that happen
#how i used to do in my previous code implementation then. Since i have given the class object instead of the value in heap, so how will it do the comparison?