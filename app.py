# -*- coding: utf-8 -*-


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def master():
    return render_template('master.html')

@app.route('/index')
def index():

    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/predict',methods=['POST'])
def predict():
   int_features=[]
   Age=request.form['age']
   int_features.append(float(Age))
   Sex=request.form['sex']
   int_features.append(float(Sex))
   Steroid=request.form['steroid']
   int_features.append(float(Steroid))
   Antivirals=request.form['antivirals']
   int_features.append(float(Antivirals))
   Fatigue=request.form['fatigue']
   int_features.append(float(Fatigue))
   Malaise=request.form['malaise']
   int_features.append(float(Malaise))
   Anorexia=request.form['anorexia']
   int_features.append(float(Anorexia))
   Liver_big=request.form['liver']
   int_features.append(float(Liver_big))
   Liver_firm=request.form['liver_firm']
   int_features.append(float(Liver_firm))
   Spleen_palable=request.form['spleen_palable']
   int_features.append(float(Spleen_palable))
   Spiders=request.form['spiders']
   int_features.append(float(Spiders))
   Ascites=request.form['ascites']
   int_features.append(float(Ascites))
   Varices=request.form['varices']
   int_features.append(float(Varices))
   Bilirubin=request.form['bilirubin']
   int_features.append(float(Bilirubin))
   Alk_phosphate=request.form['alk_phosphate']
   int_features.append(float(Alk_phosphate))
   Sgot=request.form['sgot']
   int_features.append(float(Sgot))
   Albumin=request.form['albumin']
   int_features.append(float(Albumin))
   Protime=request.form['protime']
   int_features.append(float(Protime))
   Histology=request.form['histology']
   int_features.append(float(Histology))
   print(int_features)
   final_features=[np.array(int_features)]
   print(final_features)
   prediction = model.predict(final_features)
   print(prediction)
   output = float(prediction)
   print(output)
   if output == 1:
       return render_template('prediction.html', prediction_result='Person has no hepatitis')
   else:
       return render_template('prediction.html', prediction_result='Person has hepatitis')



if __name__=="__main__":
    app.run(debug=True)