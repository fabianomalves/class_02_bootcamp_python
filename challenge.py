# Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

try:
    name = str(input('Type your name: '))

    if len(name) == 0:
        raise ValueError('The name cannot be empty.')
        exit()
    elif any(char.isdigit() for char in name):
        raise ValueError('The name cannot contain numbers.')
        exit()
    else:
        print('The name is valid: ', name)
except ValueError as e:
    print(e)
    exit()

# 2) Solicita ao usuário que digite o valor do seu salário e converte para float

try:
    salary = float(input('Type your salary: '))
    if salary < 0:
        print('Inform a positive salary number: ')
    else:
        print('The salary is valid: ', salary)
except ValueError as e:
    print(f'Invalid information for salary {e}. Inform a number.')
    exit()


# 3) Solicita ao usuário que digite o valor do bônus recebido e converte para float

try:
    bonus = float(input('Type the bonus received: '))
    if bonus < 0:
        print('Inform a positive number: ')
    else:
        print(('Your bonus is valid: ', bonus))
except ValueError as e:
    print(f'Invalid information for the bonus {e}. Inform a number.')
    exit()
