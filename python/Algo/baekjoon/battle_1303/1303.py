import sys
sys.stdin = open("input.txt", 'r')
# input = sys.stdin.readline

def dfs(si,sj, color):
    visited[si][sj] = 1
    stack = [(si,sj)]
    cnt = 1
    while stack:
        i,j = stack.pop()
        for ni,nj in [(i+1,j),(i,j+1),(i-1,j),(i,j-1),]:
            if 0<=ni<M and 0<=nj<N and visited[ni][nj] == 0 and field[ni][nj] == color:
                visited[ni][nj] = 1
                cnt += 1
                stack.append((ni,nj))
    return cnt*cnt

N,M = map(int, input().split())
field = [input().strip() for _ in range(M)]
visited = [[0]*N for _ in range(M)]
blue_count = 0
white_count = 0
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            if field[i][j] == 'W':
                white_count += dfs(i,j, 'W')
            else:
                blue_count += dfs(i,j, 'B')
print(white_count, blue_count)