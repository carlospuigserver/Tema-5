#desarrollar un reloj de horas, minutos y segundos utilizando el módulo datetime con la hora actual? Hazlo en un script llamado reloj.py y ejecútalo en la terminal

from datetime import datetime
from time import sleep

def reloj():
    while True:
        now = datetime.now()
        print(now.strftime("%H:%M:%S"))
        sleep(1)

reloj()

