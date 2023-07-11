import heapq
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq=freq
        self.symbol=symbol
        self.left=left
        self.right=right
        self.huff=''

    def __lt__(self, nxt):
        return self.freq< nxt.freq
def print_nodes(node,val=''):
    newval= val + str(node.huff)
    if(node.left):
        print_nodes(node.left, newval)
    if(node.right):
        print_nodes(node.right, newval)
    if(not node.left and not node.right):
        print(f"{node.symbol} -> {newval}")
chars=[]
n=int(input("Enter the nodes:"))
for i in range(0,n):
    l=input(f"Node {i+1}:")
    chars.append(l)
freq=[]
print("Enter the frequencies:\n")
for i in range(0,n):
    m=int(input(f"frequency of node {i+1}:"))
    freq.append(m)
nodes=[]
for x in range(len(chars)):
    heapq.heappush(nodes, Node(freq[x],chars[x]))

while len(nodes)>1:
    left=heapq.heappop(nodes)
    right=heapq.heappop(nodes)
    left.huff=0
    right.huff=1
    newNode=Node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    heapq.heappush(nodes, newNode)
print_nodes(nodes[0])
def decode_text(encoded_text, starting_node):
    decoded_text = ''
    current_node = starting_node

    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if not current_node.left and not current_node.right:
            decoded_text += current_node.symbol
            current_node = starting_node

    return decoded_text

starting_node = nodes[0]

encoded_text = input("Enter the encoded text: ")
decoded_text = decode_text(encoded_text, starting_node)
print("Decoded text:", decoded_text)
