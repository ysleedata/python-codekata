# 배열의 평균값
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120817
# 알고리즘: 기초
# 작성자: 이윤서
# 작성일: 2026. 02. 25. 09:21:18

def solution(numbers):
    sn = sum(numbers)
    ln = len(numbers)
    result = round((sn / ln), 2)
    return result

numbers = [1,2,3,4]
print(solution(numbers))