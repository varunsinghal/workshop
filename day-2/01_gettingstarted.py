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


if __name__ == '__main__':
    app.run()
