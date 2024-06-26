from math import inf
def divide(first, second):
    if second == 0:
        return 'math(inf)'
    else:
        return first / second

print(divide(50, 0))
print(divide(500, 100))


