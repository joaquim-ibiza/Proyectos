import math

def calcular_problema_inverso(x1, y1, x2, y2):
    # Cálculo de incrementos
    delta_x = x2 - x1
    delta_y = y2 - y1

    # Cálculo de la distancia plana (Pitágoras)
    distancia = math.sqrt(delta_x**2 + delta_y**2)

    # Cálculo del azimut en radianes usando atan2 para gestionar los cuadrantes
    azimut_rad = math.atan2(delta_x, delta_y)

    # Conversión a grados centesimales (gons)
    azimut_gon = azimut_rad * (200 / math.pi)

    # Ajuste para que el azimut sea siempre positivo (entre 0 y 400 gons)
    if azimut_gon < 0:
        azimut_gon += 400

    return distancia, azimut_gon

def main():
    print("--- Calculadora del Problema Inverso Topográfico ---")
    try:
        x1 = float(input("Coordenada X del Estacionamiento (Punto 1): "))
        y1 = float(input("Coordenada Y del Estacionamiento (Punto 1): "))
        x2 = float(input("Coordenada X del Punto Visado (Punto 2): "))
        y2 = float(input("Coordenada Y del Punto Visado (Punto 2): "))

        dist, azimut = calcular_problema_inverso(x1, y1, x2, y2)
        
        print(f"\n--- Resultados ---")
        print(f"Distancia plana: {dist:.3f} metros")
        print(f"Azimut: {azimut:.4f} gons")
    except ValueError:
        print("Error: Por favor, introduce valores numéricos.")

if __name__ == "__main__":
    main()