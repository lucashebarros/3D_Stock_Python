import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import random

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H2("Estoque em Tempo Real"),
        dcc.Dropdown(
            id='warehouse-select',
            options=[
                {'label': 'Armazém 1', 'value': '0'},
                {'label': 'Armazém 2', 'value': '1'},
                {'label': 'Armazém 3', 'value': '2'},
            ],
            value='0',
            clearable=False,
        ),
        html.Div(id='total-items', children="Total de Itens: 0"),
        html.Div(id='low-stock', children="Estoque Baixo: 0"),
        dcc.Graph(id='stock-chart'),
        html.Div(id="selected-item-info", children="Nenhum item selecionado"),
    ], style={'width': '300px', 'padding': '20px', 'background': '#f4f4f4', 'display': 'flex', 'flexDirection': 'column'}),

    # IFrame para o 3D externo
    html.Iframe(
        src="/assets/warehouse_3d.html",  # Supondo que o arquivo esteja em assets/warehouse_3d.html
        style={'flex': '1', 'height': '100vh', 'width': '100%'}
    )
], style={'display': 'flex'})

@app.callback(
    [Output('stock-chart', 'figure'), Output('total-items', 'children'), Output('low-stock', 'children')],
    [Input('warehouse-select', 'value')]
)
def update_stock(warehouse):
    quantities = [random.randint(1, 15), random.randint(1, 5), random.randint(1, 10)]
    total_items = sum(quantities)
    low_stock = len([q for q in quantities if q <= 3])

    fig = go.Figure(
        data=[
            go.Bar(
                x=['Item A', 'Item B', 'Item C'],
                y=quantities,
                marker=dict(color=['#4caf50', '#f44336', '#2196f3'])
            )
        ],
        layout=go.Layout(
            title='Quantidade em Estoque',
            xaxis=dict(title='Item'),
            yaxis=dict(title='Quantidade', range=[0, 20])
        )
    )

    return fig, f"Total de Itens: {total_items}", f"Estoque Baixo: {low_stock}"

if __name__ == '__main__':
    app.run_server(debug=True)
