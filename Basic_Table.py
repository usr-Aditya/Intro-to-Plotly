
import plotly
import plotly.graph_objs as go

trace = go.Table(
    header=dict(values=['A Scores', 'B Scores']),
    cells=dict(values=[[100, 90, 80, 90],
                       [95, 85, 75, 95]]))

data = [trace] 
plotly.offline.plot(data, filename = 'basic_table')