import math  # importe math lib to exercise 10


# # #### Inteiros (`int`)

# """
# 1. Escreva um programa que soma dois números inteiros
# inseridos pelo usuário.
# """

# number_1 = int(input('Type the first integer number: '))
# number_2 = int(input('Type the second integer number: '))


# nummber_sum = number_1 + number_2

# print(f'The sum of {number_1} and {number_2} is {nummber_sum}.')


# """
#  2. Crie um programa que receba um número do usuário
#  e calcule o resto da divisão desse número por 5.
# """

# number = int(input('Type an integer number: '))

# division_rest_number = number % 5

# print(f'The division rest from {number} is {division_rest_number}.')

# """
# 3. Desenvolva um programa que multiplique
# dois números fornecidos pelo usuário e mostre o resultado.
# """

# number_1 = int(input('Type the first integer number: '))
# number_2 = int(input('Type the second integer number: '))

# number_product = number_1 * number_2

# print(f'The product of {number_1} and {number_2} is {number_product}')


# """
# 4. Faça um programa que peça dois números inteiros e
# imprima a divisão inteira do primeiro pelo segundo.
# """

# number_1 = int(input('Type the integer number 1 to be divided: '))
# number_2 = int(input('Type the integer number 2 to be divided: '))

# integer_division = number_1 // number_2

# print(f'The integer division by {number_1} and'
#       f'{number_2} is {integer_division}')


# """
# 5. Escreva um programa que calcule
# o quadrado de um número fornecido pelo usuário.
# """

# number = int(input('Type a number: '))

# power_number = number**2

# print(f'The power of {number} ins {power_number}.')


# #### Números de Ponto Flutuante (`float`)


# """
# 6. Escreva um programa que receba
# dois números flutuantes e realize sua adição.
# """

# number_1 = float(input("Type a float number: "))
# number_2 = float(input("Type other float number: "))

# sum_float_numbers = number_1 + number_2

# print(f"The sum of {number_1} and {number_2} is {sum_float_numbers}.")


# """
# 7. Crie um programa que calcule a média de
# dois números flutuantes fornecidos pelo usuário.
# """

# number_1 = float(input("Type the first float number: "))
# number_2 = float(input("Type the second float number: "))

# average_numbers = (number_1 + number_2) / 2

# print(f"The average number between "
#       f"{number_1} and {number_2} is {average_numbers}.")


# """
# 8. Desenvolva um programa que calcule a potência de
# um número (base e expoente fornecidos pelo usuário).
# """


# number_base = float(input("Type the base number: "))
# number_exponent = float(input("Type the exponent number: "))

# power_number = number_base**number_exponent

# print(f"The power between "
#       f"{number_base} and {number_exponent} is {power_number}.")


# """
# 9. Faça um programa que converta a temperatura
# de Celsius para Fahrenheit.
# Temperature in degrees Fahrenheit
# (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32
# """

# celsius_degree = float(input("Type a temperature in Celsius: "))

# fahrenheint_degree = ((celsius_degree * 9/5) + 32)

# print(f"The celsius temperature in celsius {celsius_degree} "
#       f"is equivalent to {fahrenheint_degree} Fahrenheit.")


# """
# 10. Escreva um programa que calcule a área
# de um círculo, recebendo o raio como entrada.
# The area of a circle is calculated using the formula A = πr²,
# where A represents the area, π (pi) is a mathematical constant
# approximately equal to 3.14159, and r is the radius of the circle.
# Identify the radius (r): The radius is the distance from
# the center of the circle to any point on its edge.
# Square the radius (r²): Multiply the radius by itself (r * r).
# Multiply by π (pi): Multiply the squared radius (r²) by the
# mathematical constant π (approximately 3.14159).
# """

# PI_CONSTANT = math.pi


# radius = float(input("Type the radius from a circle: "))

# circle_area = PI_CONSTANT * (radius ** 2)

# print(f"The area from a circle with radius {radius} is {circle_area:.02f}.")

# #### Strings (`str`)

# """
# 11. Escreva um programa que receba uma
# string do usuário e a converta para maiúsculas.
# """

# string_input = str(input("Type a string: "))

# string_upper = string_input.upper()

# print(f"The string {string_input} in upper case is {string_upper}.")

# """
# 12. Crie um programa que receba o nome completo
# do usuário e imprima o nome com todas as letras minúsculas.
# """

# complete_name = str(input("Type your complete name: "))

# complet_name_lower = complete_name.lower()

# print(f"Your complete name {complete_name} "
#       f"in lower case is {complet_name_lower}.")


# """
# 13. Desenvolva um programa que peça ao usuário para inserir
# uma frase e, em seguida, imprima esta frase
# sem espaços em branco no início e no final.
# """

# phrase = str(input("Type a phrase: "))

# phrase_without_space = phrase.strip()


# print(f"The phrase {phrase} without spaces is {phrase_without_space}.")


# """
# 14. Faça um programa que peça ao usuário para digitar
# uma data no formato "dd/mm/aaaa" e, em seguida,
# imprima o dia, o mês e o ano separadamente.
# """

# date = str(input("Type a date in the format dd/mm/yyyy: "))

# day = date[0:2]
# month = date[3:5]
# year = date[6:10]

# print(f"From your date {date}, the day is {day}, "
#       f"the month is {month} and the year is {year}.")


"""
15. Escreva um programa que concatene
duas strings fornecidas pelo usuário.
"""

string_1 = str(input("type a string: "))
string_2 = str(input("Type other string: "))

concatenated_string = string_1 + string_2

print(f"The string concatenated is {concatenated_string}.")

# #### Booleanos (`bool`)

"""
16. Escreva um programa que avalie duas expressões booleanas
inseridas pelo usuário e retorne o
resultado da operação AND entre elas.
"""

"""
17. Crie um programa que receba dois valores booleanos do usuário e retorne o
resultado da operação OR.
"""

"""
18. Desenvolva um programa que peça ao usuário para inserir um valor booleano
e, em seguida, inverta esse valor.
"""

"""
19. Faça um programa que compare se dois números fornecidos
pelo usuário são iguais.
"""

"""
20. Escreva um programa que verifique se dois números
 fornecidos pelo usuário são diferentes.
"""

# #### try-except e if

"""
21: Conversor de Temperatura
"""

"""
22: Verificador de Palíndromou
"""

"""
23: Calculadora Simples
"""

"""
24: Classificador de Números
"""

"""
25: Conversão de Tipo com Validação
"""
