# https://www.codewars.com/kata/514b92a657cdc65150000006
def solution(number):
    cnt = 0
    for i in range(number):
        cnt += i if i % 3 == 0 or i % 5 == 0 else 0
    return cnt
