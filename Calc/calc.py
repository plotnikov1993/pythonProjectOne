import log as log1

def calc(a, b):
    point = input('\tВведите знак: ')
    if point == '+':
        result = a + b
        print(result)
        log1.log(f'{a}+{b}={result}')
    elif point ==  '-':
        result = a - b
        print(result)
        log1.log(f'{a}-{b}={result}')
    elif point == '*':
        result = a * b
        print(result)
        log1.log(f'{a}*{b}={result}')
    elif point == '/':
        if b == 0:
            print("Деление на 0 не допускается")
        else:
            result = a /b
            print(result)
            log1.log(f'{a}/{b}={result}')