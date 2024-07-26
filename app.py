from flask import Flask, render_template, request
from flask_static_digest import FlaskStaticDigest
import model

app = Flask(__name__)
flask_static_digest = FlaskStaticDigest(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    season = request.form['season']
    trained_model = model.train_model()
    predictions = model.predict_rookie_of_the_year(trained_model, season)
    return render_template('result.html', season=season, predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)
