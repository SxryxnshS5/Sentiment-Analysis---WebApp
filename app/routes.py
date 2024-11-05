from flask import render_template, request, redirect, url_for
from app import app  # Import the app instance
from app.service import getResult

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    analysis = getResult(request.form.get('text'))

    # Render the analysis in the profile assessment template
    return render_template('sentiment_analysis.html', analysis=analysis)
