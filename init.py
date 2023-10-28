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
