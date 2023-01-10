from bokeh.plotting import figure, output_file, show
import pandas as pd

graph = figure(title = "Bokeh Bar Chart")
 
path = "D:/Downloads/tips.csv"
data = pd.read_csv(path)
 
graph.vbar(data['total_bill'], top=data['tip'])

show(graph)