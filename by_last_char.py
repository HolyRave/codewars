# https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0
def last(s):
    a = sorted(s.split(),key=lambda c1: c1[-1])
    return a
