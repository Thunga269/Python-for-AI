from bokeh.plotting import figure, show
import pandas as pd

path = "D:/Downloads/tips.csv"
data = pd.read_csv(path) 

graph = figure(title = "Bokeh Line Chart")

# Đếm tần số xuất hiện
df = data['tip'].value_counts()

graph.line(df, data['tip'])

show(graph)