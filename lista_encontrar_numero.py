lista = [10,2,7,8,5,3,22,17,18]

item = int(input())
number_found = False

#Print list with the expected format
for i, l in enumerate(lista):
    if i == 0:
        print("{", end ="")
        print(f"{i}:{l}, ",end = "")
    elif i!= (len(lista)-1):
        print(f"{i}:{l}, ", end = "")
    else:
        print(f"{i}:{l}", end = "}\n\n")

    if l == item:
        number_found = True
        found_on_position = i

if number_found:
    print(f"Item: {item}, foi encontrado na posicao {found_on_position}.")
else:
    print(f'Item: {item}, "nao" foi encontrado.') 