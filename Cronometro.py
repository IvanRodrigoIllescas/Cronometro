import time


class Cronometro:

    tiempoInicial = 0
    tiempoFinal = 0

    ultimoTiempo = 0


    def __init__(self):
        pass

    def iniciar(self):
        self.tiempoInicial = time.time()

    def parar(self):
        self.tiempoFinal = time.time()
        tiempoPasado = self.tiempoFinal - self.tiempoInicial

        self.ultimoTiempo = round(tiempoPasado, 2)

    def getTiempo(self):
        return self.ultimoTiempo