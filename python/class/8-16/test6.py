#순열1
def f(i, N):
    if i == N:
        print(A)
    else:
        # 자신부터 오른쪽 끝까지
        for j in range(i, N):
            A[i], A[j] = A[j], A[i]
            f(i+1,N)
            A[i], A[j] = A[j], A[i]
A = [0,1,2]
f(0, 3)