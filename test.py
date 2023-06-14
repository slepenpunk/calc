def calc(expression):
    try:
        return eval(expression)
    except:
        return 'Invalid data!'


expression = input('Enter expression: ')
solution = calc(expression)
print(solution)
