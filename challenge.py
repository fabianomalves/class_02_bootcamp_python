"""Desafio - Refatorar o projeto da aula anterior,
evitando Bugs!"""

BONUS = 1000

""" 1) Solicita ao usuário que digite seu nome"""

try:
    name_user = str(input("Type your name: "))

    if len(name_user) == 0:
        raise ValueError("The name cannot be empty.")
        exit()
    elif any(char.isdigit() for char in name_user):
        raise ValueError("The name cannot contain numbers.")
        exit()
    else:
        print("The name is valid: ", name_user)
except ValueError as e:
    print(e)
    exit()

""" 2) Solicita ao usuário que digite o valor do seu salário
 e converte para float"""

salary_value = input("Type your salary: ")

if "," in salary_value:
    salary_value = salary_value.replace(",", ".")
try:
    salary_value = float(salary_value)
    if salary_value < 0:
        print("Inform a positive salary number: ")
    else:
        print("The salary is valid: ", salary_value)
except ValueError as e:
    print(
        f"""Invalid information for salary {e}.
        Inform a number."""
    )
    exit()


""" 3) Solicita ao usuário que digite o valor do bônus
recebido e converte para float"""

bonus_percentage = input("Informe your bonus percentage: ")

if "," in bonus_percentage:
    bonus_percentage = bonus_percentage.replace(",", ".")

try:
    bonus_percentage = float(bonus_percentage)
    if bonus_percentage < 0:
        print("Inform a positive number: ")
    else:
        print("Your bonus is valid: ", bonus_percentage)
except ValueError as e:
    print(f"Invalid information for the bonus {e}. Inform a number.")
    exit()

# 4) Calculate the final value bonus

final_bonus_salary = BONUS + (salary_value * bonus_percentage)

print(
    f"""The user {name_user}, have a final salary with
      bonus value: {final_bonus_salary}."""
)
