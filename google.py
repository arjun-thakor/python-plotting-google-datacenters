from plotly.offline import plot
import plotly.graph_objs as go

# mapbox_access_token = '---------------ADD_YOUR_TOKEN_HERE-----------------------'

data = [
    go.Scattermapbox(
        lat=['45.598969','33.194790','41.258961', '39.059010', '34.680090', '35.905392',
             '36.452290', '36.318310', '-33.359741', '24.075550', '1.352083', '53.349804',
             '53.442108', '60.569199', '50.447849'],
        lon=['-121.178940', '-80.010353', '-95.854362', '-88.544850', '-86.077760',
             '-81.534737', '-95.378070', '-87.364820', '-70.726501', '120.545067',
             '103.819839', '-6.260310', '6.825710', '27.193800', '3.820250'],
        mode='markers',
        hoverlabel=dict(font=dict(family='Roboto, sans-serif', size=18, color='white')),
        marker=dict(
            size=10,
            color='orange'
        ),
        text=['The Dalles - Oregon', 'Berkeley County, South Carolina','Council Bluffs - Iowa',
              'Douglas County - Georgia', 'Jackson County - Alabama', 'Lenoir - North Carolina',
              'Mayes County - Oklahoma', 'Montgomery County - Tennessee', 'Quilicura - Chile',
              'Changhua County - Taiwan', 'Singapore', 'Dublin - Ireland', 'Eemshaven - Netherlands',
              'Hamina - Finland', 'St. Ghislain - Belgium']
    )
]

layout = go.Layout(
    title='Google Data Centers',
    font=dict(family='Roboto, sans-serif', size=18, color='#7f7f7f'),
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken='---------------ADD_YOUR_TOKEN_HERE-----------------------',
        style='light'
    ),
)

fig = dict(data=data, layout=layout)

plot(fig, filename='G-DataCenters.html')
