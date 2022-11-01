a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
menor = a
if b < c and b < a:
    menor = b
if c < b and c < a:
    menor = c
print(f"menor {menor}, maior {maior}")
