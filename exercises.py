import math  # importe math lib to exercise 10
import ast  # import ast lib to exercise 16
import operator  # import operator lib to exercise 16


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
# import math  # importe math lib to exercise 10
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


# """
# 15. Escreva um programa que concatene
# duas strings fornecidas pelo usuário.
# """

# string_1 = str(input("type a string: "))
# string_2 = str(input("Type other string: "))

# concatenated_string = string_1 + string_2

# print(f"The string concatenated is {concatenated_string}.")

# # #### Booleanos (`bool`)

# """
# 16. Escreva um programa que avalie duas expressões booleanas
# inseridas pelo usuário e retorne o
# resultado da operação AND entre elas.
# """

# """
# With this simple code,
# with two booleans variables,
# we can evaluate the AND operation.
# This without user's input.
# """

# boolean_1 = True
# boolean_2 = True

# result_boolean = boolean_1 and boolean_2

# print(f"The result between {boolean_1} AND {boolean_2} is {result_boolean}.")

# """It's possible to use eval() to evaluate boolean expressions,
# but be careful with the input, as it can lead to security
# issues if not properly sanitized.
# """

# boolean_1 = input("Type a boolean: ")
# boolean_2 = input("Type other boolean: ")

# try:
#     result_1 = eval(boolean_1)
#     result_2 = eval(boolean_2)

#     final_result = result_1 and result_2
#     print(f"The final result between {result_1} "
#           f"and {result_2} is {final_result}")
# except Exception as e:
#     print(f"And error occurred: {e}")

# """
# Or try this safe_eval(expr) function, to evaluate boolean
# expressions with secure input:
# """


# def safe_eval(expr):
#     ops = {
#         ast.Eq: operator.eq,
#         ast.NotEq: operator.ne,
#         ast.Gt: operator.gt,
#         ast.Lt: operator.lt,
#         ast.GtE: operator.ge,
#         ast.LtE: operator.le,
#     }

#     node = ast.parse(expr, mode="eval")

#     def _eval(node):
#         if isinstance(node, ast.Expression):
#             return _eval(node.body)
#         if isinstance(node, ast.Compare):
#             left = _eval(node.left)
#             right = _eval(node.comparators[0])
#             op = type(node.ops[0])
#             if op in ops:
#                 return ops[op](left, right)
#             else:
#                 raise ValueError("Operator not allowed")
#         if isinstance(node, ast.Constant):
#             return node.value
#         raise ValueError("Expression not allowed")

#     return _eval(node)


# expression_1 = (
#     input("Type one boolean expression, (like 5 > 3 or true):")
#     .strip()
#     .lower()
#     .replace("true", "True")
#     .replace("false", "False")
# )
# expression_2 = (
#     input("Type other boolean expression, (like 5 == 5 or false):")
#     .strip()
#     .lower()
#     .replace("true", "True")
#     .replace("false", "False")
# )

# try:
#     result_1 = safe_eval(expression_1)
#     result_2 = safe_eval(expression_2)
#     final_result = result_1 and result_2

#     print(
#         f"The bolean result between {result_1} "
#         f"AND {result_2} is {final_result}")

# except Exception as e:
#     print(f"An erro occured: {e}")


# """
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o
# resultado da operação OR.
# """

# boolean_1 = False
# boolean_2 = True

# result_boolean = boolean_1 or boolean_2

# print(f"The result between {boolean_1} OR {boolean_2} is {result_boolean}.")


# """
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano
# e, em seguida, inverta esse valor.
# """

# boolean_value = True

# boolean_inverted = not boolean_value

# print(f"The boolean value {boolean_value} inverted is {boolean_inverted}.")

# """
# 19. Faça um programa que compare se dois números fornecidos
# pelo usuário são iguais.
# """

# number_1 = 2
# number_2 = 5

# equal_values = number_1 == number_2

# print(f"The numbers {number_1} and {number_2} are equals: {equal_values}.")

# """
# 20. Escreva um programa que verifique se dois números
#  fornecidos pelo usuário são diferentes.
# """

# number_1 = 5
# number_2 = 2

# different_values = number_1 != number_2

# print(f"The numbers {number_1} and {number_2} "
#       f"are different: {different_values}.")

# #### try-except e if

# """
# 21. Escreva um programa que converta a temperatura
# de Celsius para Fahrenheit. O programa deve solicitar
# ao usuário a temperatura em Celsius e, utilizando try-except,
# garantir que a entrada seja numérica, tratando qualquer ValueError.
# Imprima o resultado em Fahrenheit ou uma
# mensagem de erro se a entrada não for válida.
# Fórmula
# (0 °C × 9/5) + 32 = 32 °F
# """

# try:
#     celsius = float(input("Type the temperature in Celsies degress: "))
#     fahrenheit = (celsius * 9/5) + 32

#     print(f"The temperature {celsius} degress Celsius "
#           f"is equivalent to {fahrenheit} defress Fahrenhigt.")

