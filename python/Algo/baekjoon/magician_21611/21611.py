import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
blizzard = [list(map(int, input().split())) for _ in range(M)]
