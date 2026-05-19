# Calculadora simples em Python

print("=== CALCULADORA ===")

# Entrada de dados
num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /,**,%): ")
num2 = float(input("Digite o segundo número: "))

# Verificação da operação
if operacao == "+":
    resultado = num1 + num2

elif operacao == "-":
    resultado = num1 - num2

elif operacao == "*":
    resultado = num1 * num2

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"

elif operacao == "**":
    resultado = num1 ** num2

elif operacao == "%":
    resultado = num1 % num2

else:
    resultado = "Operação inválida"

# Saída
print("Resultado:", resultado)