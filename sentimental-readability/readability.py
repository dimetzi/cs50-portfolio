# TODO
from cs50 import get_string

text = get_string("Text: ")
word = 1
letter = 0
sentence = 0

for c in text:
    if c.isalpha():
        letter += 1
    elif c == " ":
        word += 1
    elif c == "." or c == "!" or c == "?":
        sentence += 1

L = letter / word * 100
S = sentence / word * 100
index = round(0.0588 * L - 0.296 * S - 15.8)
if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
