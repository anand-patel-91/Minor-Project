from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__, template_folder='templates', static_url_path='/static')

# Load the dataset and train the model
data = pd.read_csv('sm_MadhyaPradesh_2020.csv')
X = data.drop(columns=['DistrictName', 'State Name', 'Date'])
y = data['DistrictName']
clf = RandomForestClassifier(random_state=42)
clf.fit(X, y)

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [data['feature1'], data['feature2'], data['feature3'], data['feature4']]
    predicted_district = clf.predict([features])[0]
    return jsonify({'predicted_district': predicted_district})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
