# encoding: utf-8

import requests
import re
import time
from bs4 import BeautifulSoup


def get_color():

    color_option = input("\nDo you want your painting in color? \n\x1b[5m->\x1b[25m ")
    color_option = color_option.lower().strip()
    if color_option == "y" or color_option == "yes":
        color = "color"
        return color
    else:
        color = "mono"
        return color


def get_ascii(color_response, image_link):
    ascii_generator = "https://www.ascii-art-generator.org/"

    website_data = {
        "art_type": color_response,
        "userfile": "(binary)",
        "userfile_url": image_link,
        "banner_text": "",
        "outFormat_caca": "utf8",
        "figlet_font": 0,
        "width": 150,
        "banner_width": 150,
        "user_screen_width": 150,
    }

    r = requests.post(ascii_generator, data=website_data)
    soup = BeautifulSoup(r.text, "html.parser")
    script = [
        script.text for script in soup.find_all("script") if "var url" in script.text
    ][0]
    name = re.search(r"name=(\w*)", script).group(1)
    now = int(time.time())
    # https://
    check_url = "https://www.ascii-art-generator.org/FW/result.php"
    params = {"name": name, "tscachebusttamp": now}
    check = "__wait__123"
    while check == "__wait__123":
        check = requests.get(check_url, params=params).text
        time.sleep(3)
        # print("checked")

    check_soup = BeautifulSoup(check, "html.parser")
    art_link = "https://www.ascii-art-generator.org" + check_soup.find("a")["href"]

    art = requests.get(art_link)
    with open("art.txt", "wb") as code:
        code.write(art.content)
        print("\nYour masterpiece is done!")
