import numpy as np
from flask import Flask, render_template, request, redirect
import pickle
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/Predict')
def prediction():
    return render_template('Index.html')
@app.route('/home')
def homee():
    return render_template('Home_1.html')

@app.route('/form', methods=["POST"])
def brain():
    Nitrogen=float(request.form['Nitrogen'])
    Phosphorus=float(request.form['Phosphorus'])
    Potassium=float(request.form['Potassium'])
    Temperature=float(request.form['Temperature'])
    Humidity=float(request.form['Humidity'])
    Ph=float(request.form['ph'])
    Rainfall=float(request.form['Rainfall'])
     
    values=[Nitrogen,Phosphorus,Potassium,Temperature,Humidity,Ph,Rainfall]
    
    if Ph>0 and Ph<=14 and Temperature<100 and Humidity>0:
        
        arr = [values]
        acc = model.predict(arr)
        # print(acc)
        return render_template('prediction.html', prediction="According to given soil nutrients, Best crop to grow is: "+str(acc))
    else:
        return render_template('Sorry.html', prediction="Sorry... No crop can be grown with the given weather and soil conditions")



if __name__ == '__main__':
    app.run(debug=True)
