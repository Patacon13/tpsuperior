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

potencialesArray = np.array(potenciales)

print(potencialesArray[0] + potencialesArray[1])

N = len(potenciales)
T = 1.0 / (0.0001 * 2)

x_f = np.linspace(0.0, T, N//2)
print(len(x_f))
y_f = fft(potencialesArray)

plt.plot(x_f, np.abs(y_f[:N//2]))
plt.show()

#print(fftfreq(N, T))
