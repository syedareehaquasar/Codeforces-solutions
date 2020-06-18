def solution(s : str, k : int, n : int) -> int:
    for i, v in enumerate(s):
        if v == 1:
            if i > k:
                ans += 

tc = int(input())
for i in range(tc):
    n, k = [int(x) for x in input().split()]
    s = input()
    print(solution(s, k, n))