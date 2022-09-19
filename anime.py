import os
import requests
import re

animehtml = "./templates/anime.html"
imgdir = "./img/anime/"


temp1 = """{% extends "base.html" %}
<link rel="stylesheet" href="anime.css">
<div class="gallery">
"""

temp2 = """</div>
</body>
</html>
"""

def create():
    contents = os.listdir(imgdir)
    with open(animehtml, "w") as f:
        f.write(temp1) 
        for i in contents:
            h = re.sub(r"\..*", "", i)
            foo = '<div class="container"> <img src="../img/anime/'+i+'"><div class="text">'+h+'</div></div>\n'
            f.write(foo)
        f.write(temp2)


def main():

    url = "https://kitsu.io/api/edge/anime"
    name = [
        "Hajime no Ippo",
        "Code Geases",
        "Sekai Saikou no Ansatsusha, Isekai Kizoku ni Tensei suru",
        "saenai-heroine-no-sodatekata",
        "Violet Evergreen",
        "evangelion",
        "Dakara Boku wa, H ga Dekinai",
        "KonoSuba",
        "Miss Kobayashi's Dragon Maid",
        "Grand-Blue",
        "sword art online",
        "Girlfriend Girlfriend.",
        "Black Cover",
        "Komi-san wa, Comyushou desu",
        "Yancha Gal no Anjou san",
        "Horimiya",
        "Ichigo",
        "Kitachi",
        "Domestic girlfriend",
        "Anohana",
        "vampire knight",
        "hunter x hunter",
        "Dragon Ballz",
        "Naruto",
        "Bleach",
        "Kakeguri",
        "tsucmuchi moonlit fantasy season1",
        "Re:zero",
        "Masamune-kun's Revenge ep6",
        "Gangsta",
        "Kaguya-sama love is war",
        "High School Dxd",
        "God of Highschool",
        "The Devil is a Part-timer",
        "Classroom of elite",
        "The Melancholy of Haruhi Suzumiy",
        "Kaichou wa maid-Sama",
        "Death Note",
        "The misfit if demon academy",
        "Charlotte",
        "tokyo ghoul",
        "Cowboy Beebop"
]
    headers = {
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json'
    }
    for i in name:
        print(i)
        params = {
                'page[limit]':  1,
                'page[offset]': 0,
                'filter[text]': i
                }
        
        re = requests.get(url, headers=headers, params=params)
        resp = re.json()
        img = resp['data'][0]['attributes']['posterImage']['original']
        try:
            title = resp['data'][0]['attributes']['titles']['en']
        except:
            title = i
        types = resp['data'][0]['type']
        save_file = "./img/" + types + "/" + title
        with open(save_file, 'bw') as f:
            f.write(requests.get(img).content)
        create()


if __name__ == '__main__':
    main()
