from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/get-prediction',methods=['POST'])
def get_prediction():
    return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True)