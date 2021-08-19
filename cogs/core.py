import discord, asyncio, random
from discord.ext import commands
from discord_components import *


class Core(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.nums = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7, 8, 9, ]

    @commands.command(aliases=['d'])
    async def duel(self, ctx, user : discord.Member):
        emojis = {e.name:str(e) for e in ctx.bot.emojis}
        await ctx.send(
            embed=discord.Embed(title='Duels', description=f'**Player 1:** {ctx.author.mention}\n**Player 2:** {user.mention}', color=65535),
            components=[[
            Button(style=ButtonStyle.green, label="Accept", custom_id="accept"),
            Button(style=ButtonStyle.red, label="Decline", custom_id="decline")]], delete_after=10)

        try:
            res = await self.client.wait_for("button_click", check=lambda m: m.author == user and m.channel == ctx.message.channel, timeout=10)
            if res.component.id == "accept":
                await res.message.delete()
                first = await ctx.send(embed=discord.Embed(title=f'{ctx.author.name} vs {user.name}', description=f"‏‏‎⋆｡˚ ☽ ˚｡⋆｡˚ ☁︎ ˚｡⋆\n⋆｡˚ ☽ ˚｡⋆｡˚ ☁︎ ˚｡⋆\n\n{emojis['samstrike1']}{emojis['samstrike2']} ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎{emojis['waddlestrike2']}{emojis['waddlestrike1']}", color=65535), components=[Button(style=ButtonStyle.red, label=" ‎‎‎‎ ‎‎  ‎‎ ‎‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ 💢‎ ‎‎‎‎ ‎‎  ‎‎ ‎‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎‎‎", disabled=True, custom_id="attack")])

                await asyncio.sleep(random.choice(self.nums)) # randomly waits 0-10 seconds

                await first.edit(embed=discord.Embed(title=f'{ctx.author.name} vs {user.name}', description=f"‏‏‎⋆｡˚ ☽ ˚｡⋆｡˚ ☁︎ ˚｡⋆\n⋆｡˚ ☽ ˚｡⋆｡˚ ☁︎ ˚｡⋆\n\n{emojis['samstrike1']}{emojis['samstrike2']} ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎{emojis['waddlestrike2']}{emojis['waddlestrike1']}", color=65535), components=[Button(style=ButtonStyle.red, disabled=False, label=" ‎‎‎‎ ‎‎  ‎‎ ‎‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ 💢‎ ‎‎‎‎ ‎‎  ‎‎ ‎‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎ ‎‎‎‎", custom_id="attack")])
                try:
                    res = await self.client.wait_for("button_click", check=lambda m: m.author == user or m.author == ctx.author and m.channel == ctx.message.channel, timeout=10)
                    if res.component.id == "attack":
                        if res.author.id == self.client.user.id:
                            await first.edit(embed=discord.Embed(title=f'{res.author.name} is the winner!', description=f"‏‏‎⋆｡˚ ☽ ˚｡⋆｡˚ ☁︎ ˚｡⋆\n⋆｡˚ ☽ ˚｡⋆｡˚ ☁︎ ˚｡⋆\n\n{emojis['4193_Kirbyhappy']} ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎{emojis['waddlelose2']}{emojis['waddlelose1']}", color=65535))
                        else:
                            await first.edit(embed=discord.Embed(title=f'{res.author.name} is the winner!', description=f"‏‏‎⋆｡˚ ☽ ˚｡⋆｡˚ ☁︎ ˚｡⋆\n⋆｡˚ ☽ ˚｡⋆｡˚ ☁︎ ˚｡⋆\n\n{emojis['samlose']} ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎  ‎{emojis['samwaddle']}", color=65535))
                except asyncio.TimeoutError:
                    await first.edit(embed=discord.Embed(title=f'{res.author.name} vs {user.name}', description=f"‏‏‎⋆｡˚ ☽ ˚｡⋆｡˚ ☁︎ ˚｡⋆\n⋆｡˚ ☽ ˚｡⋆｡˚ ☁︎ ˚｡⋆\n\n{emojis['samlose']} ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎{emojis['waddlelose2']}{emojis['waddlelose1']}", color=65535))
            else:
                await res.message.delete()
        except asyncio.TimeoutError:
            await ctx.send(embed=discord.Embed(description=f"{user.mention} did not answer the duel request in time", color=65535))





def setup(client):
    client.add_cog(Core(client))