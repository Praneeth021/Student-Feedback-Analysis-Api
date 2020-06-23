from flask import Flask,render_template
from flask_restful import Resource,Api
from NLP_util import pred

app=Flask(__name__)

@app.route('/')
def Hello():
    ans=pred('Teaches well')
    res= "postive" if ans==1 else "negative"
    return (f'Your prediction is {res} becoz its {ans}')


if __name__=='__main__':
    app.run(debug=True)