from random import choice

class RandomWalk:
    """Una clase para generar caminos aleatorios"""

    def __init__(self, num_points=5000):
        """Inicializa los atributos del camino"""

        self.num_points= num_points

        #Todos los caminos empiezan en (0,0)
        self.x_values=[0] #Lista con los valores de x
        self.y_values=[0] #Lista con los valores de y

    def rellenar_camino(self):
        """Calcula todos ls puntos del camino, decide si va izquierda o derecha yc uanto avanza en la dirección, arriba o abajo  y hasta donde llegará"""
        
        while len(self.x_values) < self.num_points:

            #Decide en que direccion ir y cuando avanzar en esa dirección
            x_direccion = choice([1,-1]) #Izquierda o derecha
            x_distancia = choice([0,1,2,3,4]) #Cuanto se desplaza, se incluye el 0 para poder moverse por los ejes
            x_paso = x_direccion * x_distancia

            y_direccion = choice([1,-1]) #Arriba o abajo
            y_distancia = choice([0,1,2,3,4])
            y_paso = y_direccion * y_distancia

            #Rechaza movimiento que no van a ninguna parte y continua el bucle ignorando el movimiento
            if x_paso == 0 and y_paso == 0:
                continue
            
            #Calcula la nueva posición. Sumamos a los valores la distancia recorrida  y los añadimos a la lista
            x = self.x_values[-1] + x_paso 
            y = self.y_values[-1] + y_paso

            self.x_values.append(x)
            self.y_values.append(y)





