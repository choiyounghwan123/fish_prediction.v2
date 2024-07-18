# 큰수의 법칙 - 수학적 풀이

import sys

# N,M,K를 공백으로 구분하여 입력받기
N,M,K = map(int,sys.stdin.readline().split())

# N개의 수를 공백으로 구분하여 입력받은 후 정렬
data = sorted(list(map(int,sys.stdin.readline().split())))
first = data[-1] # 가장 큰수
second = data[-2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(M/(K+1)) * K
count +=  M%(K+1)

res = count * first
res += (M-count) * second
print(res)

