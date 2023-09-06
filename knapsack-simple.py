def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)
    return max(
        val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
        knapSack(W, wt, val, n - 1)
    )

n = int(input("Enter the number of items: "))
profit = []
weight = []
for i in range(n):
  item_profit = int(input(f"Enter profit for item {i}: "))
  profit.append(item_profit)
  item_wt = int(input(f"Enter weight of item {i}: "))
  weight.append(item_wt)

W = int(input("Enter total Knapsack Capacity: "))
print(knapSack(W, weight, profit, n))
