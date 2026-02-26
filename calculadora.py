print("🔧 CALCULADORA DE CABOS ELÉTRICOS")
print("="*30)

potencia = float(input("Potência (Watts): "))
tensao = float(input("Tensão (Volts): "))
distancia = float(input("Distância (metros): "))

corrente = potencia / tensao
bitola = round((corrente * distancia * 2) / (56 * 0.03), 1)

print("="*30)
print(f"Corrente: {corrente:.1f} A")
print(f"Bitola: {bitola} mm²")

if bitola <= 1.5:
    print("Cabo: 1.5 mm²")
elif bitola <= 2.5:
    print("Cabo: 2.5 mm²")
elif bitola <= 4.0:
    print("Cabo: 4.0 mm²")
else:
    print("Cabo: 6.0 mm² ou mais")
