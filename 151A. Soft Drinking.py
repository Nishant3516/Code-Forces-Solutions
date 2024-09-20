n, k, l, c, d, p, nl, np = list(map(int, input().split()))

val1 = (k*l)//nl
val2 = c*d
val3 = p//np

print(min(val1, val2, val3)//n)
