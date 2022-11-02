import hashlib, secrets, sys
def sha256gen(filename):

    b = False

    while (not b):

        try:
            sha256_hash = hashlib.sha256()
            with open(filename,"rb") as f:
                for byte_block in iter(lambda: f.read(4096),b""):
                    sha256_hash.update(byte_block)
                sha256 = sha256_hash.hexdigest()
            b = True
        except:
            print("Error. Comprueba la ruta del fichero.")
            filename = input("Inserta el nombre del fichero: ")
           
    return sha256

def rdn_hex_gen():

    return secrets.token_hex(4) + " G26"

def comprobar(file1, file2):

    print("Se comparan los ficheros ", file1, " y ", file2, "...\n")

    # Se define una variable que indica cuántos requisitos cumple el fichero
    aprob = 0

    f1 = open(file1, 'r')
    f2 = open(file2, 'r')

    t1 = f1.readlines()
    t2 = f2.readlines()
    # No se comprueba la última linea porque contiene el código randomizado. Se trata de comprobar que el resto de líneas son iguales.
    t2 = t2[0:len(t2)-1]
    
    print("Comprobando ficheros...")
    if t1 == t2:
        aprob += 1
        print("Contenido igual.")
    else:
        print("Contenido distinto.")
    
    sha = sha256gen(file2)

    cont = 0
    i = 0

    # Se cuenta el número de ceros que hay al principio del hash.
    while(i < (len(sha) - 1) and sha[i] == '0'):
        cont = cont + 1
        i = i + 1

    # Se comprueba que hay al menos 3 ceros.
    print("\nComprobando ficheros...")
    if(cont >= 3):
        aprob += 1
        print("Segundo fichero con hash correcto.")
    else:
        print("Segundo fichero con hash incorrecto.")

    f1.close()
    f2.close()

    # Si se cumplen los dos requisitos, se devuelve True.
    return aprob==2

if __name__ == '__main__':
    f1 = sys.argv[1]
    f2 = sys.argv[2]

    aprob = comprobar(f1, f2)

    if(aprob == 2):
        print("\n¡CORRECTO!")
    else:
        print("\n¡INCORRECTO!")