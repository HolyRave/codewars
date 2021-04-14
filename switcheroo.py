# https://www.codewars.com/kata/57f759bb664021a30300007d/
def switcheroo(string):
    return "".join([ ch.replace('a','b') if ch=="a" else ch.replace('b','a') for ch in string ])
