from flask import Flask, request, render_template
from machinetranslation import translator

app = Flask(__name__)


@app.route('/')
def index():
    """
    Renders the index.html template.
    """
    return render_template('index.html')


@app.route('/englishToFrench', methods=['POST'])
def english_to_french():
    """
    Translates the English text to French.
    """
    english_text = request.form['text']
    french_text = translator.english_to_french(english_text)
    return french_text


@app.route('/frenchToEnglish', methods=['POST'])
def french_to_english():
    """
    Translates the French text to English.
    """
    french_text = request.form['text']
    english_text = translator.french_to_english(french_text)
    return english_text


if __name__ == '__main__':
    app.run()
