# 큰 수의 법칙

import sys

# N,M,K를 공백으로 구분하여 입력받기
N,M,K = map(int,sys.stdin.readline().split())
data = sorted(list(map(int,sys.stdin.readline().split())))
result = 0

first = data[-1]
second = data[-2]
while True:
    for i in range(K):
        if M == 0:
            break
        result += first
        M-=1
    if M == 0:
        break
    result+=second
    M-=1

print(result)