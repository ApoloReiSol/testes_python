# Calculadora simples

numero_um = float(imput("digite o primeiro numero: "))
numero_dois = float(input("digite o segundo numero: "))

resultado = ''
if operacao == '+':
    resultado = numero_um + numero_dois
elif operacao == '-':
    resultado = numero_um - numero_dois
elif operacao == '*':
    esultado =numero_um * numero_dois
elif operacao == '/':
    if numero_dois == 0:
        print("Não é possivel dividir por zero")
    else:
        resultado = numero_um / numero_dois
else:
    prin("O0peração nãorenhecida")

if resultado != '':
    print(f"O resultado é{resultado}")