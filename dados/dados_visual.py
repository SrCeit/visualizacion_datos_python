from dado import Dado
from plotly.graph_objs import Bar, Layout
from plotly import offline

dado_1 = Dado() #Dado de 6 caras
dado_2 = Dado()

results = []

for num in range(100000):
    result= dado_1.lanzar() + dado_2.lanzar()
    results.append(result)

frecuencias = []

maximo = dado_1.num_sides + dado_2.num_sides
for valor in range(2, maximo+1):
    frecuencia= results.count(valor)
    frecuencias.append(frecuencia)
print(frecuencias)

#Visualizar los datos:
x_values = list(range(2, maximo +1))
data = [Bar(x = x_values, y = frecuencias)]

x_axis_config = {'title': 'Result', 'dtick':1} #dtick gestiona el espacio entre marcas
y_axis_config = {'title': 'Frecuencia del resultado'}
my_layout = Layout(title='Resultados de lanzamiento', xaxis= x_axis_config, yaxis= y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
