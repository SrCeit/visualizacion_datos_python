from dado import Dado
from plotly.graph_objs import Bar, Layout
from plotly import offline

dado = Dado() #Dado de 6 caras

results = []

for num in range(100000):
    result= dado.lanzar()
    results.append(result)

frecuencias = []

for valor in range(1, dado.num_sides+1):
    frecuencia= results.count(valor)
    frecuencias.append(frecuencia)
print(frecuencias)

#Visualizar los datos:
x_values = list(range(1, dado.num_sides +1))
data = [Bar(x = x_values, y = frecuencias)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frecuencia del resultado'}
my_layout = Layout(title='Resultados de lanzamiento', xaxis= x_axis_config, yaxis= y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
