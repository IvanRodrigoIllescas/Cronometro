# Cronometro
Cronometro para medir tiempos dentro del codigo

1º Lo importamos donde lo vallamos a usar
```python
from Cronometro import Cronometro
```
2º Creamos unn objeto de la clase Cronometro
```
cronometro = Cronometro()
```
3º Lo iniciamos
```
cronometro.iniciar()
```
4º Hacemos lo que tengamos que hacer
```
time.sleep(2.647)
```
5º Lo paramos
```
cronometro.parar()
```
6º Accedemos al ultimo tiempo que ha guardado
```
print(cronometro.ultimoTiempo)
```
Cuando lo paramos también nos devuelve el tiempo
```
tiempo = cronometro.parar()
```
