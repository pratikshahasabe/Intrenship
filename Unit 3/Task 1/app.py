from flask import Flask, render_template,url_for,request, redirect, jsonify
import pickle#Initialize the flask App
import numpy as np


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
     return render_template('index.html')     

@app.route('/predict',methods=['GET','POST'])
def predict():
   
    post_name=request.form['name']
    int_features = [int(request.form['hours_you_slep'])]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = np.round(prediction[0][0])
    return render_template('/success.html', prediction_text=f'Hello, {post_name}. you sleep {final_features[0][0]} hours. and you active {int(output)} hours')


if __name__ == "__main__":
    app.run(debug=True)