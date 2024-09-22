def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return True
    return False


def find_two_composite(n):
    for x in range(4, n // 2 + 1):
        if is_composite(x) and is_composite(n - x):
            return x, n - x
    return None


# Reading input
n = int(input())
result = find_two_composite(n)
if result:
    print(result[0], result[1])
