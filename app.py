import json
import os
import subprocess
from time import sleep
from typing import TypedDict

import dotenv
import google.generativeai as genai
from PIL import Image

from helpers import pre_game, press_a, press_b, press_d, press_l, press_m, press_n, press_r, press_u, start_game_menu, take_screenshot

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

Valid Buttons are: a, b, u, d, l, r, m, n
i.e. A, B, Up, Down, Left, Right, Start, Select

Use this JSON schema:

Move = {'buttons': list[str], 'description': str}
Return: Move
""".strip()

playing = True

chat = model.start_chat()
response = chat.send_message([PROMPT])
# print(response.text)

# response = chat.send_message(
#     ["Okay let's start with a test. The picture is in the lab of proff oak with pokeballs in front of the character"],
#     generation_config=genai.GenerationConfig(response_mime_type="application/json", response_schema=Move),
# )

subprocess.Popen(["mgba-qt", ROM_PATH], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

for i in range(5, -1, -1):
    print(f"Starting Gameplay control in {i} seconds")
    sleep(1)

print("Spawing dotoold in background")
os.system("pkill dotoold")
os.system("dotoold &")

# Starting Game
print(response.text)
print()

start_game_menu()

if False:
    # only if new save file
    pre_game()

sleep(5)

while playing:
    print("Starting AI Gameplay Loop".center(50, "*"))
    img_path = take_screenshot()

    print("Asking AI the screenshot....")
    response = chat.send_message(
        Image.open(img_path), generation_config=genai.GenerationConfig(response_mime_type="application/json", response_schema=Move)
    )

    print("Got Response")
    print(response.text)
    print()
    print("Making steps...")

    move = json.loads(response.text)

    for button in move["buttons"]:
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
            case "m":
                press_m()
            case "n":
                press_n()

        sleep(5)

    print("Waiting 15 seconds before next screenshot...")
    print("\n\n")
    sleep(15)
