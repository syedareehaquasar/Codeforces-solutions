def solution(n):
    if n % 10 == 0:
        return "codeforces" + (n // 10) * "sssssssss"
    elif n % 2 == 0:
        return "codeforce" + (n//2) * "ses"
    elif (n-1) % 2 == 0 and n > 1:
        return "codeforce" + ((n-1)//2) * "ses" + "s"
    return "codeforces" + (n-1) * "s"

n = int(input())
print(solution(n))