import os
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_service_key.json'
speech_client = speech.SpeechClient()

media_file_name_wav = "17-06-2022 11 58 26.wav"

with open(media_file_name_wav, 'rb') as f1:
    byte_data_wav = f1.read()
audio_wav = speech.RecognitionAudio(content=byte_data_wav)

config_wav = speech.RecognitionConfig(
    sample_rate_hertz = 48000,
    enable_automatic_punctuation=True,
    language_code = 'vi-VN',
    audio_channel_count=2
)
#
# response_standard_wav = speech_client.recognize(
#     config = config_wav,
#     audio = audio_wav
# )
#
# print(response_standard_wav)

## Transcribing a long media file
media_uri = "gs://speech-to-text1705/17-06-2022 11 58 26.wav"
long_audi_wav = speech.RecognitionAudio(uri=media_uri)

config_wav_enhanced = speech.RecognitionConfig(
    sample_rate_hertz = 48000,
    enable_automatic_punctuation=True,
    language_code = 'vi-VN',

)

operations = speech_client.long_running_recognize(
    config = config_wav_enhanced,
    audio = long_audi_wav
)
response = operations.result(timeout=90)
for result in response.results:
    print(result.alternatives[0].transcript)
    print(result.alternatives[0].confidence)
    print()