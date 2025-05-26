# Atividade Prática 01

## 1. Programa de Saudação

print("Hello, world!")


## 2. Calculadora de Soma
 
numero1 = 12
numero2 = 14
soma = numero1 + numero2
print("A soma é:", soma)
 

## 3. Calculadora de Volume
 
comprimento = 12
largura = 14
altura = 20
volume = comprimento * largura * altura
print("O volume da caixa é:", volume, "cm³")
 

## 4. Calculadora de Preço Total
 
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3
preco_total = preco_unitario * quantidade

print("Produto:", nome_produto)
print("Preço unitário: R$", preco_unitario)
print("Quantidade:", quantidade)
print("Preço total: R$", preco_total)
 

## 5. Diferença de Produtos
 
A = int(input())
B = int(input())
C = int(input())
D = int(input())

DIFERENCA = (A * B - C * D)
print("DIFERENCA =", DIFERENCA)
 

# Atividade Prática 02

## 1. Conversor de Moeda
 
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print("R$", valor_reais, "equivale a:")
print("US$", round(valor_dolar, 2))
print("€", round(valor_euro, 2))
 

## 2. Calculadora de Desconto
 
nome_produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

print("Produto:", nome_produto)
print("Preço original: R$", preco_original)
print("Desconto:", desconto_percentual, "%")
print("Valor do desconto: R$", valor_desconto)
print("Preço final: R$", preco_final)
 

## 3. Calculadora de Média Escolar
 
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print("Notas do aluno:")
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Média final:", round(media, 2))
 

## 4. Calculadora de Consumo de Combustível
 
distancia = 300
combustivel = 25

consumo_medio = distancia / combustivel

print("Distância percorrida:", distancia, "km")
print("Combustível gasto:", combustivel, "litros")
print("Consumo médio:", round(consumo_medio, 2), "km/l")
 

## 5. Calculadora de Soma com Entrada do Usuário
 
A = int(input())
B = int(input())

X = A + B

print("X =", X)
 

## 6. Calculadora de Salário por Horas Trabalhadas
 
numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

salario = horas_trabalhadas * valor_por_hora

print("NUMBER =", numero_funcionario)
print("SALARY = R$", format(salario, ".2f"))

# Atividade Prática 03
# 1 - Área da Circunferência
raio = float(input())
PI = 3.14159265
area = PI * (raio ** 2)
print(f"A={area:.4f}")

# 2 - Classificador de Idade
idade = int(input("Digite a idade: "))
if 0 <= idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")

# 3 - Calculadora de IMC
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))
imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f}")
if imc < 18.5:
    print("Classificacao: Abaixo do peso")
elif imc < 25:
    print("Classificacao: Peso normal")
elif imc < 30:
    print("Classificacao: Sobrepeso")
else:
    print("Classificacao: Obeso")

# 4 - Conversor de Temperatura
temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C/F/K): ").upper()
destino = input("Digite a unidade de destino (C/F/K): ").upper()
resultado = temp
if origem == 'C':
    if destino == 'F':
        resultado = (temp * 9/5) + 32
    elif destino == 'K':
        resultado = temp + 273.15
elif origem == 'F':
    if destino == 'C':
        resultado = (temp - 32) * 5/9
    elif destino == 'K':
        resultado = (temp - 32) * 5/9 + 273.15
elif origem == 'K':
    if destino == 'C':
        resultado = temp - 273.15
    elif destino == 'F':
        resultado = (temp - 273.15) * 9/5 + 32
else:
    print("Unidade de origem inválida")
    exit()
print(f"Temperatura convertida: {resultado:.2f}")

# 5 - Verificador de Ano Bissexto
ano = int(input("Digite o ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano bissexto")
else:
    print("Nao eh ano bissexto")

# 6 - Calculadora de Comissão
nome = input()
salario_fixo = float(input())
total_vendas = float(input())
total_receber = salario_fixo + (total_vendas * 0.15)
print(f"TOTAL = R$ {total_receber:.2f}")

# 7 - Calculadora da Média
N1, N2, N3, N4 = map(float, input().split())
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10
print(f"Media: {media:.1f}")
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    media_final = (media + exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")




 
