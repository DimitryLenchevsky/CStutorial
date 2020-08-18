import requests
import misc
import json

token = misc.token
# https://api.telegram.org/bot1295729088:AAEM0gn6jZdbzgXxv60srIOZM5s5hqRM5Is/sendmessage?chat_id=279594361&text=hi
URL = 'https://api.telegram.org/bot' + token + '/'


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()

    chat_id = data['result'][-1]['message']['chat']['id']
    message_text = data['result'][-1]['message']['text']
    
    message = {'chat_id' : chat_id,
               'text' : message_text}
    return message


def main():
    #d = get_updates()
    
    #with open('updates.json', 'w') as f:
    #    json.dump(d, f, indent=2, ensure_ascii=False)
    get_message()

if __name__ == '__main__':
    main()