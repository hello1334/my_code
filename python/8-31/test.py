'''
재귀 호출을 이용한 조합 생성 알고리즘
조합은 순열과 다르게 순서상관없이 중복되지 않은 조합만 호출
'''

def ncr(n, r):
    if r==0:
        print(tr)
    elif n<r:       # 남은 원소보다 많은 원소를 선택해야 하는 경우
        return
    else:
        tr[r-1] = a[n-1]       # [n-1] 조합에 포함시키는 경우
        ncr(n-1, r-1)
        ncr(n-1, r)            # a[n-1]을 포함시키지 않는 경우



N = 5
R = 3
a = [1, 2, 3, 4, 5]
tr = [0]*R
ncr(N, R)

