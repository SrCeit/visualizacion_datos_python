import matplotlib.pyplot as plt

'''
Creamos una lista con los datos. La función subplots() genera una o varios trazados en una figura. La variable fig representa la figura, o coleccion de trazados.
La variable ax representa un trazado unico de la figura. La función plot() traza los datos que recibe.
'''
valores_entrada = [1,2,3,4,5]
cuadrado = [1,4,9,16,25]

plt.style.use('seaborn')

fig, ax = plt.subplots()

ax.plot(valores_entrada,cuadrado,linewidth=3)

#Título del gráfico
ax.set_title("Cuadrado de un número", fontsize = 24)
ax.set_xlabel("Valor", fontsize = 14)
ax.set_ylabel("Cuadrado", fontsize = 14)
#Establece el tamaño de las etiquetas de los puntos de los ejes
ax.tick_params(axis='both', which='major', labelsize =14)

plt.show()







