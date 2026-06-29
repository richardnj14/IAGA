n = int(input("Qual o tamanho da lista? \n"))
lista =[]
for i in range(n):
    item = int(input(f"{i+1}o. item da lista: "))
    lista.append(item)
print(f"\nA soma dos elementos da lista é: {sum(lista)}\n")

for i in lista:
        if i != lista[-1]:
            print(i,end=", ")
        else:
             print(i)
