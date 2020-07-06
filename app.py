from flask import Flask,render_template,request
import pickle
import numpy as np


model=pickle.load(open('iri.pkl','rb'))

app=Flask(__name__)

@app.route("/")

def fun():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])

def home():
    d1=request.form['a']
    d2=request.form['b']
    d3=request.form['c']
    d4=request.form['d']
    arr=np.array([[d1,d2,d3,d4]])
    pred=model.predict(arr)
    return render_template('after.html',data=pred)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8080)

