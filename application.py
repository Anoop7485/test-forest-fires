<<<<<<< HEAD
import pickle
from flask import Flask, request, jsonify, render_template

application = Flask(__name__)
app = application


ridge_model = pickle.load(open('models/ridge.pkl',"rb"))
print(" Ridge model loaded")
standard_scaler = pickle.load(open('models/scaler.pkl', "rb"))
print(" Scaler loaded")


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/predictdata",methods=['GET','POST'])

def predict_datapoint():
    if request.method=="POST":
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        WS=float(request.form.get('WS'))
        RAIN=float(request.form.get('RAIN'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        CLASSES=float(request.form.get('CLASSES'))
        REGION=float(request.form.get('REGION'))
        new_data_scaled=standard_scaler.transform([[Temperature,RH,WS,RAIN,FFMC,DMC,ISI,CLASSES,REGION]])
        result=ridge_model.predict(new_data_scaled)
        
        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
=======
import pickle
from flask import Flask, request, jsonify, render_template

application = Flask(__name__)
app = application


ridge_model = pickle.load(open('models/ridge.pkl',"rb"))
print(" Ridge model loaded")
standard_scaler = pickle.load(open('models/scaler.pkl', "rb"))
print(" Scaler loaded")


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/predictdata",methods=['GET','POST'])

def predict_datapoint():
    if request.method=="POST":
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        WS=float(request.form.get('WS'))
        RAIN=float(request.form.get('RAIN'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        CLASSES=float(request.form.get('CLASSES'))
        REGION=float(request.form.get('REGION'))
        new_data_scaled=standard_scaler.transform([[Temperature,RH,WS,RAIN,FFMC,DMC,ISI,CLASSES,REGION]])
        result=ridge_model.predict(new_data_scaled)
        
        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
>>>>>>> b02853ef (first commit)
