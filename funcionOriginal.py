from scipy.fft import fft, ifft, fftfreq
import numpy as np
import matplotlib.pyplot as plt

archivo = open('calamar_pda.txt')
tiempos = []
potenciales = []

# Lectura de archivo
contadorDeLineas = 0
for estaLinea in archivo:
    if contadorDeLineas == 1:
        tiempos = estaLinea.split(",")
    elif contadorDeLineas == 3:
        potenciales = estaLinea.split(",")
    contadorDeLineas += 1
tiempos[-1] = tiempos[-1].replace('\n', '')
potenciales[-1] = potenciales[-1].replace('\n', '')

N = len(potenciales)

x_f = [float(esteNumero) for esteNumero in tiempos]
y_f = [float(esteNumero) for esteNumero in potenciales]

print(len(y_f))
print(len(x_f))

plt.plot(x_f, y_f)

plt.xlabel("tiempo [ms]")
plt.ylabel("potenciales [mV]")

plt.show()
