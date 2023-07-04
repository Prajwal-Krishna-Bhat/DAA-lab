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

