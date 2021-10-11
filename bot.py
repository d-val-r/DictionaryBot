import os, requests
from dotenv import load_dotenv

load_dotenv()

dict_key = os.getenv("DICT_KEY")
thes_key = os.getenv("THES_KEY")
word = input("enter a word: ")

raw = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={dict_key}")

response = raw.json()

print(response)
