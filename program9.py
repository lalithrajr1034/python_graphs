import plotly.express as ex
import pandas as pd

data =pd.DataFrame({
    'a': [1,2,3,4,5],
    'b': [2,3,4,5,6],
    'c': [3,4,5,6,7],
    'name': ['A','B','C','D','E']
    })
lalith=ex.scatter_3d(data,x='a',y='b',z='c',text='name')
lalith.show()