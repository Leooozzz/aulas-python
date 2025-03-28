listacompra = []
for c in range(3):
    c = input('Digite a sua lista: ')
    listacompra.append(c)
print(listacompra)
print("""Escolha oque voce quer da lista: 
[1]Altere o valor da lista
[2]adicionar elementos
[3]remover elemento
""")
escolha=int(input('Escolha o numero: '))
if escolha ==1:
    oqdesejaalt=str(input('digite oq voce deseja alterar: '))
    posiçao=int(input('Digite a posiçao: '))
    listacompra[posiçao]=oqdesejaalt
    print(listacompra)
elif escolha ==2:
    addelemento=str(input('Oque voce quer adicionar: '))
    listacompra.append(addelemento)
    print(listacompra)
else:
    remove=str(input('Oque voce quer remover: '))
    listacompra.remove(remove)
    print(listacompra)