import sys
import deeppavlov
import requests
from answers import zapolnenie
from deeppavlov import configs
from deeppavlov import build_model, configs
def bot():
    bot1 = build_model(configs.squad.squad_ru, download=True)
    answers = [[0] * 2 for i in range(13)]
    TOTAL_TEXT = ''
    answers, TOTAL_TEXT = zapolnenie(answers, TOTAL_TEXT)
    s = str(input())
    try:
        result = bot1([TOTAL_TEXT], [s])
        result = str(result[0][0])
        for i in range(13):
            if(result in answers[i][0]):
                print(answers[i][1])
    except:
        print("Ваш запрос некорректен")
bot()