from ensurepip import version
import json
from ibm_watson import LanguageTranslatorV3
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikeyforspeech=os.environ['apikeyforspeech']
urlforspeech=os.environ['urlforspeech']
apikeyforlang=os.environ['apikeyforlang']
urlforlang=os.environ['urlforlang']

authenticator=IAMAuthenticator(apikeyforlang)
language_translator=LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(urlforlang)


def englishToFrench(englishText):
    frenchText=language_translator.translate(text=englishText, model_id='en-fr').get_result()
    return frenchText.get('translations')[0].get('translation')

def frenchToEnglish(frenchText):
    englishText=language_translator.translate(text=frenchText, model_id='fr-en').get_result()
    return englishText.get('translations')[0].get('translation')

def englishToUrdu(englishText):
    urduText = language_translator.translate(text=englishText, model_id='en-ur').get_result()
    return urduText.get('translations')[0].get('translation')

def urduToEnglish(urduText):
    englishText = language_translator.translate(text=urduText, model_id='ur-en').get_result()
    return englishText.get('translations')[0].get('translation')

def initialize_speech_to_text():
    authenticator = IAMAuthenticator(apikeyforspeech)
    speech_to_text = SpeechToTextV1(authenticator=authenticator)
    speech_to_text.set_service_url(urlforspeech)
    return speech_to_text

def speechToText(audio_path):
    speech_to_text = initialize_speech_to_text()

    with open(audio_path, 'rb') as audio_file:
        response = speech_to_text.recognize(audio=audio_file, content_type='audio/wav')
        recognized_text = response.get_result()['results'][0]['alternatives'][0]['transcript']

    return recognized_text
