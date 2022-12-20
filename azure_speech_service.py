# azure_speech_service.py


import azure.cognitiveservices.speech as speechsdk
import os

from line_chatbot_api import *

# (Resource Management -> Keys and Endpoint -> Key 1 or Key 2, Location/Region) subscription key and region for speech service
speech_config = speechsdk.SpeechConfig(subscription="1f847fd8beac4fa88e7f261f93407fae", region="eastus")
speech_config.speech_recognition_language = "zh-TW"

def message_to_wav(message_content, filename_wav):
    filename_mp3 = 'temp_audio.mp3'
    with open(filename_mp3, 'wb') as fd:
        for chunk in message_content.iter_content():
            fd.write(chunk)
    # -i : set input file name, -y : overwrite output file if it exists, -loglevel quiet : suppress ffmpeg log output
    os.system(fr'/Users/williamyen/Desktop/Github/AI_FinalProject_Group9/ffmpeg -y -i {filename_mp3} {filename_wav} -loglevel quiet')

def transcribe_from_file(filename_wav):
    audio_input = speechsdk.AudioConfig(filename = filename_wav)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config = speech_config, audio_config = audio_input)
    result = speech_recognizer.recognize_once_async().get()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print(f"No speech could be recognized: {result.no_match_details}")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Speech Recognition canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {cancellation_details.error_details}")
            print("Did you set the speech resource key and region values?")
    return "transcribe error"

