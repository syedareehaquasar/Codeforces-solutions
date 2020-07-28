def sol(n, a, b):
    for l in range(n):
        if a[l] > b[l]:
            return -1
        for 

tc = int(input())
while tc > 0:
    n = int(input())
    a = input()
    b = input()
    print(sol(n, a, b))