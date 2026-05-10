import folium
import requests

print("🛰️ Conectando con la Red del Espacio...")

# 1. Obtener la ubicación de la ISS en tiempo real desde una API pública
url = "http://api.open-notify.org/iss-now.json"
respuesta = requests.get(url)
datos = respuesta.json()

lat = float(datos['iss_position']['latitude'])
lon = float(datos['iss_position']['longitude'])

print(f"📍 Posición actual de la ISS detectada: Lat {lat}, Lon {lon}")

# 2. Crear el mapa centrado en la ISS
# Usamos un estilo de mapa diferente para que parezca un monitor de control
mapa_iss = folium.Map(location=[lat, lon], zoom_start=4, tiles="CartoDB positron")

# 3. Añadir un marcador especial para la ISS
folium.Marker(
    location=[lat, lon],
    popup="Estación Espacial Internacional",
    icon=folium.Icon(color="purple", icon="cloud", icon_color="white")
).add_to(mapa_iss)

# 4. Guardar el mapa
mapa_iss.save("donde_esta_la_iss.html")

print("✅ Mapa de órbita generado. Abre 'donde_esta_la_iss.html' para ver dónde sobrevuela ahora mismo.")