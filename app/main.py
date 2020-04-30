from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('pages/dashboard.html')

@app.route('/nutrition', methods=['GET'])
def nutrition():
    return render_template('pages/nutrition.html')

@app.route('/training', methods=['GET'])
def training():
    return render_template('pages/training.html')

@app.route('/measurements', methods=['GET'])
def measurements():
    return render_template('pages/measurements.html')
