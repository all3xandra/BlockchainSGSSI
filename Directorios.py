import sys, Comprobar, Hash, os
from pathlib import Path

def directorios(f1, directory):

    files = []
    fileZero = ""

    basepath = Path(directory)

    # Se recorren todos los ficheros del directorio.
    files_in_basepath = (entry for entry in basepath.iterdir() if entry.is_file())
    n_of_files = 0

    # Se recorren los ficheros dentro del directorio.
    for item in files_in_basepath:
        n_of_files += 1
        # Se comprueba que el fichero no es el original.
        if item.name == f1:
            print("El fichero ", f1, " ya existe en el directorio ", directory)
        else:
            path = directory + "/" + item.name
            # Se comprueba que el fichero cumple los requisitos.
            if(Comprobar.comprobar(f1, path)):
                sha256 = Hash.sha256gen(path)
                # Se añaden a la lista de ficheros el nombre del fichero y el hash del mismo, bajo el modelo de un diccionario (equivalente a HashMap).
                files.append(dict(name=item.name, sha256=sha256))
                print("Fichero ", item.name, " añadido a la lista de ficheros.\n")

    # Se busca el primer fichero cuyo hash empiece por la cadena más larga de ceros.
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

    # Se devuelve un diccionario conteniendo la lista de ficheros que cumplen los requisitos
    # y el nombre del primer fichero cuyo hash empieza por la cadena más larga de ceros.
    return dict(ficheros=files, fichero_mas_ceros=fileZero)

if __name__ == '__main__':

    f1 = sys.argv[1]
    directory = sys.argv[2]

    resul = directorios(f1, directory)

    for file in resul['ficheros']:
        print("Fichero: ", file['name'], " SHA256: ", file['sha256'])

    print("Porcentaje de ficheros correctos en el directorio: ", (len(resul["ficheros"])/len(os.listdir(directory)))*100, "%")

    print("\nPrimer fichero con más ceros: ", resul['fichero_mas_ceros'])