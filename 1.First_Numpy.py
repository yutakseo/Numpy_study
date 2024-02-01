'''
넘파이 특징
1. 과학 연산을 위한 라이브러리
2. 행렬/배열 처리 및 연산
3. 난수 생성
'''

#1.배열의 생성
import numpy as np

#2차원 리스트 a 생성
a = [[1,2,3],[4,5,6]]

#넘파이 배열 생성
b = np.array(a)
print(b)
#b 배열의 차원 출력
print(b.ndim)
#b배열에서 (0,0)번째 원소 접근
print(b[0,0])


#1.2특수배열 생성
print(np.arange(10))
print(np.arange(5, 10))
print(np.zeros((2,2)))  # 0행렬 생성
print(np.ones((2,2)))   # 1행렬 생성

print(np.full((2,3), 7)) #모든 원소가 7인 2*3 행렬생성

print(np.eye(3))        #단위행렬
print(np.eye(5))