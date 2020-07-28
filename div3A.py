def solution(x, y, n):
    # for i in reversed(range(n + 1)):
    #     if i % x == y:
    #         return i
    if n % x == y:
        return n
    if n % x > y:
        return n - ((n % x) - y)
    else:
        n -= (n % x) + 1
        return  n - ((n % x) - y)
    return 0


tc = int(input())
while tc > 0:
    x, y, n = map(int, input().split())
    print(solution(x, y, n))
    tc -= 1


# accepted