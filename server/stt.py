import os
import assemblyai as aai
from flask import jsonify
import medai as mai



def data():
    aai.settings.api_key = "97ad5eac2a1a4f6a8bcd363bd712808e"
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/espn-bears.m4a")
        
    print(transcript.text)
    return jsonify({
        'message': transcript.text
    })
