import os
from dotenv import load_dotenv

load_dotenv()

dict_key = os.getenv("DICT_KEY")
thes_key = os.getenv("THES_KEY")

print(dict_key, thes_key)
