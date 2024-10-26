from flask import Flask, render_template, request
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import os

#set two environment variables, FLASK_APP and FLASK_ENV
os.environ['FLASK_APP'] = 'main.py'
os.environ['FLASK_ENV'] = 'development' 

#Instantiate the Flask app
app = Flask(__name__)

# Load the trained model
with open('logistic_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the TfidfVectorizer
with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
# Safely get email content from form
        email_text = request.form.get('email_text')  
        if email_text:  # Ensure there is text input
# Vectorize the input text using the loaded TfidfVectorizer
            email_vectorized = vectorizer.transform([email_text])
# Print email text and vectorized text shape
            print("Email text input:", email_text)                 
            print("Vectorized input shape:", email_vectorized.shape)
# Make a prediction using the loaded model
            prediction = model.predict(email_vectorized)
            print("Prediction:", prediction)
# Interpret prediction result
            result = 'spam' if int(prediction[0]) == 0 else 'ham'

# Render result back to the HTML template
            return render_template('index.html', prediction=result)
        else:
# Handle empty form input case
            return render_template('index.html', prediction="Please enter email content.")
#start the server
if __name__ == '__main__':
    app.run(debug=True)
