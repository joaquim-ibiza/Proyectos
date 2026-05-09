import folium

print("Iniciando sistema cartográfico...")

# 1. Crear el mapa base (centrado en la Península y con estilo oscuro)
# Las coordenadas 40.0, -2.0 son más o menos el centro de España
mapa = folium.Map(location=[40.0, -2.0], zoom_start=6, tiles="CartoDB dark_matter")

# 2. Añadir Marcador: Base actual (UPV)
folium.Marker(
    location=[39.4811, -0.3409],
    popup="Base Operativa: UPV",
    tooltip="Comando Joaquim",
    icon=folium.Icon(color="green", icon="info-sign")
).add_to(mapa)

# 3. Añadir Marcador: Objetivo futuro (SatCen)
folium.Marker(
    location=[40.4856, -3.4561],
    popup="Objetivo: Centro de Satélites de la UE",
    tooltip="SatCen",
    icon=folium.Icon(color="red", icon="star")
).add_to(mapa)

# 4. Trazar la ruta de vuelo (Una línea conectando ambos puntos)
coordenadas_ruta = [
    [39.4811, -0.3409], # UPV
    [40.4856, -3.4561]  # SatCen
]
folium.PolyLine(locations=coordenadas_ruta, color="cyan", weight=3, opacity=0.8).add_to(mapa)

# 5. Exportar el mapa a una web interactiva
archivo_salida = "mapa_mision.html"
mapa.save(archivo_salida)

print(f"✅ Mapa generado con éxito. Busca el archivo '{archivo_salida}' en tu carpeta.")