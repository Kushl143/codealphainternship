from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    translator = Translator()
    input_lang = request.form['input_lang']
    text = request.form['text']
    output_lang = request.form['output_lang']

    translated_text = translator.translate(text, src=input_lang, dest=output_lang).text
    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
