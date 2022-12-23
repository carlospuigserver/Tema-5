import sys

fichero=open("contador.txt", "r")
fichero.seek(0)
contenido=fichero.readline()
if len(contenido)==0:
    contenido=0

fichero.write(contenido)
fichero.close()

try:
    contenido=int(contenido)
    if len(sys.argv)==2:
        if sys.argv[1]=="suma":
            contenido+=1
        elif sys.argv[1]=="resta":
            contenido-=1
    print(contenido)
    fichero=open("contador.txt", "w")
    fichero.write(str(contenido))
    fichero.close()
except:
    print("Error: Tipo de dato no valido")