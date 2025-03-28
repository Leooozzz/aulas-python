peso = float(input("Digite seu peso : "))
altura = float(input("Digite sua altura : "))
imc = peso / (altura ** 2)
print(f"Seu imc é: {imc}")
if 18.5 <= imc <= 24.9:
    print("imc normal.")
else:
    print("imc fora da faixa normal.")