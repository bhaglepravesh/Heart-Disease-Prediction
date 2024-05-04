from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load the model
model = joblib.load('model.joblib')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Heart Disease Prediction System.html')

if __name__ == '__main__':
    app.run(debug=True)

