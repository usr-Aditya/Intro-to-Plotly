import plotly
import plotly.graph_objs
plotly.offline.plot({
"data": [
    plotly.graph_objs.Scatter(    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13], mode='markers',
    marker=dict(
        size=[40, 60, 80, 100]))],
"layout": plotly.graph_objs.Layout(showlegend=False,
    height=600,
    width=600,
)
})
