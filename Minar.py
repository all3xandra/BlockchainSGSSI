import hashlib, os, secrets
from time import time

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

    return secrets.token_hex(4) + " G3ce"

if __name__ == '__main__':

    f = input("Inserta el nombre del fichero: ")
    s = ""

    out_dir = f
    out_dir = out_dir.replace(".txt", ".3ce.txt")

    print("El fichero de salida será ", out_dir)

    with open(f, 'r') as fp:
        txt = fp.read()

    fin = time() + 60

    taux = ""
    contaux = 0
    intentos = 0

    while(time() < fin):

        intentos = intentos + 1
        t = rdn_hex_gen()

        with open("temp.txt", 'w') as fp:
            fp.write(txt)
            fp.write(t)

        s = sha256gen("temp.txt")

        cont = 0
        i = 0

        while(i < (len(s) - 1) and s[i] == '0'):
            cont = cont + 1
            i = i + 1
        
        if(cont > contaux):
            contaux = cont
            taux = t
            print("Nuevo record: " + str(contaux) + ", intentos: " + str(intentos))

    os.remove("temp.txt")

    with open(out_dir, 'w') as fp:
        fp.write(txt)
        fp.write(taux)

    shaf1 = sha256gen(out_dir)
    print("\nIntentos totales: " + str(intentos))
    print("Hexadecimal generado: " + str(taux))
    print("SHA256 generado: " + shaf1)

    print("Program ended succesfully.")