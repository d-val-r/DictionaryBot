import os, requests, pandas
from dotenv import load_dotenv


load_dotenv()

dict_key = os.getenv("DICT_KEY")
thes_key = os.getenv("THES_KEY")
word = input("enter a word: ")

raw = str(requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={dict_key}").text)


json_data = pandas.read_json(raw)

df = pandas.DataFrame(json_data)


