# 숫자 비교하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120807
# 알고리즘: 기초
# 작성자: 이윤서
# 작성일: 2026. 01. 22. 11:17:43

def solution(num1,num2):
    if num1 == num2:
        return 1
    else:
        return -1

num1 = 2
num2 = 3
print(solution(2,3))