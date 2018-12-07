#!/usr/bin/python

import requests

response = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})

jokeStr = str(response.json()["joke"])

audio = requests.get("http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=\"" + jokeStr + "\"&tl=en")

with open("new.mp3", "wb") as hdl:
  for block in audio.iter_content(1024):
    hdl.write(block)
