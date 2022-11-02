import hashlib

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