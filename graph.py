import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def make_graph(stock, per):
    st = yf.Ticker(stock)
    df = st.history(period=per)
    fig3 = make_subplots(specs=[[{"secondary_y": True}]])
    fig3.add_trace(go.Candlestick(x=df.index,open=df['Open'],high=df['High'],low=df['Low'],close=df['Close'],name='Price'))
    fig3.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume'),secondary_y=True)
    fig3.update_layout(xaxis_rangeslider_visible=False)
    fig3.add_trace(go.Scatter(x=df.index,y=df['Close'].rolling(window=20).mean(),marker_color='blue',name='20 Day MA'))
    fig3.add_trace(go.Bar(x=df.index, y=df['Volume'], name='Volume'),secondary_y=True)
    fig3.update_layout(title={'text':stock, 'x':0.5})
    fig3.update_yaxes(range=[0,800000000],secondary_y=True)
    fig3.update_yaxes(visible=False, secondary_y=True)
    fig3.update_layout(xaxis_rangeslider_visible=False)  #hide range slider
    df['diff'] = df['Close'] - df['Open']
    df.loc[df['diff']>=0, 'color'] = 'green'
    df.loc[df['diff']<0, 'color'] = 'red'
    return fig3.write_html(r'static/graph.html')


