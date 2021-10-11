import os, requests 
from dotenv import load_dotenv
from pandas import DataFrame, read_json


load_dotenv()

dict_key = os.getenv("DICT_KEY")
thes_key = os.getenv("THES_KEY")
word = input("enter a word: ")

try:
    raw = str(requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={dict_key}").text)


    json_data = read_json(raw)

    df = DataFrame(json_data)

    for definition in df['shortdef']:
        for parts in definition:
            print(parts)
        print("\n\n", end="")
except:
    print("Merriam-Webster has no entry for this word.")
