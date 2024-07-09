from deep_translator import GoogleTranslator


translator_en_kr = GoogleTranslator(source='en', target='korean')
translator_kr_en = GoogleTranslator(source='korean', target='en')


def translate_en_kr(message):
    return translator_en_kr.translate(message)


def translate_kr_en(message):
    return translator_kr_en.translate(message)


print(translate_en_kr("hello"))
print(translate_kr_en("감사합니다"))

