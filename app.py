from flask import Flask, render_template, request
from scrapers import get_data, get_financials, get_holders, get_profile, get_analytics
from graph import make_graph, make_rev_graph, make_pie_graph
from sign import check_sign


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/get_stock', methods=['GET', 'POST'])
def get_stock():
    if request.method == "POST":
        stock_name = request.form.get('stock')

        data = get_data(stock_name)
        financial_data = get_financials(stock_name)
        holders_data = get_holders(stock_name)
        profile = get_profile(stock_name)
        growth = get_analytics(stock_name)

        candle_graph = make_graph(stock_name)
        rev_graph = make_rev_graph(financial_data)
        pie_graph = make_pie_graph(holders_data)
        
        colour = check_sign(data,'percent')

        return render_template('card.html', data=data, profile=profile, growth=growth, colour=colour)

    else:
        return render_template('index.html')

@app.errorhandler(500)
def handle_500(e):
    error = 'Please enter valid inputs'
    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run()