# except ValueError as e:
#     print(f"An error occurred: {e}.")
#     print("Please, type an correct number in Celsius degress")

# """
# 22. Crie um programa que verifica se uma palavra
# ou frase é um palíndromo
# (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações).
# Utilize try-except para garantir que a entrada seja uma string.
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.
# """

# try:
#     is_palindrome = input("Type a word or phrase: ")
#     if isinstance(is_palindrome, str):
#         is_palindrome_formated = is_palindrome.replace(" ", "").lower()
#         if is_palindrome_formated == is_palindrome_formated[::-1]:
#             print(f"the word or phrase {is_palindrome}, is a palindrome.")
#         else:
#             print(f"The word or phrase {is_palindrome}, is not a palindrome.")

# except ValueError as e:
#     print(f"An error occurred: {e}")
#     print("Please, type a correct word or phrase.")


# """
# 23. Desenvolva uma calculadora simples que aceite
# duas entradas numéricas e um operador (+, -, *, /) do usuário.
# Use try-except para lidar com divisões por zero e entradas
# não numéricas. Utilize if-elif-else para realizar a
# operação matemática baseada no operador fornecido.
# Imprima o resultado ou uma mensagem de erro apropriada.
# """

# try:
#     number_1 = float(input("Type the first number: "))
#     number_2 = float(input("Type the second number: "))
#     mathematical_operator = input("Type the operator (+, -, *, /): ")
#     result = None

#     if mathematical_operator == "+":
#         result = number_1 + number_2
#     elif mathematical_operator == "-":
#         result = number_1 - number_2
#     elif mathematical_operator == "*":
#         result = number_1 * number_2
#     elif mathematical_operator == "/" and number_2 != 0:
#         result = number_1 / number_2
#     else:
#         print("Invalid operator or division by zero.")
#     if result is not None:
#         print(f"The result of {number_1} "
#               f"{mathematical_operator} {number_2} is {result}")
# except ValueError as e:
#     print(f"Occurred an error: {e}")
#     print("Please, type an correct number.")

# """
# 24. Escreva um programa que solicite ao usuário
# para digitar um número. Utilize try-except
# para assegurar que a entrada seja numérica
# e utilize if-elif-else para classificar o número
# como "positivo", "negativo" ou "zero".
# Adicionalmente, identifique se o número é "par" ou "ímpar".
# """

# """
# Enter a string input, that will be converted as integer,
# and checked if it's a number. After that,
# the number will be classified as positive,
# negative or zero. And even or odd.
# Ther is a try-except to handle the conversion
# """

# numeric_number = input("Type a numeric integer number: ")


# try:
#     numeric_number = int(numeric_number)
#     if numeric_number == 0:
#         print(f"The number {numeric_number} is zero.")
#     elif numeric_number > 0:
#         print(f"The number {numeric_number} is positive.")
#     elif numeric_number < 0:
#         print(f"The number {numeric_number} is negative.")
#     if numeric_number % 2 == 0:
#         print(f"The number {numeric_number} is even.")
#     else:
#         print(f"The number {numeric_number} is odd.")
# except ValueError as e:
#     print(f"An error occurred: {e}")
#     print("Please, type a correct integer number.")

"""
25. Crie um script que solicite ao usuário uma lista de
números separados por vírgula. O programa deve converter
a string de entrada em uma lista de números inteiros.
Utilize try-except para tratar a conversão de cada número
e validar que cada elemento da lista convertida é um inteiro.
Se a conversão falhar ou um elemento não for um inteiro,
imprima uma mensagem de erro.
Se a conversão for bem-sucedida para todos os elementos,
imprima a lista de inteiros.
"""

"""
This code will ask the user to type a list of numbers separated by commas.
Then, it will convert the string input into a list of integers.
If the conversion is successful, it will print the list of integers.
If the conversion fails, it will print an error message.
The script is using a try-except block to handle any ValueError that may occur
This structure uses list comprehension to convert the string
input into a list of integers.
"""

numbers_list = input("Type a list of numbers separated by commas: ")

try:
    numbers_list = [int(number.strip()) for number in numbers_list.split(",")]
    if numbers_list:
        for number in numbers_list:
            if not isinstance(number, int):
                raise ValueError(f"{number} is not an integer.")
except ValueError as e:
    print(f"An error occurred: {e}")
    print("Please, type a correct list of numbers separated by commas.")
print(f"The list of numbers is: {numbers_list}")

"""
This structure uses a for loop to iterate over the list of numbers
and convert each number to an integer.
"""


entry_list = input("Enter a list of numbers separated by commas: ")
numbers_str = entry_list.split(",")
numbers_int = []
try:
    for number in numbers_str:
        numbers_int.append(int(number.strip()))
    print("The list of numbers is:", numbers_int)
except ValueError as e:
    print(f"An error occurred: {e}")
    print("Please, type a correct list of numbers separated by commas.")
