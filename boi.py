import os
os.system("cls")

boi1 = input("Nome do boi 1: ")
peso1 = float(input(f"Peso de {boi1} (kg): "))

boi2 = input("Nome do boi 2: ")
peso2 = float(input(f"Peso de {boi2} (kg): "))

boi3 = input("Nome do boi 3: ")
peso3 = float(input(f"Peso de {boi3} (kg): "))

bois = [
    (boi1, peso1),
    (boi2, peso2),
    (boi3, peso3)
]

bois = sorted(bois, key=lambda x: x[1], reverse=True)

print("\n=== Ranking (mais pesado → mais leve) ===")

print(f"1) {bois[0][0]} — {bois[0][1]:.2f} kg")
print(f"2) {bois[1][0]} — {bois[1][1]:.2f} kg")
print(f"3) {bois[2][0]} — {bois[2][1]:.2f} kg")
