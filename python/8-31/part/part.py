import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    subset = []
    total = 0
    for i in range(1<<N):
        tmp = []
        for j in range(N):
            if i&(1<<j):
                tmp.append(arr[j])
        if sum(tmp) == K:
            total += 1
    print(f'#{tc} {total}')