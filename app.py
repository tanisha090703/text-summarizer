from flask import Flask, render_template,session,redirect,request
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
from text_summary import summarizer

global rawdocs,stopwords


app=Flask(__name__,template_folder='templates')


@app.route('/')
def index():
    return render_template('home.html')
    


@app.route('/home',methods=['GET','POST'])
def home():
    if request.method=='POST':
        rawdocs=request.form['rawdocs']
        return redirect('analyse.html')
    return render_template('home.html')

@app.route('/analyse',methods=['GET','POST'])
def analyse():
    if request.method=='POST':
        rawtext=request.form['rawtext']
        summary,original_txt=summarizer(rawtext)
    return render_template('analyse.html',summary=summary,rawtext=rawtext)
        









if __name__=='__main__':
    app.secret_key='secret_key'
    app.run(debug=True)