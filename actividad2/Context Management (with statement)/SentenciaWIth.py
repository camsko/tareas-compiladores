if __name__ == "__main__":
    print("Escribiendo en archivo:")
    with open("archivo.txt", "w") as f:
        f.write("Hola Keylor y Henoc\n")

    print("Leyendo archivo:")
    with open("archivo.txt", "r") as f:
        for linea in f:
            print(linea.strip())