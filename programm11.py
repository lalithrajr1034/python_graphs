import plotly.express as px
from plotly.offline import plot

gapminder_data = px.data.gapminder()

print(gapminder_data.head(10).to_markdown())

df = gapminder_data.query("year==2007")

fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
                     hover_name="country", size="pop", projection="equirectangular")
plot(fig, filename='Map.html')
