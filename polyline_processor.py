import math
import csv

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    print("--- Procesador de Poligonales en Lote ---")
    archivo_csv = 'coordenadas.csv'
    distancia_total = 0.0
    puntos = []

    # Bloque para leer el archivo de forma segura
    try:
        with open(archivo_csv, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Saltamos la primera línea (cabecera: ID,X,Y)
            
            for fila in csv_reader:
                # fila[0] es el ID, fila[1] es X, fila[2] es Y
                puntos.append((float(fila[1]), float(fila[2])))
        
        # Recorremos la lista de puntos para sumar las distancias
        for i in range(len(puntos) - 1):
            x1, y1 = puntos[i]
            x2, y2 = puntos[i+1]
            tramo = calcular_distancia(x1, y1, x2, y2)
            distancia_total += tramo
        
        print(f"Se han procesado {len(puntos)} puntos correctamente.")
        print(f"La longitud total de la poligonal es: {distancia_total:.3f} metros.")

    except FileNotFoundError:
        print(f"Error: No se ha encontrado el archivo '{archivo_csv}'.")
        print("Por favor, crea uno en la misma carpeta con el formato ID,X,Y.")
    except ValueError:
        print("Error: Hay datos no numéricos en las coordenadas del archivo.")

if __name__ == "__main__":
    main()