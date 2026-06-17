paciente = input("Nome do paciente..............: ")
pc = float(input("Peso corporal do paciente (kg): "))
alt = float(input("Altura do paciente (m)........: "))

IMC_value = pc / alt **2

if (IMC_value < 18.5):
    interpretacao = "Magreza"

if (IMC_value >= 18.5) and (IMC_value < 25.0):
    interpretacao = "Normal"

if (IMC_value >= 25) and (IMC_value < 30):
    interpretacao = "Sobrepeso"

if (IMC_value >= 30) and (IMC_value < 40):
    interpretacao = "Obesidade"

if (IMC_value >= 40):
    interpretacao = "Obesidade grave"

print(f"\nNome do paciente: {paciente} ")
print(f"IMC.............: {IMC_value:.2f} ")
print(f"{interpretacao}")