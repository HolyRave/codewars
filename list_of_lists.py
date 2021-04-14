# https://www.codewars.com/kata/586e1d458cb711f0a800033b
def process_data(data):
    prod = 1
    for list in data:
        prod *= (list[0] - list[1])
    return prod
