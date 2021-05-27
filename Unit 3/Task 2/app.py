from flask import Flask, render_template,request,url_for
from flask_bootstrap import Bootstrap 
from nltk.tokenize import sent_tokenize
import pandas as pd 


# NLP Packages
from textblob import TextBlob,Word 
import random 
import time

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')     

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method== 'POST':
        text = request.form['text']
        string=sent_tokenize(text)
        df=pd.DataFrame({'sentence':string})
        df1=pd.DataFrame({'sentence':string})
        l=[]
    for s in string:
        analysis = TextBlob(s).sentiment
        analysisPol = TextBlob(s).polarity
#analysisNeu = TextBlob(sentence).neutral
        if analysisPol ==0:
            l.append('Neutral')
        elif analysisPol >0:
            l.append('Positive')
        else:
            l.append('Negative')
    df['sentimental']=l 
    #df = pd.DataFrame(l)
    analysis = TextBlob(text).sentiment
    analysisPol = TextBlob(text).polarity
    if analysisPol ==0:
        output=('Neutral')
    elif analysisPol >0:
        output=('Positive')
    else:
        output=('Negative')
    return render_template('/success.html',tab=[df1.to_html(classes='data table table-striped')],title=df.columns.values, tables=[df.to_html(classes='data table table-striped')],titles=df.columns.values, output=f'The sentimened analysis of whole paragraph is {output}')


if __name__ == "__main__":
    app.run(debug=True)