import asyncio
import random
from discord.ext import commands, tasks
import discord
from utils.database import user_get, update_user, findall

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @tasks.loop(minutes=2)
    async def randomword(self):
        palavras = ['relógio', 'paralelepipedo', 'câmera', 'controle', 'container', 'televisão', 'papel', 'copo', 'água', 'mouse']
        palavra = random.choice(palavras)
        channel = self.client.get_channel(986747642010816562)

        msg = await channel.send(palavra)
        def check(message):
            return message.content.lower() == palavra
        while True:
            try:    
                message = await self.client.wait_for('message', timeout=4, check=check)
            except asyncio.TimeoutError:
                return await msg.delete()
            else:
                embed=discord.Embed(title="Recebeu", description="500 coins", color=0x00ff4c)
                embed.set_author(name=message.author.name)
                embed.add_field(name="Acertou a palavra", value=palavra, inline=False)
                await message.channel.send(embed=embed)
                await update_user(message.guild.id, message.author.id, 'coins', 500, 'inc')

    @tasks.loop(hours=2)
    async def CDI(self):
        channel = self.client.get_channel(986747642010816562)
        await channel.send('O saldo de vocês está rendendo 100% do CDI no banco!')
        for i in await findall():
            coins = await user_get(933020401632677888,int(i['_id']), 'banco')
            coins = int(coins) * 1.01
            coins = str(coins).split('.')[0]
            coins = int(coins)
            await update_user(933020401632677888, i['_id'], 'banco', coins, 'set')

    @commands.Cog.listener()
    async def on_ready(self):
        print('@================@')
        print('    BOT ONLINE    ')
        print('@================@')
        self.randomword.start()
        self.CDI.start()
        while True:
            await self.client.change_presence(status=discord.Status.online, activity=discord.Game(name="so", type=3))
            
            await self.client.change_presence(status=discord.Status.online, activity=discord.Game(name="foda", type=3))
            await asyncio.sleep(1)
def setup(client):
    client.add_cog(Events(client))
