import time

from Cronometro import Cronometro

cronometro = Cronometro()

cronometro.iniciar()

time.sleep(2.647)

cronometro.parar()

print(cronometro.ultimoTiempo)