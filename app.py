import os
import subprocess
from time import sleep
from typing import TypedDict

import dotenv
import google.generativeai as genai
from PIL import Image

from helpers import hold_a, press_a, press_b, press_d, press_l, press_r, press_u, release_a, take_screenshot

API_KEY = dotenv.get_key(dotenv.find_dotenv(), "API_KEY")
ROM_PATH = "./Pokemon - Emerald Version (USA, Europe).gba"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp")


class Move(TypedDict):
    buttons: list[str]
    description: str


PROMPT = """
Welcome, you are an awesome Pokémon Games player. You have an amazing experience of playing all kinds of early Pokémon games, including
Red, Blue, Yellow, Gold, Silver, Crystal, Ruby, Sapphire, Emerald and all others. Today you will be playing Pokémon Emerald.
It's an awesome Pokémon game filled with adventures, don't you agree? You will receive the current status of the game in a screenshot.
You have to respond with the button to be pressed in order to progress further in the game. Think and make decisions responsibly!
Build up a great team and make up to the elite four.

For each screenshot you recieve, you need to respond with the list of button presses needed to complete the objective currently on-screen
and also a description of the actions performed. Respond in JSON only. Return an object containing a key called `button` with the array of buttons to press,
and a key called `description` with the description of the move. Contain as much key presses as possible in one screenshot. DO NOT return anything else.
Don't use markdown syntax, only JSON.

Valid Buttons are: a, b, u, d, l, r
i.e. A, B, Up, Down, Left, Right

Use this JSON schema:

Move = {'buttons': list[str], 'description': str}
Return: Move
""".strip()

playing = True
subprocess.Popen(["mgba-qt", ROM_PATH], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

chat = model.start_chat()
response = chat.send_message([PROMPT])

for i in range(5, -1, -1):
    print(f"Starting Gameplay control in {i} seconds")
    sleep(1)

print("Spawing dotoold in background")
os.system("dotoold &")

while playing:
    print(response.text)
    print()

    sleep(2)
    press_a()
    sleep(8)
    press_a()
    sleep(3)
    press_a()

    print("Opening passed!")
    print("Starting Professor scene!")

    hold_a()
    for _ in range(20):
        sleep(2)
        press_b()
    release_a()

    print("Selecting Character")

    sleep(8)

    # ask gemini for character
    # press keys
    #
    # take screenshot
    img_path = take_screenshot()

    response = chat.send_message(
        Image.open(img_path), generation_config=genai.GenerationConfig(response_mime_type="application/json", response_schema=Move)
    )

    print(response)

    for button in response["buttons"]:
        match button.lower():
            case "a":
                press_a()
            case "b":
                press_b()
            case "u":
                press_u()
            case "d":
                press_d()
            case "l":
                press_l()
            case "r":
                press_r()

    sleep(500)
