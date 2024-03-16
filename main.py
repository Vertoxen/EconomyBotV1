import settings
import discord
from discord.ext import commands


def run():
    intents = discord.Intents.default()

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print("__________________________")
        print(bot.user.name)
        print(bot.user.id)
        print("__________________________")

    bot.run(settings.DISCORD_SECRET)


if __name__ == '__main__':
    run()
