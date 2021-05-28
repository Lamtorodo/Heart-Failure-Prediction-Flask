import pickle

import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    '''
    pour l'affichage sur html
    '''

    features = request.form.to_dict()
    features = list(features.values())
    features = list(map(int, features))
    print(features)
    final_features = np.array(features).reshape(1,12)
    prediction = model.predict(final_features)

    #select = request.form.get('category')
    output = round(prediction[0], 2)
    if (format(output)==1):
        prediction_text='This patient has a high risk to die from heart failure '
    else :
        prediction_text='This patient has a low risk to die from a heart failure '    
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)