from flask import Flask,render_template,request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app=Flask(__name__)

@app.route('/',methods=["GET"])
@cross_origin()
def homePage():
    return render_template('index.html')

@app.route('/predict',methods=["POST","GET"])
@cross_origin()

def index():
    if request.method == 'POST':
        try:
            RM=float(request.form['RM'])
            LSAT=float(request.form['LSAT'])

            filename='modelx.pickle'
            loaded_model =pickle.load(open(filename,'rb'))

            prediction = loaded_model.predict([[RM,LSAT]])
            print('predicted house price is',prediction,"$")

            return render_template('results.html',prediction=(1000*prediction))

        except Exception as e:
            print('the exception message is:',e)
            return "something is wrong"

    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()


