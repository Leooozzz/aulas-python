valor_prd=float(input('Digite o valor do produto:'))
descont=float(input('Digite o valor do desconto: '))
desconto=(valor_prd*descont)/100
print(f'O produto de  R${valor_prd} com {descont}% ficou R${valor_prd-desconto}')