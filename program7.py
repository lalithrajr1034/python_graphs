from bokeh.plotting import figure, show
from bokeh.models import Label, Legend

days = [1, 2, 3, 4, 5]
temperature_bengaluru = [18, 20, 22, 19, 17]
temperature_mysuru = [22, 25, 20, 26, 23]

plot = figure(title="Temperature Comparison")

line_mysuru = plot.line(days, temperature_mysuru)
line_bengaluru = plot.line(days, temperature_bengaluru,color="blue")

annotation_mysuru = Label(x=4, y=22, text="Weather in Mysuru")
annotation_bengaluru = Label(x=4, y=21, text="Weather in Bengaluru")
legend = Legend(items=[("Mysuru", [line_mysuru]),("Bengaluru", [line_bengaluru])])

plot.add_layout(legend)
plot.add_layout(annotation_mysuru)
plot.add_layout(annotation_bengaluru)
show(plot)
