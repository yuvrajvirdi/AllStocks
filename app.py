from re import S
from flask import Flask, render_template, request
from scraper import get_data
from graph import make_graph

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_stock():
    if request.method == "POST":
        stock_name = request.form.get('sname')
        period = request.form.get('period')
        data = get_data(stock_name)
        stock_graph = make_graph(stock_name, period)
        return render_template('card.html', data=data)
    else:
        return render_template('index.html')
    
@app.errorhandler(500)
def handle_500(e):
    error = 'Please enter valid inputs'
    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run()
