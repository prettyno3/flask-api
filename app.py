from flask import Flask, render_template, jsonify
from dataApi.stockQuote import getData
import os

app = Flask(__name__)


@app.route("/dataApi/<ticker>")
def dataApi(ticker=None):
    return jsonify(getData(ticker=ticker))


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8888))
    app.run(host='0.0.0.0', port=port)
