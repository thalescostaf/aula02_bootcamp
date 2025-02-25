CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
try:
    nome_usuario = input("Digite o seu nome: ")
except TypeError:
    print("O nome está errado")
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario_usuario = float(input("Digite o seu salario: "))
except ValueError:
    print("O valor está errado! Insira um número.")
except KeyboardInterrupt:
    print("O programa foi interrompido!")


# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

try:
    bonus_usuario = float(input("Digite o valor do seu Bonus: "))
except ValueError:
    print("O Bonus precisa ser numérico")
except KeyboardInterrupt:
    print("O programa foi interrompido!")

# 4) Calcule o valor do bônus final
if salario_usuario > 0 and bonus_usuario >= 0:
    kpi = CONSTANTE_BONUS + salario_usuario * bonus_usuario
    print(f"O valor do seu salario com bonus e taxa final é: ", kpi)
else:
    print("O Salario ou Bonus está errado")

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus
print(f"O usuario {nome_usuario} possui o bonus de {kpi}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
# O usuário deixar o nome ou algum outro campo em branco
# O usuário colocar letra com número, ou símbolo de moeda R$