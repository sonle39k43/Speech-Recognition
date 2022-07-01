import os
from google.cloud import speech_v1p1beta1 as speech
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_service_key.json'

client = speech.SpeechClient()
speech_file = "17-06-2022 11 58 26.wav"
with open(speech_file, "rb") as audio_file:
    content = audio_file.read()

audio = speech.RecognitionAudio(content=content)

diarization_config = speech.SpeakerDiarizationConfig(
    enable_speaker_diarization=True,
    min_speaker_count=2,
    max_speaker_count=10,
)
media_uri = "gs://speech-to-text1705/17-06-2022 11 58 26.wav"
long_audi_wav = speech.RecognitionAudio(uri=media_uri)

config = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    language_code="vi-VN",
    diarization_config=diarization_config,
)
print("Vui lòng chờ...")
response = client.recognize(config=config, audio=long_audi_wav)
print(response)
result = response.results[-1]

#
words_info = result.alternatives[0].words
print(words_info)

# Printing out the output:
for word_info in words_info:
    print(
        u"Từ: '{}', speaker_tag: {}".format(word_info.word, word_info.speaker_tag)
    )
