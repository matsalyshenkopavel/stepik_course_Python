n, k = map(int, input().split())
def rec(n, k):
    if k > n:
        return 0
    elif k == 0:
        return 1
    else:
        return rec(n - 1, k) + rec(n - 1, k - 1)

print(rec(n, k))