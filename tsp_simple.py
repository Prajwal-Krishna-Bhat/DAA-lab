graph = [[0 for i in range(100)] for i in range(100)]
vis = [0 for i in range(100)]
start = 1
n = -1

def tsp(cur) :
    vis[cur] = 1
    bestCost= 99999
    bestVertex = -1
    bestPath = ""
    
    for i in range(1,n+1) : 
        if vis[i]:
            continue
        cost,path = tsp(i)
        
        if cost+graph[cur][i]<bestCost: 
            bestCost = cost+graph[cur][i]
            bestVertex = i
            bestPath = path
    vis[cur] = 0
    
    if bestVertex==-1:
        bestPath = (str(cur) + " -> " + str(start))
        return graph[cur][start],bestPath
        
    bestPath = (str(cur) + " -> " + bestPath)
    return bestCost,bestPath
    
n = int(input("Enter number of cities: "))
print("Enter the cost matrix:")
graph = [[0 for i in range(n+1)] for i in range(n+1)]

for i in range(1,n+1):
    l = list(map(int,input().split()))
    for j in range(1,n+1):
        graph[i][j] = l[j-1]
        
print("The cost matrix is: ")
for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j],end="\t")
    print()
    
cost,bestPath = tsp(start)
print("Optimal solution:")
print("The path is:")
print(bestPath)
print("Minimum cost is ",cost)