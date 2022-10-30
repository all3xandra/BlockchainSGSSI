import hashlib, sys, Comprobar
from pathlib import Path

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

def directorios(f1, directory):

    files = []
    fileZero = ""

    basepath = Path(directory)
    files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
    for item in files_in_basepath:
        if item.name == f1:
            print("El fichero ", f1, " ya existe en el directorio ", directory)
        else:
            path = directory + "/" + item.name
            aprob = Comprobar.comprobar(f1, path)
            if(aprob==2):
                sha256 = sha256gen(path)
                files.append(dict(name=item.name, sha256=sha256))
                print("\nFichero ", item.name, " añadido a la lista de ficheros.\n")

    contaux = 0
    for pair in files:
        cont = 0
        i = 0
        s = pair["sha256"]

        while(i < (len(s) - 1) and s[i] == '0'):
            cont += 1
            i += 1

        if(cont > contaux):
            contaux = cont
            fileZero = pair["name"]

    print("\nEl fichero con más ceros es ", fileZero, " con ", contaux, " ceros.\n")

    return dict(ficheros=files, fichero_mas_ceros=fileZero)

if __name__ == '__main__':

    f1 = sys.argv[1]
    directory = sys.argv[2]

    resul = directorios(f1, directory)

    for file in resul['ficheros']:
        print("Fichero: ", file['name'], " SHA256: ", file['sha256'])

    print("\nFicher con más ceros: ", resul['fichero_mas_ceros'])