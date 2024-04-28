import hashlib

# Nombre del archivo que deseas encriptar
nombre_archivo = input("Ingresa el nombre del archivo: ")

# Abre el archivo en modo lectura de bytes (rb)
with open(nombre_archivo, "rb") as archivo:
    contenido_bytes = archivo.read()

# Calcula el hash MD5
hash_md5_archivo = hashlib.md5(contenido_bytes)

# Imprime el valor hexadecimal del hash
print("El equivalente hexadecimal del hash del archivo es:", hash_md5_archivo.hexdigest())
