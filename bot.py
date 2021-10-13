import os, requests 
from dotenv import load_dotenv
from pandas import DataFrame, read_json
from discord.ext import commands


load_dotenv()

# get API keys from environment variables
disc_key = os.getenv("DISCORD_KEY")
dict_key = os.getenv("DICT_KEY")
thes_key = os.getenv("THES_KEY")
thes_url = "https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{}?key={}"
dict_url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/{}?key={}"

# the main function that will handle user requests
def request_word(word, url, key):
    response = []
    raw = str(requests.get(url.format(word, key)).text)

    json_data = read_json(raw)

    df = DataFrame(json_data)
    try:
        for definition in df['shortdef']:
            for part in definition:
                response.append(part)
            response.append("\n")

    except:
        try:
            for index in df.index:
                response.append(f"Did you mean {df[0][index]}?")
        except:
            response.append("Merriam-Webster has no entry for this word.")
    return response


# start of the bot-related code
client = commands.Bot(command_prefix = "#")
@client.command(pass_context = True)
async def define(ctx, word):
    for response in request_word(word, dict_url, dict_key):
        await ctx.channel.send(response)


client.run(disc_key)
