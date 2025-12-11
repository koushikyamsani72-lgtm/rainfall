from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
model=pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    data=[
        float(request.form["humidity"]),
        float(request.form["temperature"]),
        float(request.form["windspeed"]),
        float(request.form["cloud"])
    ]
    pred=model.predict([data])[0]
    return render_template("result.html",prediction=round(pred,2))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
