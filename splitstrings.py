# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
def solution(s):
    if len(s) % 2 != 0:
        s += "_"
    list = []
    list += s[::2]
    list += s[::-2]
    list2 = []
    for ind in range(int(len(list)/2)):
      list2.append(list[0]+list[-1])
      list = list[1:-1]
    return list2
