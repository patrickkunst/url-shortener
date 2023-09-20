from flask import Flask, request, redirect
from src.sql import connectToSql

app = Flask(__name__)


@app.route("/addurl", methods=["POST"])
def add_url():
    try:
        data = request.json
        db = connectToSql()
        cursor = db.cursor()
        sql = "INSERT INTO urls (short, full) VALUES (%s, %s)"
        vals = (data["short"], data["full"])
        cursor.execute(sql, vals)
        db.commit()
        db.close()
        return "success"
    except:
        return "something went wrong"


@app.route("/<url>", methods=["GET"])
def get_url(url):
    try:
        db = connectToSql()
        cursor = db.cursor()

        sql = "SELECT full FROM urls WHERE short = '" + url + "'"
        cursor.execute(sql)
        res = cursor.fetchall()
        print(res[0][0])
        db.close()
        return redirect(res[0][0])
    except:
        return "something went wrong"
