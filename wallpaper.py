#!/usr/bin/python3
import requests


res = requests.get("https://picsum.photos/2500")
with open("/home/lee/.local/share/backgrounds/background.jpg", "wb") as bg:
    bg.write(res.content)

