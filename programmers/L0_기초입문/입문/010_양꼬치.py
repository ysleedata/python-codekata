# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 이윤서
# 작성일: 2026. 02. 05. 17:00:07

def solution(n,k):
    k = k - (n // 10)
    if k < 0:
        k = 0
   
    result = (12000 * n) + (2000 * k)
    return result
    