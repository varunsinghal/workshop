import pandas as pd
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/preview")
def preview():
    start = request.args.get("start", type=int, default=0)
    end = request.args.get("end", type=int, default=5)
    df = pd.read_csv("physician_rx.csv")
    return df[start:end].to_html()


@app.route("/column/<column_name>")
def column_preview(column_name):
    df = pd.read_csv("physician_rx.csv")
    return df[[column_name]].to_html()


if __name__ == '__main__':
    app.run()
