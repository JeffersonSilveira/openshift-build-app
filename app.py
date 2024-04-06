import os
from flask import Flask
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
<<<<<<< HEAD:app.py
    return render_template("index.html")
=======
    return '<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="author" content="Jefferson Rosa">
    <title>The End of the Internet</title>
    <style>
        * {
            box-sizing: border-box;
        }
        html, body {
            width: 100%;
            height: 100%;
            background-color: #000;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            justify-content: space-around;
            align-items: center;
        }
        a {
            color: inherit;
            text-decoration: none;
        }
        .page {
            color: #fff;
            text-transform: uppercase;
            font-family: Times New Roman;
            font-weight: 900;
            padding: 3.3333333333333335vw;
            padding-top: 5vw;
        }
        .small-line {
            font-size: 5.833333333333333vw;
            transform: scale(1,1.5);
            line-height: 1.2;
        }
        .large-line {
            font-size: 8.333333333333334vw;
            transform: scale(1,1.5);
            line-height: 1.2;
        }
        .error {
            margin-top: 3.3333333333333335vw;
            margin-bottom: 0.5833333333333334vw;
            font-size: 3vw;
            font-family: Helvetica;
            transform: scale(1,1.5);
            font-weight: 600;
        }
        .title {
            margin-top: 1.6666666666666667vw;
            font-size: 3vw;
            font-family: Helvetica;
            transform: scale(1,1.5);
            font-weight: 600;
            line-height: .9;
            float: right;
        }
    </style>
</head>
<body>
    <div class="page">
    <div class="small-line">oops</div>
    <div class="small-line">something</div>
    <div class="large-line">went wrong</div>
    <div class="error">error:404</div>
    <div class="title">app prank created successfully</div>
    </div>
</body>
</html>'
>>>>>>> 3288f06686c2aa47c945cfb14aa3a39629888ec5:build-app.py

@app.route('/api')
def hello():
    return '{status: ok}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
