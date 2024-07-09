import wikipedia
import os
import warnings
warnings.filterwarnings("ignore")


def who_is(session=None, query='South Korea'):
    try:
        return wikipedia.summary(query)
    except Exception:
        pass
    return "I don't know about "+query


print(who_is())
