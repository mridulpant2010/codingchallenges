import heapq


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
        
def build_frequency_map():
    pass


def build_tree() -> None:
    pass

class Node:
    def __init__(self,val,weight):
        self.val=val
        self.weight=weight

def build_heap(frequency_map:dict) -> None:
    he = []
    for k,v in frequency_map.iteritems():
        heapq.heappush(he,Node(k,v))

    while len(he) > 0:
        first= heapq.heappop(he)
        second = heapq.heappop(he)
        third = Node(first.val + second.val)
        heapq.heappush(he,third)
    print(third)
        
    