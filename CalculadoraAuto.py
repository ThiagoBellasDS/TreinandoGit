## Projeto Calculadora Automática - DSA

# Mostrar a mensagem: 'Python Calculator'
import soma as soma

print('\n********** Python Calculator ************')
print("\n")

# Mostrar opções de operações para o utilizador
print('Selecione o número da operação desejada:')
print('\n')
opcoes = ('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
print(opcoes)
print('\n')

# Solicitar a opção desejada
op_desejada = float(input('Digite sua opção: '))

# Solicitar o primeiro número
num1 = float(input('Digite o primeiro número '))

# Solicitar o segundo número
num2 = float(input('Digite o segundo número '))

if op_desejada == 1:
    soma = num1 + num2
    print('O resultado da operação é: ' + str(soma))
elif op_desejada == 2:
    subtração = num1 - num2
    print('O resultado da operação é: ' + str(subtração))
elif op_desejada == 3:
    multiplicação = num1 * num2
    print('O resultado da operação é: ' + str(multiplicação))
elif op_desejada == 2:
    divisao = num1 / num2
    print('O resultado da operação é: ' + str(divisao))