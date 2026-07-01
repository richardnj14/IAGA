discount_rate = 0.1

total = float(input())

print(f"Valor do Produto  = R$ {total:.2f}")
print(f"Valor do Desconto = R$ {total*discount_rate:.2f}")
print(f"Valor Final       = R$ {total*(1-discount_rate):.2f}")