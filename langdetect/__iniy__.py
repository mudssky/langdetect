from langdetect import LangDetector
__langDector = LangDetector()

print('hello')


def detect(text):
    return __langDector.detect(text)
