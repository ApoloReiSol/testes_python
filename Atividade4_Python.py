# - Caculo Salarial

salario = float(input("Digite seu salário:"))
tempo_servico = float(input("informe o tempo de serviço"))

if tempo_servico > 5:
    total = salario * 1.05
else:
    total = salario

if (total > salario):
    print(f"Seu novo salário é de {total}")
else:
    print(f"Seu salário permanece o mesmo")