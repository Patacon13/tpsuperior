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

# Calculo de funcion con a

a = int(input('Ingrese el valor de A: '))

funcionEscalon = []


for i in range (0, 1000):
    if i < a or i > 1000 - a:
        funcionEscalon.append(1/(2*a))
    else:
        funcionEscalon.append(0)

funcionConvolucionada = np.convolve(y_f, funcionEscalon)

print(len(funcionConvolucionada))

x_escalon = []

for i in range (0, 1000):
    x_escalon.append(i)

    
plt.plot(x_escalon, funcionEscalon)

#plt.plot(x_f, funcionConvolucionada[999:])

plt.show()
