from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    frenchText = translator.englishToFrench(textToTranslate)
    return frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    englishText = translator.frenchToEnglish(textToTranslate)
    return englishText

@app.route("/englishToUrdu")
def englishToUrdu():
    textToTranslate = request.args.get('textToTranslate')
    urduText = translator.englishToUrdu(textToTranslate)
    return urduText

@app.route("/urduToEnglish")
def urduToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    englishText = translator.urduToEnglish(textToTranslate)
    return englishText

@app.route("/speechToText", methods=["POST"])
def speech_to_text():
    audio_file = request.files['audio']
    recognized_text = translator.speechToText(audio_file)
    return recognized_text

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

