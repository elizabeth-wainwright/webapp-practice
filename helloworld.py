from os import path
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/breed_input")
def fill_in():
    return render_template("input.html")

@app.route("/breed", methods=["POST", "GET"])
def breed():
    if request.method == "POST":
        result = request.form
        return render_template("output_display.html", animal=result["Animal"], breed=result["Breed"])

if __name__ == "__main__":
    app.run(host="10.0.0.178", port=80, debug=True)