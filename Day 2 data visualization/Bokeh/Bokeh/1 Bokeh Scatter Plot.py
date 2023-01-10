from bokeh.plotting import figure, show
from bokeh.palettes import magma
from bokeh.palettes import viridis
import pandas as pd
#pip install bokeh
path = "D:/Downloads/tips.csv"
data = pd.read_csv(path)

graph = figure(title = "Bokeh Scatter Graph")

#https://docs.bokeh.org/en/2.4.2/docs/reference/palettes.html
#color = magma(256)
color = viridis(256)
 
graph.scatter(data['total_bill'], data['tip'], color=color)
show(graph)