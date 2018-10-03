import json
from bs4 import BeautifulSoup


if __name__ == '__main__':
    print(__name__)

    data = ""
    try:
        file = open('full-emoji-list.html')
        data = file.read()
    except Exception as e:
        print(e)
    finally:
        file.close()

    obj = BeautifulSoup(data, 'lxml')
    trs = obj.find_all('tr')
    emoji_list = []
    for tr in trs:
        char = tr.find('td', class_='chars')
        if char == None:
            continue
        emoji_list.append({
            "emojiChar": "",
            "emoji": char.text,
            "description": tr.find('td', class_='name').text,
            "aliases": [],
            "tags": []
        })
    print(len(emoji_list))
    with open('temp.json', 'w') as outfile:
        json.dump(emoji_list, outfile)
