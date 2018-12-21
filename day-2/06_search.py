import pandas as pd
from flask import Flask, request

app = Flask(__name__)
df = pd.read_csv("physician_rx.csv")


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/preview")
def preview():
    start = request.args.get("start", type=int, default=0)
    end = request.args.get("end", type=int, default=5)
    columns_str = request.args.get("columns", type=str, default='0')
    columns = list(map(lambda x: int(x), columns_str.split(',')))
    return df.iloc[start:end, columns].to_html()


@app.route("/column/<column_name>")
def column_preview(column_name):
    return df[[column_name]].to_html()


@app.route("/search")
def search():
    column_name = request.args.get("name", type=str)
    operator = request.args.get("operator", type=str)
    value = request.args.get("value", type=float)
    if operator == 'less than':
        return df[df[column_name] < value].to_html()
    elif operator == 'equal':
        return df[df[column_name] == value].to_html()
    elif operator == 'greater than':
        return df[df[column_name] > value].to_html()


if __name__ == '__main__':
    app.run()
