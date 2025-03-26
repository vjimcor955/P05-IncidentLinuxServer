import os
import hashlib

def calculateHash(file, algorithm='SHA256'):     # Algoritmo de los hashes
    try:
        hash_func = getattr(hashlib, algorithm.lower())()
        with open(file, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                hash_func.update(byte_block)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"Error: El archivo '{file}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al calcular el hash del archivo '{file}': {e}")
        return None

def readHashFile(hashFile):
    providedHashList = {}
    try:
        with open(hashFile, 'r') as f:
            for linea in f:
                try:
                    hash_value, nombre = linea.strip().split(' ', maxsplit=1)
                    providedHashList[nombre.strip()] = hash_value.strip()
                except ValueError:
                    print(f"Error: Formato incorrecto en la línea '{linea.strip()}'.")
    except FileNotFoundError:
        print(f"Error: El archivo de hashes '{hashFile}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo de hashes: {e}")
        return None
    return providedHashList

def compareHashes(hashFile, evidencesDir='.'):
    providedHashList = readHashFile(hashFile)
    if providedHashList is None:
        return

    print("\nComprobación de archivos y hashes:")
    for nombre, providedHash in providedHashList.items():
        route = os.path.join(evidencesDir, nombre)
        file = os.path.basename(route)

        print(f"\n\n- Archivo: {file}")
        if not os.path.exists(route):
            print(f"  Resultado: El archivo no existe.")
            continue

        calculatedHash = calculateHash(route)
        if calculatedHash is None:
            continue

        print(f"\n  · Hash proporcionado:  {providedHash}")
        print(f"  · Hash calculado:      {calculatedHash}")
        if calculatedHash == providedHash:
            print(f"\n  Resultado: COINCIDEN.")
        else:
            print(f"\n  Resultado: NO COINCIDEN.")

hashFile = 'hashes_sha256.txt'                                                        # Archivo que contiene los hashes que se proporcionan
evidencesDir = 'D:\\Asignaturas\\Forense\\Unidad_5\\P05-LinuxForensics\\Evidencias'  # Directorio donde se encuentran las evidencias
compareHashes(hashFile, evidencesDir)