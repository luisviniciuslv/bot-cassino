import asyncio
from discord.ext import commands
import discord
import random
from utils.database import user_get, update_user
from utils.funcoes import level
class Jogos(commands.Cog):
    def __init__(self, client):
        self.client = client

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
            await level(ctx.guild.id, ctx.author.id, value)
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
            await level(ctx.guild.id, ctx.author.id, value)
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
            await level(ctx.guild.id, ctx.author.id, value)
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
