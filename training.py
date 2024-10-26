import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import zipfile
import pickle


# Path to the zip file
zip_path = 'archive (7).zip'

# Open the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
# List all files in the zip archive
    print(zip_ref.namelist())

# Read a specific file inside the zip (e.g., a CSV file)
    with zip_ref.open('combined_data.csv') as f:
# Load the file content into a pandas DataFrame
        df = pd.read_csv(f)
        print(df.head())

# Split dataset into features (X) and labels (y)
x = df['text']
y = df['label']

# Split the data into training and test sets (80% train, 20% test)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=2, stratify=y)

# Creating a TfidfVectorizer with additional parameters to optimize efficiency
feature_extraction = TfidfVectorizer(
    min_df=2,  # Increases minimum document frequency to ignore very rare words
    max_df=0.9,  # Ignores very common words appearing in >90% of documents
    max_features=10000,  # Limits number of features for faster processing
    stop_words='english', 
    lowercase=True
)

# Transform the train and test datasets
x_train_features = feature_extraction.fit_transform(x_train)
x_test_features = feature_extraction.transform(x_test)

# Convert labels to integers
y_train = y_train.astype('int')
y_test = y_test.astype('int')

# Build and train the Logistic Regression model with optimized parameters
model = LogisticRegression(solver='liblinear', class_weight='balanced', max_iter=200)

# Train the model on training data
model.fit(x_train_features, y_train)

# Calculate accuracy on training data
train_predictions = model.predict(x_train_features)
train_accuracy = accuracy_score(y_train, train_predictions)
print(f"Accuracy on training data: {train_accuracy}")

# Calculate accuracy on test data
test_predictions = model.predict(x_test_features)
test_accuracy = accuracy_score(y_test, test_predictions)
print(f"Accuracy on test data: {test_accuracy}")

# Display confusion matrix for the test data
conf_matrix = confusion_matrix(y_test, test_predictions)
print("Confusion Matrix:\n", conf_matrix)

# Test the model on new email data
new_email = ["i love ajuma, but my ego always gets in the way. kindly send me a book to help me get over my ego"]
new_email_features = feature_extraction.transform(new_email)
prediction = model.predict(new_email_features)
print("Prediction on new email:", "Spam" if prediction[0] == 1 else "Ham")

# Save the trained model and vectorizer to files for later use
with open('logistic_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('tfidf_vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(feature_extraction, vectorizer_file)

# Load the model and vectorizer for validation
with open('logistic_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    loaded_vectorizer = pickle.load(vectorizer_file)