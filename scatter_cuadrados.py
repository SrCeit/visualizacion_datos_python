import matplotlib.pyplot as plt

x_valor= range(1,1001)
y_valor=[x**2 for x in x_valor]

plt.style.use('seaborn')

fig, ax = plt.subplots()

ax.scatter(x_valor,y_valor,c=(0,0.8,0), s=10)

ax.set_title("Números cuadrados", fontsize=24)
ax.set_xlabel("Valor", fontsize=14)
ax.set_ylabel("Cuadrado", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 1100, 0, 1100000])

plt.show()