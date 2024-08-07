def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        count_divisor = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                if i == j**2:
                    count_divisor += 1
                else:
                    count_divisor += 2
        if count_divisor > limit:
            answer += power
        else:
            answer += count_divisor
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/136798
