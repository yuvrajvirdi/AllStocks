from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)

@app.route('/')
def get_stock():
    return render_template('index.html')