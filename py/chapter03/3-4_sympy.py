from sympy import Symbol, solve

# 식을 정의
a = Symbol('a')
b = Symbol('b')
ex1 = a + b - 1
ex2 = 5 * a + b - 3

# 연립방정식 풀기
print(solve((ex1, ex2)))
