import plotly.express as px
import pandas as pd
from plotly.offline import plot

data = {
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Studying_Hours': [4, 3, 2, 5, 1],
    'Sleep_Hours': [7, 6, 7, 8, 7]
}

df = pd.DataFrame(data)

fig = px.line(df, x='Date', y=['Studying_Hours', 'Sleep_Hours'],
              color_discrete_sequence=['blue', 'green'],
              title="Engineering Student's Daily Studying and Sleeping Time Series",
              labels={'value': 'Hours'})

fig.update_layout(legend_title_text='Activities')

plot(fig, filename='Student_statistics.html')
