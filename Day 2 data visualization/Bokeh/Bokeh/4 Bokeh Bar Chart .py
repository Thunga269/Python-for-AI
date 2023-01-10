from bokeh.plotting import figure, output_file, show
import pandas as pd

path = "D:/Downloads/tips.csv"
data = pd.read_csv(path)

graph = figure(title = "Bokeh Bar Chart")

graph.vbar(data['total_bill'], top=data['tip'],
           legend_label = "Bill VS Tips", color='green')
 
graph.vbar(data['tip'], top=data['size'],
           legend_label = "Tips VS Size", color='red')
 
graph.legend.click_policy = "hide"

show(graph)