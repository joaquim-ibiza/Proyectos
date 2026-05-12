def dms_a_dd(grados, minutos, segundos, direccion):
    dd = float(grados) + float(minutos)/60 + float(segundos)/3600
    if direccion.upper() in ['S', 'W', 'O']:
        dd *= -1
    return dd

def dd_a_dms(decimal):
    direccion = "N" if decimal >= 0 else "S" # Simplificado para latitud
    decimal = abs(decimal)
    grados = int(decimal)
    minutos_full = (decimal - grados) * 60
    minutos = int(minutos_full)
    segundos = (minutos_full - minutos) * 60
    return grados, minutos, segundos

def main():
    print("--- Conversor de Coordenadas Geográficas ---")
    opcion = input("¿Qué quieres hacer? (1: GMS a Decimal | 2: Decimal a GMS): ")

    if opcion == "1":
        g = input("Grados: ")
        m = input("Minutos: ")
        s = input("Segundos: ")
        d = input("Dirección (N, S, E, W): ")
        print(f"Resultado en Decimal: {dms_a_dd(g, m, s, d):.6f}")
    
    elif opcion == "2":
        dec = float(input("Introduce el valor decimal: "))
        g, m, s = dd_a_dms(dec)
        print(f"Resultado: {g}° {m}' {s:.2f}\"")

if __name__ == "__main__":
    main()