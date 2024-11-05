# Sentiment Analysis Using "distilbert" model

This project is a simple Sentiment Analysis web application built using Flask and Hugging Face's `transformers` library. The application takes user input, analyzes the sentiment, and displays whether the sentiment is positive or negative. This web app is a foundational project to learn the basics of NLP with pretrained models. Future iterations will include a custom fine-tuned model designed specifically for analyzing sentiment in financial news articles.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Usage](#usage)
- [Future Development](#future-development)

## Features

- **Sentiment Analysis**: Uses the `distilbert/distilbert-base-uncased-finetuned-sst-2-english` model to classify text as having positive or negative sentiment.
- **User Input Form**: Provides a simple web interface to input text for sentiment analysis.
- **Flask Integration**: Backend logic powered by Flask, making it easily extendable.
- **Learning-Focused**: Serves as an introductory project for understanding sentiment analysis with Hugging Face and Flask.

## Technologies

- **Python**: Core language for the backend and model integration.
- **Flask**: Web framework used to create the app's backend and route handling.
- **Hugging Face Transformers**: Provides the pretrained DistilBERT model for sentiment analysis.
- **HTML/CSS**: Basic frontend for the form and result display.

## Setup

To run this project locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/sentiment-analysis-web-app.git
    cd sentiment-analysis-web-app
    ```

2. **Install Required Packages**:
    Create a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Install Hugging Face Transformers**:
    ```bash
    pip install transformers
    ```

4. **Run the Application**:
    Start the Flask server:
    ```bash
    flask run
    ```
    The app will be available at [http://localhost:5000](http://localhost:5000).

## Usage

1. Open the app in a web browser at [http://localhost:5000](http://localhost:5000).
2. Enter text in the input form to analyze the sentiment.
3. Submit the form to receive a sentiment analysis result, which will be displayed on a new page.

## Code Overview

### Main Model Code

The app uses a pretrained DistilBERT model fine-tuned for sentiment analysis, loaded through Hugging Face's `transformers` library:

```python
from transformers import pipeline

task = "text-classification"
model_id = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
classifier = pipeline(task, model_id)

def getResult(text):
    result = classifier(text)
    return result
```

### Flask Routes (in `routes.py`)

The app has two main routes:
- **Index Route** (`/`): Displays the input form for the user to enter text.
- **Analyze Route** (`/analyze`): Handles form submissions and displays sentiment analysis results.

```python
from flask import render_template, request
from app import app
from app.service import getResult

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    analysis = getResult(request.form.get('text'))
    return render_template('sentiment_analysis.html', analysis=analysis)
```

## Future Development

This app is a basic learning project to get comfortable with NLP using pretrained models and building web interfaces with Flask. The next step in the project evolution is to develop a custom fine-tuned model focused on analyzing the sentiment of financial news, specifically tailored to predict trends based on the sentiment in financial content.

