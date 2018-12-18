import pandas as pd
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/preview")
def preview():
    df = pd.read_csv("physician_rx.csv")
    return df[0:5].to_html()


@app.route("/column/<column_name>")
def column_preview(column_name):
    df = pd.read_csv("physician_rx.csv")
    return df[[column_name]].to_html()


if __name__ == '__main__':
    app.run()
