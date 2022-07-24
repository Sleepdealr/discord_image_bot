import discord
import get_images
import json

client = discord.Client()

with open("config.json", "r") as f:
    CONFIG = json.load(f)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    images = get_images.main()
    while images is None:
        images = get_images.main()
    impath, source  = images
    with open(impath, "rb") as img:
        await client.get_channel(CONFIG["channelid"]).send(content="Source=<{}>".format(source),file=discord.File(img))
        print("{}======{}".format(impath,source))
    get_images.logging.info("Posted to discord.")
    exit()

client.run(CONFIG["discordapi"])

