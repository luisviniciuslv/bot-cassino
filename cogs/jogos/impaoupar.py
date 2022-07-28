import asyncio
import random

import discord
from discord.ext import commands
from utils.database import update_user, user_get
from utils.funcoes import level


class ImparouPar(commands.Cog):
    def __init__(self, client):
        self.client = client

   
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
  client.add_cog(ImparouPar(client))
