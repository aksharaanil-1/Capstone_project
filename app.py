from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(_name_)

# Load your trained model (assuming it is saved as 'model.pkl')
# model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index_form.html')  # Create an HTML form for user input

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the form data
        time = float(request.form['time'])
        amount = float(request.form['amount'])
        features = [float(request.form[f'V{i}']) for i in range(1, 29)]  # Assume V1-V28 are inputs

        # Combine all features into a single input array
        input_data = np.array([[time] + features + [amount]])

        # Predict using your model (replace with your actual model)
        # prediction = model.predict(input_data)

        # For now, let's just return the input
        return f"Input received: {input_data}"
    
    return "Error"

if _name_ == '_main_':
    app.run(debug=True)