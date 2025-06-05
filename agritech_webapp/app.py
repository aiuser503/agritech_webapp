from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/disease", methods=["GET", "POST"])
def disease():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join("static", file.filename)
            file.save(filepath)
            result = "The leaf image shows signs of Leaf Rust disease."
            return render_template("disease.html", filename=file.filename, result=result)
    return render_template("disease.html")

@app.route("/stress", methods=["GET", "POST"])
def stress():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join("static", file.filename)
            file.save(filepath)
            result = "The plant shows signs of water stress."
            return render_template("stress.html", filename=file.filename, result=result)
    return render_template("stress.html")

@app.route("/pest", methods=["GET", "POST"])
def pest():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join("static", file.filename)
            file.save(filepath)
            result = "The plant is affected by pests like Aphids."
            return render_template("pest.html", filename=file.filename, result=result)
    return render_template("pest.html")

@app.route("/yield")
def yield_prediction():
    result = "Predicted yield: 3.5 tons per hectare (based on sample data)."
    return render_template("yield.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
