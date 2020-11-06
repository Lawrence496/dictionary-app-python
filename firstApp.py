import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? \nEnter Y if Yes, N if No: " % get_close_matches(word, data.keys())[0])
        if yn == "Y" or "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or "n":
            return "The word doesn't exist."
        else:
            return "We don't understand your entry."
    else:
        return "The word doesnt exist. Double check!!"

word = input("Enter a word: ")

print(translate(word))

