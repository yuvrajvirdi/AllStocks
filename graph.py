import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(stock):
    st = yf.Ticker(stock)
    df = st.history(period='1y')
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Candlestick(x=df.index,open=df['Open'],high=df['High'],low=df['Low'],close=df['Close'],name='Price'))
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.add_trace(go.Scatter(x=df.index,y=df['Close'].rolling(window=20).mean(),marker_color='blue',name='20 Day MA'))
    fig.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume'),secondary_y=True)
    fig.update_layout(title={'text':stock+' Candlelight Graph', 'x':0.5})
    fig.update_yaxes(range=[0,800000000],secondary_y=True)
    fig.update_yaxes(visible=False, secondary_y=True)
    fig.update_layout(xaxis_rangeslider_visible=False)
    df['diff'] = df['Close'] - df['Open']
    df.loc[df['diff']>=0, 'color'] = 'green'
    df.loc[df['diff']<0, 'color'] = 'red'
    return fig.write_html(r'static/graph.html')

def make_rev_graph(data):
    fig = go.Figure(data=[
        go.Bar(name='Total Revenue', x=data[0], y=data[1]),
        go.Bar(name='Cost of Revenue', x=data[0], y=data[2]),
        go.Bar(name='Gross Profit', x=data[0], y=data[3])
    ])
    fig.update_layout(barmode='group')
    fig.update_layout(autosize=False,width=455,height=455)
    fig.update_layout(title_text='Revenue Breakdown over Fiscal Years', title_x=0.5)
    return fig.write_html(r'static/revgraph.html')

def make_pie_graph(arr):
    labels = arr[0]
    values = arr[1]
    fig = go.Figure(data=[go.Pie(labels=labels,values=values)])
    fig.update_layout(autosize=False,width=455,height=455)
    fig.update_layout(title_text='Major Shareholders', title_x=0.5)
    fig.update_layout(legend=dict(
        orientation="h",
        yanchor="top",
        y=0.0000000009,
        xanchor="right",
        x=1
    ))
    return fig.write_html(r'static/piegraph.html')
