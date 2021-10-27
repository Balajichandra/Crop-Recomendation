from flask import Flask,render_template,request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'RF-model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        N = int(request.form['N'])
        P = int(request.form['P'])
        K = int(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        my_prediction = classifier.predict(data)
        return render_template('result.html', prediction=my_prediction)
if __name__ == "__main__":
    app.run(debug=True)        
    