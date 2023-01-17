import pywhatkit as kit
import wikipedia
import time 
import pyautogui
import requests
from pynput.keyboard import Key, Controller

keyboard = Controller()

wikipedia.set_lang("es")

def buscar_en_google(query):
    kit.search(query)

def buscar_en_wikipedia(query):
    results = wikipedia.summary(query, sentences=4)
    return results

def poner_en_yt(video):
    kit.playonyt(video)

def mandar_was(number, message):
    try:
        kit.sendwhatmsg_instantly(f"+34{number}", message)
        time.sleep(10)
        pyautogui.click()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))

def buscar_en_internet(info, nlineas):
    try:
        return kit.info(info, lines=nlineas)
    except Exception as e:
        print(str(e))

def chiste_random():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def tiempo_grafico(ciudad):
    url = f"https://wttr.in/{ciudad}"

    res = requests.get(url)
    print(res.text)

def tiempo(ciudad):
    url = f"https://es.wttr.in/{ciudad}?format=j1"
    res = requests.get(url)
    weather_dic = res.json()
    #parámetros q queira devolver
    temp_c = weather_dic['current_condition'][0]['temp_C']
    desc_temp_C = weather_dic['current_condition'][0]['lang_es'][0]['value']
    return temp_c, desc_temp_C