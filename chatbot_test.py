import asyncio
import random  # random 모듈 추가
from chatbot import Chat, register_call
import os
import requests
import wikipedia
import python_weather
import warnings
warnings.filterwarnings("ignore")

@register_call("do_you_know")
def do_you_know(session=None, query=None):
    return "I do not know about " + query

@register_call("weather")
def call_weather(session=None, city='New York'):
    global weather_string
    try:
        if os.name == 'nt':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(get_weather())
    except Exception:
        weather_string = "I do not know the weather"
    return weather_string

weather_string = None

async def get_weather(city='New York'):
    global weather_string
    async with python_weather.Client() as client:
        weather = await client.get(city)
        await client.close()
    weather_string = ""
    for hourly in list(weather.daily_forecasts)[0].hourly_forecasts:
        weather_string = weather_string + str(hourly.time) + " " + str(hourly.temperature) + " deg.C " + str(hourly.description) + "\n"

@register_call("wiki")
def who_is(session=None, query='South Korea'):
    try:
        return wikipedia.summary(query)
    except Exception:
        pass
    return "I don't know about "+query
    

horoscopes = [
    "오늘은 좋은 일이 생길 것입니다.",
    "주의해야 할 일이 있을 수 있습니다.",
    "건강에 유의하세요.",
    "사랑운이 좋은 날입니다.",
    "금전운이 강화된 날입니다.",
    "새로운 기회가 찾아올 것입니다.",
    "친구와의 관계가 좋아질 것입니다.",
    "중요한 결정을 내리기에 좋은 날입니다.",
    "스트레스를 피하고 휴식을 취하세요.",
    "창의력이 넘치는 날입니다.",
    "오늘은 당신의 노력이 결실을 맺을 것입니다.",
    "사람들과의 협력이 중요한 날입니다.",
    "예상치 못한 행운이 찾아올 것입니다.",
    "자기 자신을 믿으세요.",
    "작은 일에도 감사하는 마음을 가지세요.",
    "새로운 것을 시도해보세요.",
    "오늘은 휴식을 취하는 것이 좋습니다.",
    "주변 사람들에게 친절을 베푸세요.",
    "직장에서 좋은 평가를 받을 것입니다.",
    "계획했던 일이 순조롭게 진행될 것입니다.",
    "감정을 잘 조절하는 것이 중요합니다.",
    "목표를 향해 꾸준히 나아가세요.",
    "오늘은 자신감을 가지고 행동하세요.",
    "좋은 소식이 당신을 기다리고 있습니다.",
    "재능을 발휘할 수 있는 기회가 생길 것입니다.",
    "오늘은 모험을 즐겨보세요.",
    "가족과 시간을 보내는 것이 좋습니다.",
    "지출을 조심하세요.",
    "긍정적인 태도가 중요한 날입니다.",
    "오늘은 인내심을 발휘해야 합니다."
]


@register_call("horoscope")
def get_horoscope(session=None):
    try:
        return random.choice(horoscopes)
    except Exception:
        return "I don't know the general horoscope for today"

first_question = "Hi, how are you?"
chat = Chat(os.path.join(os.path.dirname(os.path.abspath(__file__)), "chatbot_test.template"))
chat.converse(first_question)