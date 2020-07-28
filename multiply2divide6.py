def solution(n):
    if n == 1:
        return 0
    i, j = 0, 0
    while n % 3 == 0:
        i += 1
        n //= 3
    while n % 2 == 0:
      n //= 2
      j += 1
    if n == 1 and j <= i:
        return i + (i-j)
    return -1
    
tc = int(input())
while tc > 0:
    n = int(input())
    print(solution(n))
    tc -= 1
