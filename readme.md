# 💬 Sentiment Analysis Web App

A fully functional *Sentiment Analysis Platform* that allows users to input text and receive immediate feedback on whether the sentiment is *Positive, **Neutral, or **Negative. This project leverages the power of Hugging Face Transformers and is built using **Flask* as the backend.

> 🏆 This project was built as part of a *Hackathon organized by CSVTU Bhilai*.

<p align="center">
  <img src="images/Image 1.jpg" alt="App Demo" width="700"/>
  <img src="images/Image 2.jpg" alt="App Demo" width="700"/>
  <img src="images/Image 3.jpg" alt="App Demo" width="700"/>
  <img src="images/Image 4.jpg" alt="App Demo" width="700"/>
  <img src="images/Image 5.jpg" alt="App Demo" width="700"/>
  <img src="images/Image 6.jpg" alt="App Demo" width="700"/>
</p>

---

## ✨ Key Features

- 🎯 Real-time sentiment analysis using a fine-tuned *RoBERTa* model  
- 🧠 Confidence score to reflect model certainty  
- 🧵 Clean and responsive web interface  
- 📊 Designed for analyzing reviews, tweets, feedback, and comments  

---

## 📑 Table of Contents

- [System Architecture](#-system-architecture)  
- [Front-end](#-front-end)  
- [Back-end](#-back-end)  
- [Model](#-model)  
- [API Design](#-api-design)  
- [Use Cases](#-use-cases)  
- [Future Enhancements](#-future-enhancements)  

---

## 🏗 System Architecture

The application follows a *client-server* architecture:
- *Front-end*: HTML + Bootstrap + Jinja templates for dynamic rendering  
- *Back-end*: Flask application using the Hugging Face transformers library for prediction  
- *Model*: A fine-tuned RoBERTa model hosted locally for low-latency inference  

---

## 🎨 Front-end

The UI is built using *HTML, **Bootstrap, and **Jinja2* for rendering dynamic content.

### 🖥 Pages

- *Home Page*: Text area to input sentence(s)  
- *Result Page*: Displays sentiment class and model confidence  

### 🧰 Tools & Libraries

- HTML5  
- Bootstrap 5  
- Jinja2  

---

## ⚙ Back-end

The backend uses *Flask* to serve the UI and handle requests between the model and the interface.

### 🔧 Features

- RESTful POST route for text analysis  
- Softmax-based classification  
- JSON-based internal routing  

### 🛠 Libraries

- Flask  
- Transformers (by Hugging Face)  
- PyTorch  
- Regex, NumPy  

---

## 🤖 Model

> *Model Name*: [cardiffnlp/twitter-roberta-base-sentiment](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)

- *Base*: RoBERTa  
- *Classes*:  
  - Negative  
  - Neutral  
  - Positive  
- *Specialty*: Optimized for short-form content like tweets, messages, and comments  

---

## 🔌 API Design

The app follows a simple RESTful API design:

| Method | Route        | Description                      |
|--------|--------------|----------------------------------|
| GET    | /          | Load homepage                    |
| POST   | /analyze   | Analyze submitted text for sentiment |

- Results are passed using *Flask session objects* and *Jinja rendering*

---

## 📌 Use Cases

- 🛍 *Customer Feedback Analysis*  
  Analyze product reviews from platforms like Amazon or Flipkart to measure customer satisfaction.

- 🧵 *Social Media Monitoring*  
  Track and assess sentiment on Twitter, Facebook, or Instagram posts to manage brand reputation.

- 📰 *News Sentiment Classification*  
  Classify article headlines or summaries to detect tone and potential political bias.

- 🎓 *Educational Projects*  
  Ideal starter for NLP-focused student projects, hackathons, or mini-projects.

- 🧪 *Product Review Aggregator*  
  Automatically summarize thousands of user reviews into positive, negative, and neutral trends.

- 📢 *Opinion Mining for Surveys*  
  Detect emotional tone from open-ended survey responses for better insights.

- 🤖 *Chatbot Emotion Detection*  
  Enable emotion-aware responses in chatbots based on detected sentiment.

---

## 🌱 Future Enhancements

- 📈 Add a sentiment graph for visualizations  
- 🗂 Upload CSV or text files for batch sentiment analysis  
- 🌐 Add multilingual support using XLM-R  
- 💬 Integrate with WhatsApp or Slack via API  
- 🔐 User login + sentiment history storage  

---

> Built with ❤ by *TLE Smashers* as part of a Hackathon organized by *CSVTU Bhilai*.