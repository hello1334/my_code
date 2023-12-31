import sys
sys.stdin = open('input.txt', 'r')



def dfs(start):
    cnt = 0
    now = (0,1)
    stack = [(start, now)]
    while stack:
        m, n = stack.pop()
        if n[0] == N-1 and n[1] == N-1:
            cnt += 1
        else:
            if n[0] == N-1:
                if m == 2:
                    continue
            if n[1] == N-1:
                if m == 0:
                    continue
            for t in dir[m]:
                i,j = move[t]
                ni,nj = n
                ni, nj = ni+i, nj+j
                if t == 0 or t == 2:
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:
                        stack.append((t, (ni,nj)))
                else:
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0 and arr[ni-1][nj] == 0 and arr[ni][nj-1] == 0:
                        stack.append((t, (ni, nj)))
    return cnt

# 가로 : 0 대각선 : 1 세로 : 2
dir = {
    0:(0,1),
    1:(0,1,2),
    2:(1,2),
}
#          가로 대각선 세로
move = [(0,1), (1,1), (1,0)]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = dfs(0)
print(ans)