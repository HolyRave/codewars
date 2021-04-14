# https://www.codewars.com/kata/57e3f79c9cb119374600046b
def hello(name=''):
    if len(name) == 0:
        return "Hello, World!"
    else:
        return f'Hello, {name.capitalize()}!'
