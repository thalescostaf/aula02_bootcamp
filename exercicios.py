TAXA_FIXA = 1000

# Inserindo o salário
try:
    salario = float(input("Digite o seu salario em numero: "))
except ValueError:
    print("O valor está errado! Insira um número.")
except KeyboardInterrupt:
    print("O programa foi interrompido!")

# Calculando o bonus

try:
    bonus = float(input("Digite o valor do seu Bonus: "))
except ValueError:
    print("O Bonus precisa ser numérico")
except KeyboardInterrupt:
    print("O programa foi interrompido!")


# Calculando o KPI
# Taxa Fixa + Salario * Bonus

if salario > 0 and bonus >= 0:
    kpi = TAXA_FIXA + salario * bonus
    print(f"O valor do seu salario com bonus e taxa final é: ", kpi)
else:
    print("O Salario ou Bonus está errado")

