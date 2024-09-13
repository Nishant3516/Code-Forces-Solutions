k, n, w = map(int, input().split())
total_cost = k * (w * (w + 1)) // 2
borrowed_amount = max(0, total_cost - n)
print(borrowed_amount)