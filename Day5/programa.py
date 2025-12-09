import sys
from pathlib import Path

# programa.py
# Lee y muestra el contenido del fichero "ayuda.txt"

def leer_fichero(path: Path) -> str:
    
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"Error: fichero no encontrado: {path}")
    except UnicodeDecodeError:
        raise SystemExit(f"Error: no se pudo decodificar el fichero: {path}")
    except Exception as e:
        raise SystemExit(f"Error leyendo el fichero: {e}")

def main():
    # ruta por defecto: mismo directorio del script
    ruta = Path(__file__).parent / "ayuda.txt"
    # si se pasa un argumento, usarlo como ruta
    if len(sys.argv) > 1:
        ruta = Path(sys.argv[1])
    contenido = leer_fichero(ruta)

    intervalos: list[tuple[int, int]] = []

    for linea in contenido.splitlines():
        if not linea.strip():
            break  # al primer espacio/línea vacía dejamos de leer rangos

        try:
            num1_str, num2_str = linea.split("-")
            num1 = int(num1_str.strip())
            num2 = int(num2_str.strip())
        except ValueError:
            raise SystemExit(
                f"Formato inesperado, se esperaba 'num1 - num2' y se recibió: {linea!r}"
            )

        intervalos.append((num1, num2))

    if not intervalos:
        print(0)
        return

    # Unir rangos para no contar IDs solapados dos veces
    intervalos.sort(key=lambda par: par[0])
    union = []
    actual_ini, actual_fin = intervalos[0]

    for ini, fin in intervalos[1:]:
        if ini <= actual_fin + 1:  # solapa o es contiguo
            actual_fin = max(actual_fin, fin)
        else:
            union.append((actual_ini, actual_fin))
            actual_ini, actual_fin = ini, fin

    union.append((actual_ini, actual_fin))

    ids_validos = sum(fin - ini + 1 for ini, fin in union)
    print(ids_validos)

if __name__ == "__main__":
    main()