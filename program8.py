from bokeh.layouts import row
from bokeh.plotting import figure as figs,show
from bokeh.models import HoverTool

fig1 = figs(title="Plot 1")
x1 = [2,3,5,6]
y1 = [1,4,4,7]
b=fig1.line(x1, y1)
hover1 = HoverTool(tooltips=[("X", "@x"), ("Y", "@y")])
fig1.add_tools(hover1)

x2 = (1,2,3,4,5,6,7,8,9)
y2 = (1,2,3,4,5,6,7,8,9)
fig2 = figs(title="Plot 2")
a=fig2.circle(x2, y2, size=5)
hover2 = HoverTool(tooltips=[("X", "@x"), ("Y", "@y")])
fig2.add_tools(hover2)

show(row(fig1, fig2))
