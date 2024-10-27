`# EMAIL-SPAM-HAM-CLASSIFICATION

##TABLE OF CONTENT
* Demo
* Overview
* Motivation
* Technical Aspect
* Installation
* Run
* Deployement on Heroku
* Directory Tree
* To Do
* Bug / Feature Request
* Technologies Used
* Team
* License
* Credits

### DEMO
Link: https://ebb8b4b2-83ff-495c-b7ba-642c48fd3086-00-3je7c51leuy1s.riker.replit.dev/
![CLASSIFIER DEMO](https://github.com/user-attachments/assets/e8d67dfe-554b-40d2-a6d8-7ec8f2ec122e)

###  OVERVIEW
This is a simple email classification Flask app trained on Logistic Regression. The trained model takes an email text as an input and classification is done to identify spam and ham emails. 

### MOTIVATION
I began my python language learning sessions in june 2023, i was busy learning different parts of python only to end up forgetting because i was not applying the knowledge and this project is a remedy to that Challenge. I watched a couple of youtube videos and did some research on Chatgpt.  This is my first Machine learning Project and I just came to the realization that i can do a lot with the knowledge that i've been accumulating. let's get to it.  

### TECHNICAL ASPECT
This project is divided into two part:

Training a deep learning model using Keras. (Not covered in this repo. I'll update the link here once I make it public.)
Building and hosting a Flask web app on Heroku.
A user can choose image from a device or capture it using a pre-built camera.
Used Amazon S3 Bucket to store the uploaded image and classification.
Used CSRF Token to protect against CSRF attacks.
Used Sentry to catch the exception on the back-end.
After uploading the image, the classifications are displayed on a Bar Chart.

### INSTALLATION
The Code is written in Python 3.11.9. If you don't have Python installed you can find it [here](https://www.python.org/downloads/release/python-3119/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in your shell:
'''
pip install scikit-learn
pip install pandas
pip install numpy
pip install flask
pip install pickle
'''
### RUN
###DEPLOYMENT ON HEROKU
### PROJECT DIRECTORY TREE 
'''
project/  
│  
├── main.py           
├── model/  
│     ├── model.pkl  
│     └── tfidf_vectorizer.pkl  
├── templates/  
│     └── index.html  
└── .replit  

'''
### TO-DO  
### BUG/ FEATURE REQUEST  
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an [issue](https://github.com/pizzyander/EMAIL-SPAM-HAM-CLASSIFICATION/issues) here by including your search query and the expected result.  

If you'd like to request a new function, feel free to do so by opening an [issue](https://github.com/pizzyander/EMAIL-SPAM-HAM-CLASSIFICATION/issues) here.  

### TECHNOLOGY USED
### TEAM
AKINFE ADESANMI THOMAS
![AKINFE ADESANMI](https://github.com/user-attachments/assets/92f1721e-ab4c-428b-8b7d-48ffef1cea4b)

### LICENSE
### CREDIT

### DEMO
