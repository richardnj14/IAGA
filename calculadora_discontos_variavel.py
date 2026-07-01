total = float(input())

if total < 5000:
    discount_rate = 0.1
else:
    discount_rate = 0.15

print(f"Valor do Produto        = R$ {total:.2f}")
print(f"Valor do Desconto ({discount_rate*100:.0f}%) = R$ {total*discount_rate:.2f}")
print(f"Valor Final             = R$ {total*(1-discount_rate):.2f}")