def calcular_escala():
    print("--- Calculadora de Escalas Cartográficas ---")
    print("¿Qué deseas calcular? (E: Denominador, d: Mapa, D: Real)")
    opcion = input("Opción: ").upper()

    if opcion == 'E':
        d = float(input("Distancia en el mapa (cm): "))
        D_km = float(input("Distancia real (km): "))
        D_cm = D_km * 100000
        E = D_cm / d
        print(f"La escala es 1:{int(E)}")

    elif opcion == 'D':
        d = float(input("Distancia en el mapa (cm): "))
        E = float(input("Denominador de la escala (ej. 50000): "))
        dist_real_cm = d * E
        print(f"Distancia real: {dist_real_cm / 100} m o {dist_real_cm / 100000} km")

    elif opcion == 'd':
        D_km = float(input("Distancia real (km): "))
        E = float(input("Denominador de la escala: "))
        dist_mapa_cm = (D_km * 100000) / E
        print(f"Distancia en el mapa: {dist_mapa_cm:.2f} cm")

if __name__ == "__main__":
    calcular_escala()