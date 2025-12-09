import sys
from pathlib import Path

# programa.py
# Lee y muestra el contenido del fichero "ayuda.txt"

def leer_fichero(path: Path) -> str:
    dial = 0
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
    ruta = Path("ayuda.txt")
    # si se pasa un argumento, usarlo como ruta
    if len(sys.argv) > 1:
        ruta = Path(sys.argv[1])
    contenido = leer_fichero(ruta)
    
    # El dial empieza en 50
    dial = 50
    password_count = 0
    
    # Procesar el contenido linea por linea
    instrucciones = contenido.splitlines()
    
    for instruccion in instrucciones:
        instruccion = instruccion.strip()
        if not instruccion:
            continue
            
        direction = instruccion[0]
        try:
            valor = int(instruccion[1:])
        except ValueError:
            print(f"No se pudo interpretar el valor en: {instruccion}")
            continue

        if direction == 'R':
            start_val = dial
            end_val = dial + valor
            # Contamos cuantos multiplos de 100 hay en el rango (start_val, end_val]
            count = (end_val // 100) - (start_val // 100)
            password_count += count
            dial = end_val % 100
            
        elif direction == 'L':
            start_val = dial
            end_val = dial - valor
            # Contamos cuantos multiplos de 100 hay en el rango [end_val, start_val)
            count = ((start_val - 1) // 100) - ((end_val - 1) // 100)
            password_count += count
            dial = end_val % 100
            

         
                
    print(f"Password: {password_count}")


if __name__ == "__main__":
    main()