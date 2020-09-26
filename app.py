import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
# from werkzeug import secure_filename
# from linked_Jobs_US import final_output
# from glob import glob
import FinalSentimentAnalysis as sent
import jinja2
# import send_mail
from sklearn.externals import joblib
# Initialize the Flask application
app = Flask(__name__)
# app.jinja_env.filters['zip'] = zip

# store_final_data = r"D:\\Krish\\Krish_Main_Docs\\Projects\\Billable_Projects\\Web_Scraping\\web_service\\store_final_data\\"
#app.config['UPLOAD_FOLDER'] = upload_path

MODEL_FILE_PATH = r"models/LRmodel26092020.pkl"
loadModel = joblib.load(open(MODEL_FILE_PATH,'rb'))

@app.route('/')
def index():
    return render_template('indexPage.html')

@app.route('/upload', methods=['POST'])
def upload():

	inReview = request.form["review"]
	predictedVal = sent.predictSentiment(inReview,loadModel)
	sentimentpredicted = ""
	if str(predictedVal).strip() == "0":
		sentimentpredicted = "The movie review is bad 😞"
	else:
		sentimentpredicted = "The movie review is good, enjoy.. 😉"
	return render_template('SendSentiment.html', inReview = sentimentpredicted)

if __name__ == "__main__":
    app.run(debug=True)
