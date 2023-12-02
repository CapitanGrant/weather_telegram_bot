import json
import requests
import time

token = "6823500124:AAGMeVdgX78NyWwQ8I_0xjJHCZp8E7GAE7g"
masas = []


def save_update_ip(masas):
    with open('update_ip.json', 'w', encoding='utf-8') as file:
        json.dump(masas, file)


def load_update_ip():
    with open('update_ip.json', 'r', encoding='utf-8') as file:
        return json.load(file)


masas = load_update_ip()

while True:
    res = requests.get("https://api.telegram.org/bot" + token + "/getUpdates")
    j = json.loads(res.text)
    for i in j['result']:
        update_id = i['update_id']
        if update_id not in masas:
            print(update_id)
            masas.append(update_id)
            save_update_ip(masas)
            chat_id = i['message']['chat']['id']
            from_first_name = i['message']['from']['first_name']
            if 'text' in i['message']:
                text = i['message']['text']
                if text == '/start':
                    url = "https://source.unsplash.com/random/200x200?sig=1"
                    res = requests.get(
                        'https://api.telegram.org/bot' + token + '/sendPhoto?&chat_id=' + str(
                            chat_id) + '&photo=' + url)
                if text == "/msc":
                    fp = open('Boulevard Depo - Angry toyS.mp3', 'rb')
                    files = {'audio': fp}
                    req = requests.post(
                        'https://api.telegram.org/bot' + token + '/sendAudio?&chat_id=' + str(
                            chat_id), files=files)
                    # res = requests.get(
                    #     'https://api.telegram.org/bot' + token + '/sendMessage?&chat_id=' + str(
                    #         chat_id) + '&text=Аудио отправлено')
                    print(req.text)
    time.sleep(2)
'Boulevard Depo - Angry toyS.mp3'
