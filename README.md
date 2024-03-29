![AllStocks](/demo/logo.png)

Flask stock dashboard web application.

# Introduction

* AllStocks is a dashboard web application that scrapes information on whatever stock you want off [Yahoo Finance](https://ca.finance.yahoo.com).
* Built using Python and Flask.
* Utilizes BeautifulSoup and requests to web scrape stock data.
* Utilizes Plotly to display graphs containing key information about an inputted stock.
* Displays important information regarding the inquired stock in a modern card format.
* Utilizes NLP (spaCy) to generate summarized company descriptions
* Leverages LSTMs using Tensorflow and Keras to make a prediction model graph for Apple stock prices

# Installation

Clone the git repo in your directory.

```bash
git clone https://github.com/yuvrajvirdi/AllStocks.git
```

Set up a virtual environment in your desired directory, and activate it.

```bash
python3 -m venv venv && . venv/bin/activate
```

Use pip in your virtual environment to install the necessary packages and libraries.

```bash
pip install -r requirements.txt
```

# Use

Run the application by using the following command:

```bash
python app.py
```
# Next steps

Planning to implement a chat room feature.

# Demo

Enter a stock into the search box.

![Home](/demo/home.png)

The app will load a dashboard with your stock's information.

![Dashboard](/demo/dashboard.png)

All graphs have interactivity, and below the candlelight graph is where you can search again for other stocks.

![Research](/demo/candlelight.png)







