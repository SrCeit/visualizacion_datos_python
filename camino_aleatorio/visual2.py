import matplotlib.pyplot as plt
from caminos_random import RandomWalk


while True:
    rw = RandomWalk() 
    rw.rellenar_camino()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9), dpi= 720) 
    point_numbers = range(rw.num_points) 

    ax.plot(rw.x_values, rw.y_values, linewidth=1) 

    #Elimina los ejes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    seguir = input("Quieres seguir? y/n: ")
    if seguir == 'n':
        break


