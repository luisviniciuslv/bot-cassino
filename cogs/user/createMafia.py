import asyncio

import discord
from discord.ext import commands


class Mafia(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def createmafia(self, ctx, name:str=None):
        embed=discord.Embed(title="Tamanho da máfia", color=0xffdd00)
        embed.add_field(name="1️⃣: 5 Membros (para grupos de amigos/times)", value="`10`", inline=False)
        embed.add_field(name="2️⃣: 10 Membros (para grupos maiores de amigos)", value = "`20`", inline=False)
        embed.add_field(name="3️⃣: 20 Membros (para conhecidos e próximos)", value = "`40`", inline=False)
        embed.add_field(name="4️⃣: 50 Membros (para grupos grandes)", value = "`80`", inline=False)
        embed.add_field(name="5️⃣: 100 Membros (para grupos ainda maiores) ", value = "`100`", inline=False)
        embed.add_field(name="6️⃣: 200 Membros (para influencers em acensão)", value = "`200`", inline=False)
        
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')
        await msg.add_reaction('3️⃣')
        await msg.add_reaction('4️⃣')
        await msg.add_reaction('5️⃣')
        await msg.add_reaction('6️⃣')
        await asyncio.sleep(0.3)
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '1️⃣' or str(reaction.emoji) == '2️⃣' or str(reaction.emoji) == '3️⃣' or str(reaction.emoji) == '4️⃣' or str(reaction.emoji) == '5️⃣' or str(reaction.emoji) == '6️⃣' and reaction.message.id == msg.id
        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=20.0, check=check)
        except asyncio.TimeoutError:
            return await msg.delete()
        print(user, ctx.author)
        if str(reaction.emoji) == '1️⃣':
            print('escolheu 1')
        if str(reaction.emoji) == '2️⃣':
            print('escolheu 2')
        if str(reaction.emoji) == '3️⃣':
            print('escolheu 3')
        if str(reaction.emoji) == '4️⃣':
            print('escolheu 4')
        if str(reaction.emoji) == '5️⃣':
            print('escolheu 5')
        if str(reaction.emoji) == '6️⃣':
            print('escolheu 6')

def setup(client):
  client.add_cog(Mafia(client))
#desci de gall, se quiser vi jaja vo
#vo dar uma saida dps eu volto
