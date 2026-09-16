from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if sys.argv[1] != "-f" and sys.argv[1] != "--font" or sys.argv[2] not in figlet.getFonts():
    print("Invalid usage")
    sys.exit(1)

text = input("Input: ")

if len(sys.argv) == 1:
    font_name_random = random.choice(figlet.getFonts())
    figlet.setFont(font = font_name_random)
    print(figlet.renderText(text))


elif len(sys.argv) == 3:
    font_name = str(sys.argv[2])
    figlet.setFont(font = font_name)

    print(figlet.renderText(text))

else:
    print("Error")