import asyncio
from discord.ext import commands
import discord
import random
from utils.database import user_get, update_user, get_guild_ranking
import time

class Jogos(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def niquel(self, ctx, aposta:int):
        if aposta >  await user_get(ctx.guild.id, ctx.author.id, 'coins'):
            await ctx.channel.send(f"você tem apenas {await user_get(ctx.guild.id, ctx.author.id, 'coins')} coins na carteira")
            return
        if aposta < 1:
            await ctx.channel.send(f"você não pode apostar menos que 1 coin")
            return
        await update_user(ctx.guild.id,ctx.author.id,'valor_apostado', aposta, 'inc')
        emojis = ['x3','💎', '🪙', 'x1000', '🔥', 'x3500', 'x0.5', '💀', '⚡','🏴‍☠️','☠️']
        bobina = [random.choice(emojis), random.choice(emojis), random.choice(emojis)]
        first_embed=discord.Embed(title="Caça-níquel", color=0xffdd00)
        first_embed.set_author(name=ctx.author.name)
        first_embed.add_field(name="Valor apostado", value=aposta, inline=False)
        first_embed.add_field(name="Girando bobinas", value='?---?---?', inline=False)
        msg = await ctx.channel.send(embed=first_embed)
        await asyncio.sleep(2)
        new_embed=discord.Embed(title="Caça-níquel", color=0xffdd00)
        new_embed.set_author(name=ctx.author.name)
        new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
        new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---?---?', inline=False)
        await msg.edit(embed=new_embed)
        await asyncio.sleep(2)
        new_embed=discord.Embed(title="Caça-níquel", color=0xffdd00)
        new_embed.set_author(name=ctx.author.name)
        new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
        new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---?', inline=False) 
        await msg.edit(embed=new_embed)
        await asyncio.sleep(2)
        new_embed=discord.Embed(title="Caça-níquel", color=0xffdd00)
        new_embed.set_author(name=ctx.author.name)
        new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
        new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
        await msg.edit(embed=new_embed)
        if bobina.count('x1000') == 3:
            new_embed=discord.Embed(title="Caça-níquel", color=0x2bff00)
            new_embed.set_author(name=ctx.author.name)
            new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
            new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
            new_embed.add_field(name="Valor ganho", value=aposta*1000, inline=False)
            await update_user(ctx.guild.id,ctx.author.id,'coins', aposta*1000, 'inc')
            await msg.edit(embed=new_embed)
            return
        if bobina.count('💎') == 3:
            new_embed=discord.Embed(title="Caça-níquel", color=0x2bff00)
            new_embed.set_author(name=ctx.author.name)
            new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
            new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
            new_embed.add_field(name="Valor ganho", value=aposta*100, inline=False)
            await update_user(ctx.guild.id,ctx.author.id,'coins', aposta*100, 'inc')
            await msg.edit(embed=new_embed)
            return
        if bobina.count('🪙') == 3:
            new_embed=discord.Embed(title="Caça-níquel", color=0x2bff00)
            new_embed.set_author(name=ctx.author.name)
            new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
            new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
            new_embed.add_field(name="Valor ganho", value=aposta*10, inline=False)
            await update_user(ctx.guild.id,ctx.author.id,'coins', aposta*10, 'inc')
            await msg.edit(embed=new_embed)
            return
        if bobina.count('🔥') >= 2:
            new_embed=discord.Embed(title="Caça-níquel", color=0x2bff00)
            new_embed.set_author(name=ctx.author.name)
            new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
            new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
            new_embed.add_field(name="Valor ganho", value=aposta*5, inline=False)
            await update_user(ctx.guild.id,ctx.author.id,'coins', aposta*5, 'inc')
            await msg.edit(embed=new_embed)
            return
        if bobina.count('x3') >= 2:
            new_embed=discord.Embed(title="Caça-níquel", color=0x2bff00)
            new_embed.set_author(name=ctx.author.name)
            new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
            new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
            new_embed.add_field(name="Valor ganho", value=aposta*3, inline=False)
            await update_user(ctx.guild.id,ctx.author.id,'coins', aposta*3, 'inc')
            await msg.edit(embed=new_embed)
            return
        if bobina.count('x3500') == 3:
            new_embed=discord.Embed(title="Caça-níquel", color=0x2bff00)
            new_embed.set_author(name=ctx.author.name)
            new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
            new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
            new_embed.add_field(name="Valor ganho", value=aposta*3500, inline=False)
            await update_user(ctx.guild.id,ctx.author.id,'coins', aposta*3500, 'inc')
            await msg.edit(embed=new_embed)
            return
        if bobina.count('x0.5') == 3:
            new_embed=discord.Embed(title="Caça-níquel", color=0xffdd00)
            new_embed.set_author(name=ctx.author.name)
            new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
            new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
            new_embed.add_field(name="Valor ganho", value=round(aposta*0.5), inline=False)
            await update_user(ctx.guild.id,ctx.author.id,'coins', round(aposta*0.5), 'inc')
            await msg.edit(embed=new_embed)
        else:
            new_embed=discord.Embed(title="Caça-níquel", color=0xffdd00)
            new_embed.set_author(name=ctx.author.name)
            new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
            new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
            new_embed.add_field(name="Valor ganho", value='0', inline=False)
            await update_user(ctx.guild.id,ctx.author.id,'valor_perdido', aposta, 'inc')
            await update_user(ctx.guild.id,ctx.author.id,'coins', -aposta, 'inc')

            await msg.edit(embed=new_embed)
            return

    @commands.command()
    async def multi(self, ctx, range:int, escolha:int, aposta:int):
        if range < 2:
            await ctx.channel.send(f"Você não pode escolher um numero abaixo de 2")
            return
        if escolha > range:
            await ctx.channel.send(f"Você não pode escolher um número maior que o multiplicador")
            return
        if escolha < 1:
            await ctx.channel.send(f"você não pode escolher um número menor que 1 coin")

        if aposta >  await user_get(ctx.guild.id, ctx.author.id, 'coins'):
            await ctx.channel.send(f"você tem apenas {await user_get(ctx.guild.id, ctx.author.id, 'coins')} coins na carteira")
            return
        if aposta < 1:
            await ctx.channel.send(f"você não pode apostar menos que 1 coin")
            return

        await update_user(ctx.guild.id, ctx.author.id, 'coins', -aposta, 'inc')
        await update_user(ctx.guild.id, ctx.author.id, 'valor_apostado', aposta, 'inc')

        coins = await user_get(ctx.guild.id, ctx.author.id, 'coins')
        
        embed=discord.Embed(title="apostou", description="número par", color=0xffdd00)
        embed.set_author(name=ctx.author.name)
        embed.add_field(name="valor apostado", value=aposta, inline=False)
        embed.add_field(name="valor multiplicado a ganhar", value=aposta*range, inline=False)
        embed.add_field(name="valor na carteira", value=coins, inline=False)
        embed.set_footer(text=f"gerando numero entre 1 e {range}")
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(3)
        num = random.randint(1, range)
        if escolha == num:
            await msg.delete()
            embed=discord.Embed(title="apostou", description=f"número {escolha}", color=0x00ff4c)
            embed.set_author(name=ctx.author.name)
            embed.add_field(name="número gerado", value=num, inline=False)
            embed.add_field(name="ganhou", value=aposta*range, inline=False)
            value = aposta*range
            await ctx.channel.send(embed=embed)
            await update_user(ctx.guild.id, ctx.author.id, 'coins', value, 'inc')
            await update_user(ctx.guild.id, ctx.author.id, 'valor_ganho', value, 'inc')
        else:
            await msg.delete()
            embed=discord.Embed(title="apostou", description=f"número {escolha}", color=0xff0000)
            embed.set_author(name=ctx.author.name)
            embed.add_field(name="número gerado", value=num, inline=False)
            embed.add_field(name="perdeu", value=aposta, inline=False)
            await ctx.channel.send(embed=embed)
    @commands.command()
    async def par(self, ctx, qtdcoins : int):
        coins = await user_get(ctx.guild.id, ctx.author.id, 'coins')
        if qtdcoins > coins:
            await ctx.channel.send(f"você tem apenas {coins} coins na carteira")
            return
        if qtdcoins <= 0:
            await ctx.channel.send(f"você não pode apostar menos que 1 coin")
            return

        await update_user(ctx.guild.id, ctx.author.id, 'coins', -qtdcoins, 'inc')
        await update_user(ctx.guild.id, ctx.author.id, 'valor_apostado', qtdcoins, 'inc')

        coins = await user_get(ctx.guild.id, ctx.author.id, 'coins')

        embed=discord.Embed(title="apostou", description="número par", color=0xffee00)
        embed.set_author(name=ctx.author.name)
        embed.add_field(name="valor apostado", value=qtdcoins, inline=False)
        embed.add_field(name="valor na carteira", value=coins, inline=False)
        embed.set_footer(text="gerando numero")
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(3)
        num = random.randint(1, 1000)
        if num % 2 == 0:
            await msg.delete()
            embed=discord.Embed(title="apostou", description="número par", color=0x00ff4c)
            embed.set_author(name=ctx.author.name)
            embed.add_field(name="número gerado", value=num, inline=False)
            embed.add_field(name="ganhou", value=qtdcoins*2, inline=False)
            await ctx.channel.send(embed=embed)


            value = qtdcoins * 2
            await update_user(ctx.guild.id, ctx.author.id, 'coins', value, 'inc')
            await update_user(ctx.guild.id, ctx.author.id, 'valor_ganho', value, 'inc')
        else:
            await msg.delete()
            embed=discord.Embed(title="apostou", description="número par", color=0xff0000)
            embed.set_author(name=ctx.author.name)
            embed.add_field(name="número gerado", value=num, inline=False)
            embed.add_field(name="perdeu", value=qtdcoins, inline=False)
            await ctx.channel.send(embed=embed)
            await update_user(ctx.guild.id, ctx.author.id, 'valor_perdido', qtdcoins, 'inc')

    @commands.command(aliases=['ímpar'])
    async def impar(self, ctx, qtdcoins : int):
        coins = await user_get(ctx.guild.id, ctx.author.id, 'coins')
        if qtdcoins > coins:
            await ctx.channel.send(f"você tem apenas {coins} coins na carteira")
            return
            
        if qtdcoins <= 0:
            await ctx.channel.send(f"você não pode apostar menos que 1 coin")
            return
        await update_user(ctx.guild.id, ctx.author.id, 'coins', -qtdcoins, 'inc')
        await update_user(ctx.guild.id, ctx.author.id, 'valor_apostado', qtdcoins, 'inc')
        coins = await user_get(ctx.guild.id, ctx.author.id, 'coins')

        embed=discord.Embed(title="apostou", description="número ímpar", color=0xffee00)
        embed.set_author(name=ctx.author.name)
        embed.add_field(name="valor apostado", value=qtdcoins, inline=False)
        embed.add_field(name="valor na carteira", value=coins, inline=False)
        embed.set_footer(text="gerando numero")
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(3)

        num = random.randint(0, 1000)
        if num % 2 != 0:
            await msg.delete()
            embed=discord.Embed(title="apostou", description="número ímpar", color=0x00ff4c)
            embed.set_author(name=ctx.author.name)
            embed.add_field(name="número gerado", value=num, inline=False)
            embed.add_field(name="ganhou", value=qtdcoins*2, inline=False)
            await ctx.channel.send(embed=embed)
            value = qtdcoins * 2
            await update_user(ctx.guild.id, ctx.author.id, 'coins', value, 'inc')
            await update_user(ctx.guild.id, ctx.author.id, 'valor_ganho', value, 'inc')

        else:
            await msg.delete()
            embed=discord.Embed(title="apostou", description="número par", color=0xff0000)
            embed.set_author(name=ctx.author.name)
            embed.add_field(name="número gerado", value=num, inline=False)
            embed.add_field(name="perdeu", value=qtdcoins, inline=False)
            await ctx.channel.send(embed=embed)
            await update_user(ctx.guild.id, ctx.author.id, 'valor_perdido', qtdcoins, 'inc')
    

def setup(client):
  client.add_cog(Jogos(client))
