import math

def calcular_haversine(lat1, lon1, lat2, lon2):
    # Radio de la Tierra en kilómetros
    R = 6371.0

    # Convertir grados decimales a radianes
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Aplicación de la fórmula del Haversine
    a = math.sin(delta_phi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2)**2
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distancia = R * c
    return distancia

def main():
    print("--- Calculadora de Distancia Geodésica ---")
    try:
        l1 = float(input("Introduce latitud punto 1: "))
        n1 = float(input("Introduce longitud punto 1: "))
        l2 = float(input("Introduce latitud punto 2: "))
        n2 = float(input("Introduce longitud punto 2: "))

        resultado = calcular_haversine(l1, n1, l2, n2)
        
        print(f"\nLa distancia entre los puntos es de: {resultado:.2f} km")
    except ValueError:
        print("Error: Por favor, introduce números válidos.")

if __name__ == "__main__":
    main()