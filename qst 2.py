listanum = []
maior = 0
menor = 0
for c in range (0, 10):
    listanum.append(int(input(f"Digite um valor para a posição {c}: ")))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]


print(f"digitastes {listanum}")
print(f"o menor foi {menor} position ", end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f"{i}", end='')
print(f"o maior foi {maior} position ", end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f"{i}", end='')

print("média: {}".format(sum(listanum)/10))
