from flask import Flask, request, render_template
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import difflib

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Sample FAQs
faq_data = {
    "What are your working hours?": "We are open from 9 AM to 5 PM, Monday to Friday.",
    "What is your refund policy?": "You can request a refund within 30 days of purchase.",
    "How can I contact support?": "You can contact our support team at support@example.com.",
    "Do you offer international shipping?": "Yes, we ship to most countries worldwide."
}

# Preprocess text: tokenize, remove stopwords & punctuation
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    return " ".join(tokens)

# Find the best matching FAQ
def get_best_response(user_question):
    processed_question = preprocess_text(user_question)
    faq_keys = list(faq_data.keys())

    # Find the best match using similarity
    best_match = difflib.get_close_matches(processed_question, faq_keys, n=1, cutoff=0.5)
    
    if best_match:
        return faq_data[best_match[0]]
    else:
        return "Sorry, I couldn't find an answer to your question."

@app.route("/", methods=["GET", "POST"])
def chatbot():
    response = ""
    if request.method == "POST":
        user_input = request.form["question"]
        response = get_best_response(user_input)
    
    return render_template("chatbot.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
