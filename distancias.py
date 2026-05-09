import math

def calcular_distancia(lat1, lon1, lat2, lon2):
    """Calcula la distancia en kilómetros entre dos puntos de la Tierra."""
    # Radio aproximado de la Tierra en km
    R = 6371.0
    
    # Convertimos los grados a radianes (Matemáticas de la uni)
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # Diferencias
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    
    # Fórmula de Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distancia = R * c
    return distancia

print("🌍 SISTEMA DE CÁLCULO GEODÉSICO - INICIADO")
print("------------------------------------------")

# Coordenadas: UPV (Valencia) -> SatCen (Torrejón de Ardoz, Madrid)
dist = calcular_distancia(39.4811, -0.3409, 40.4856, -3.4561)

print(f"📍 Distancia desde la UPV hasta el Centro de Satélites de la UE: {dist:.2f} km")