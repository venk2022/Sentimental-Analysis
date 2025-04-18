from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import torch
import numpy as np

app = Flask(__name__)

# Load model and tokenizer
model_name = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
labels = ['NEGATIVE', 'NEUTRAL', 'POSITIVE']

# Create custom sentiment analyzer
def analyze_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.nn.functional.softmax(logits, dim=1)[0]
    label_index = torch.argmax(probs).item()
    return {
        "label": labels[label_index],
        "score": float(probs[label_index])
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == "POST":
        input_text = request.form["inputtext_"]
        sentiment_result = analyze_sentiment(input_text)
        print(f"Input: {input_text}")
        print(f"Result: {sentiment_result}")

    return render_template("output.html", data={
        "sentiment": sentiment_result["label"],
        "score": round(sentiment_result["score"], 3),
        "input_text": input_text
    })

if __name__ == "__main__":
    app.run(port=8000)
