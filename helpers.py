import glob
import subprocess
from time import sleep

ROM_NAME = glob.glob("*.gba")[0].strip().strip(".gba")


def press_a():
    print("Pressing A")
    psd = subprocess.Popen(["echo", "keydown z"], stdout=subprocess.PIPE)
    psu = subprocess.Popen(["echo", "keyup z"], stdout=subprocess.PIPE)
    subprocess.run(["dotoolc"], stdin=psd.stdout, check=True)
    sleep(0.5)
    subprocess.run(["dotoolc"], stdin=psu.stdout, check=True)


def hold_a():
    print("Holding A")
    psd = subprocess.Popen(["echo", "keydown z"], stdout=subprocess.PIPE)
    subprocess.run(["dotoolc"], stdin=psd.stdout, check=True)


def release_a():
    print("Releasing A")
    psu = subprocess.Popen(["echo", "keyup z"], stdout=subprocess.PIPE)
    subprocess.run(["dotoolc"], stdin=psu.stdout, check=True)


def press_b():
    print("Pressing B")
    psd = subprocess.Popen(["echo", "keydown x"], stdout=subprocess.PIPE)
    psu = subprocess.Popen(["echo", "keyup x"], stdout=subprocess.PIPE)
    subprocess.run(["dotoolc"], stdin=psd.stdout, check=True)
    sleep(0.5)
    subprocess.run(["dotoolc"], stdin=psu.stdout, check=True)


def press_u():
    print("Pressing W")
    psd = subprocess.Popen(["echo", "keydown w"], stdout=subprocess.PIPE)
    psu = subprocess.Popen(["echo", "keyup w"], stdout=subprocess.PIPE)
    subprocess.run(["dotoolc"], stdin=psd.stdout, check=True)
    sleep(0.5)
    subprocess.run(["dotoolc"], stdin=psu.stdout, check=True)


def press_l():
    print("Pressing A")
    psd = subprocess.Popen(["echo", "keydown a"], stdout=subprocess.PIPE)
    psu = subprocess.Popen(["echo", "keyup a"], stdout=subprocess.PIPE)
    subprocess.run(["dotoolc"], stdin=psd.stdout, check=True)
    sleep(0.5)
    subprocess.run(["dotoolc"], stdin=psu.stdout, check=True)


def press_d():
    print("Pressing A")
    psd = subprocess.Popen(["echo", "keydown s"], stdout=subprocess.PIPE)
    psu = subprocess.Popen(["echo", "keyup s"], stdout=subprocess.PIPE)
    subprocess.run(["dotoolc"], stdin=psd.stdout, check=True)
    sleep(0.5)
    subprocess.run(["dotoolc"], stdin=psu.stdout, check=True)


def press_r():
    print("Pressing A")
    psd = subprocess.Popen(["echo", "keydown d"], stdout=subprocess.PIPE)
    psu = subprocess.Popen(["echo", "keyup d"], stdout=subprocess.PIPE)
    subprocess.run(["dotoolc"], stdin=psd.stdout, check=True)
    sleep(0.5)
    subprocess.run(["dotoolc"], stdin=psu.stdout, check=True)


def press_m():
    print("Pressing Start")
    psd = subprocess.Popen(["echo", "keydown m"], stdout=subprocess.PIPE)
    psu = subprocess.Popen(["echo", "keyup m"], stdout=subprocess.PIPE)
    subprocess.run(["dotoolc"], stdin=psd.stdout, check=True)
    sleep(0.5)
    subprocess.run(["dotoolc"], stdin=psu.stdout, check=True)


def press_n():
    print("Pressing Select")
    psd = subprocess.Popen(["echo", "keydown n"], stdout=subprocess.PIPE)
    psu = subprocess.Popen(["echo", "keyup n"], stdout=subprocess.PIPE)
    subprocess.run(["dotoolc"], stdin=psd.stdout, check=True)
    sleep(0.5)
    subprocess.run(["dotoolc"], stdin=psu.stdout, check=True)


def take_screenshot():
    print("Taking screenshot")
    ps = subprocess.Popen(["echo", "key f12"], stdout=subprocess.PIPE)
    subprocess.run(["dotoolc"], stdin=ps.stdout, check=True)

    sleep(0.5)
    files = glob.glob("*.png")
    nums = [int(x.replace(ROM_NAME, "").strip("-.png")) for x in files]
    latest = max(nums)
    ss = f"{ROM_NAME}-{latest}.png"
    return ss


def start_game_menu():
    sleep(2)
    press_a()
    sleep(8)
    press_a()
    sleep(3)
    press_a()

    print("Opening passed!")


def pre_game():
    start_game_menu()

    print("Starting Professor scene!")
    hold_a()
    for _ in range(20):
        sleep(2)
        press_b()
        release_a()

    print("Selecting Character")

    sleep(10)

    # select Male Character
    press_a()
    sleep(8)
    press_a()
    sleep(3)

    # type out ASH
    press_a()

    for _ in range(3):
        press_d()
        for _ in range(6):
            press_r()
            press_a()
            for _ in range(5):
                press_l()
                press_u()
                press_a()

    press_m()
    press_a()

    sleep(2)
    press_a()

    hold_a()
    for _ in range(10):
        sleep(2)
        press_b()
        release_a()
