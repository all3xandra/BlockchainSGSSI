import sys, Hash, re

def comprobar(file1, file2):

    print("Se comparan los ficheros ", file1, " y ", file2, "...\n")

    f1 = open(file1, 'r')
    f2 = open(file2, 'r')

    t1 = f1.readlines()
    t2 = f2.readlines()

    # Se comprueba que la última línea cumple con las características especificadas
    # para las actividades anteriores
    last_line = re.match("[a-f0-9]{8} G([0-9a-f]{3})+", t2[-1])

    # No se comprueba la última linea porque contiene el código randomizado. Se trata de comprobar que el resto de líneas son iguales.
    t2 = t2[0:len(t2)-1]

    sha = Hash.sha256gen(file2)

    cont = 0

    # Se cuenta el número de ceros que hay al principio del hash.
    while(cont < (len(sha) - 1) and sha[cont] == '0'):
        cont = cont + 1

    aprob = True

    if(t1 != t2):
        aprob = False
        print("Contenido distinto.\n")
    if(cont < 3):
        aprob = False
        print("Segundo fichero con hash incorrecto.\n")
    if(not bool(last_line)):
        aprob = False
        print("Segundo fichero con código randomizado incorrecto.\n")

    if(aprob):
        print("El fichero ", file2, " cumple los requisitos.\n")

    f1.close()
    f2.close()

    # Si se cumplen los dos requisitos, se devuelve True.
    return aprob

if __name__ == '__main__':
    f1 = sys.argv[1]
    f2 = sys.argv[2]

    print("¡CORRECTO!") if comprobar(f1, f2) else print("¡INCORRECTO!")