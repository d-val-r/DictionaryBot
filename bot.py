import os, requests 
from dotenv import load_dotenv
from pandas import DataFrame, read_json
from discord.ext import commands


load_dotenv()

dict_key = os.getenv("DICT_KEY")
thes_key = os.getenv("THES_KEY")
disc_key = os.getenv("DISCORD_KEY")

client = commands.Bot(command_prefix = "#")

def request_def(word):
    response = []
    try:
        raw = str(requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={dict_key}").text)

        json_data = read_json(raw)

        df = DataFrame(json_data)

        for definition in df['shortdef']:
            for part in definition:
                response.append(part)
            response.append("\n")
            
    except:
        response.append("Merriam-Webster has no entry for this word.")
    return response


@client.command(pass_context = True)
async def define(ctx, word):
    for response in request_def(word):
        await ctx.channel.send(response)


client.run(disc_key)
