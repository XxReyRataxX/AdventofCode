from pathlib import Path

def main():
    # Usar ruta relativa al archivo del script, no al directorio de ejecucion
    ruta = Path(__file__).parent / "ayuda.txt"
    if not ruta.exists():
        print(f"No se encuentra {ruta}")
        return

    contenido = ruta.read_text(encoding="utf-8").strip()
    
    # Separar por comas para obtener cada elemento "num1-num2"
    items = contenido.split(',')
    
    lista_rangos = []
    total_sum = 0
    
    for item in items:
        item = item.strip()
        if not item:
            continue
            
        # Separar por guion para obtener inicio y fin
        partes = item.split('-')
        if len(partes) == 2:
            try:
                inicio = int(partes[0])
                fin = int(partes[1])
                lista_rangos.append((inicio, fin))

                # range(a, b) no incluye b, asi que usamos fin + 1 para incluirlo
                for aux in range(inicio, fin + 1):
                    s_num = str(aux)
                    length = len(s_num)
                    
                    found = False
                    # Probamos patrones de longitud 1 hasta la mitad de la longitud del numero
                    for sub_len in range(1, (length // 2) + 1):
                        if length % sub_len == 0:
                            substring = s_num[:sub_len]
                            repetitions = length // sub_len
                            if substring * repetitions == s_num:
                                found = True
                                break
                    
                    if found:
                        total_sum += aux



            except ValueError:
                print(f"Error parseando: {item}")
    
    print(f"Se han cargado {len(lista_rangos)} rangos.")
    print(f"Suma total de IDs invalidos: {total_sum}")

if __name__ == "__main__":
    main()
