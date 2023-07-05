
import assemblyai as aai


def data(url):
    aai.settings.api_key = "97ad5eac2a1a4f6a8bcd363bd712808e"
    transcriber = aai.Transcriber()

    transcript = transcriber.transcribe(url)
    return transcript.text