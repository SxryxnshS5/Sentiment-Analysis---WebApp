from transformers import pipeline

task = "text-classification"
model_id = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

classifier = pipeline(task, model_id)

def getResult(text):
    result = classifier(text)
    return result