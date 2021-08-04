import matplotlib.pyplot as plt
from caminos_random import RandomWalk


while True:
    rw = RandomWalk()
    rw.rellenar_camino()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points) #Creamos un rango con la longitud igual a los puntos y lo almacenamos  en una lista

    ax.scatter(rw.x_values, rw.y_values, c= point_numbers, cmap = plt.cm.Blues, edgecolors='none', s=15) #edgecolors indica elcolor del borde

    #Enfatizar el primer punto y el último
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s= 100)

    #Elimina los ejes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    seguir = input("Quieres seguir? y/n: ")
    if seguir == 'n':
        break

