import aiohttp
from time import strftime, gmtime

import discord
from discord.ext import commands

import config
from extensions.checks import is_tester


class Testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @is_tester()
    async def notes(self, ctx):
        """Returns current testing notes"""
        author = ctx.author
        log_channel = self.bot.get_channel(config.DISCORD_NOTES_CHANNEL_ID)

        token_generator = f'https://{config.HON_ALT_DOMAIN}/site/create-access-token'
        cat_query = {'discordId' : author.id, 'password' : config.HON_CAT_PASSWORD}
        
        async with aiohttp.ClientSession() as session:

            async with session.get(token_generator, params=cat_query) as resp:
                token = await resp.text()

        notes_url = f'https://{config.HON_ALT_DOMAIN}/{token}'
        await author.send(f'Current Testing Notes: {notes_url}')
        await log_channel.send(f'({strftime("%a, %d %b %Y, %H:%M:%S %Z", gmtime())}) {author.mention} received Testing Notes with the URL: `{notes_url}`')

def setup(bot):
    bot.add_cog(Testing(bot))
    print('Testing loaded.')
