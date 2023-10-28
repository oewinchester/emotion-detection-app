#task 2

from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions


def emotion_detector(text):

  natural_language_understanding = NaturalLanguageUnderstandingV1(
      username='USERNAME',
      password='PASSWORD',
      version='2018-11-16'
  )

  response = natural_language_understanding.analyze(
      text=text,
      features=Features(
          entities=EntitiesOptions(),
          keywords=KeywordsOptions()
      )
  )

  return response['emotion']

print(emotion_detector("I am very happy today."))


#task 3 

def emotion_detector(text):

  # Watson NLP API call

  emotions = response['emotion']

  formatted_emotions = {
    "emotion": [],
    "score": []
  }

  for emotion in emotions:
    formatted_emotions["emotion"].append(emotion['emotion'])
    formatted_emotions["score"].append(emotion['score'])

  return formatted_emotions


formatted = emotion_detector("I am very happy today.")

print(formatted)

#Expected output:

{'emotion': ['joy'], 'score': [0.9541666666666666]}


#task 4
#Create the package folder structure:
#emotion-app/
#   __init__.py
 #  detectors/
  #    __init__.py
   #   emotion.py

#emotion-app/init.py:
__version__ = '1.0'

#emotion-app/detectors/init.py:

from .emotion import detect_emotions
# detectors/emotion.py

from watson_developer_cloud import NaturalLanguageUnderstandingV1

def detect_emotions(text):
  # emotion detection logic 

  return formatted_emotions

from emotion_app.detectors import detect_emotions

detect_emotions("test text")
