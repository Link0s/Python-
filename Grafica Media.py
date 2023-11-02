import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu, sigma = 20000, 5102

# Crear una serie de datos desde 0 hasta 40,000 para representar la demanda de unidades
x = np.linspace(0, 40000, 100)

# Crear la distribución normal con la media y desviación estándar calculada
y = norm.pdf(x, mu, sigma)

# Crear el gráfico
plt.plot(x, y)

# Añadir línea vertical para la media
plt.axvline(x=mu, color='r', linestyle='--')

# Añadir etiquetas y título
plt.xlabel('Demanda de unidades de Barby Golpista')
plt.ylabel('Probabilidad')
plt.title('Distribución de Probabilidad Normal de la Demanda de Barby Golpista')
plt.grid()

# Mostrar el gráfico
plt.show()

