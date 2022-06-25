import datetime
from discord.ext import commands
import discord
import random

import pytz
from utils.database import user_get, update_user, get_guild_ranking
# funções

class User(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def doar(self, ctx, valor:int, member:discord.Member):
        if valor <= 0:
             await ctx.send(f"Você não pode doar 0 coins")
             return
        if member.id == ctx.author.id:
            await ctx.send("Você não pode doar para si mesmo")
            return
        if await user_get(ctx.guild.id, ctx.author.id, 'coins') < valor :
            await ctx.send(f"Você não pode doar menos doque você tem")
            return
        await update_user(ctx.guild.id, ctx.author.id, 'coins', -valor, 'inc')
        await update_user(ctx.guild.id, member.id, 'coins', valor, 'inc')

        embed = discord.Embed(title=f"{ctx.author.name} doou", description=f"**{valor}**", color=0x4FABF7)
        embed.add_field(name=f'para o', value=f"**{member.name}**", inline=False)
        await ctx.channel.send(embed=embed)

    @commands.command(aliases=['rec'])
    async def recompensa(self, ctx):
        async def fatura(money_hour, user):
            current_time = datetime.datetime.now(pytz.timezone('America/Santarem')).replace(microsecond=0, tzinfo=None)
            Last_hour = await user_get(user.guild.id, user.author.id, 'Last_time')
            #year
            if int(str(Last_hour).split(' ')[0].split('-')[0]) > int(str(current_time).split(' ')[0].split('-')[0]):
                return 'max'
            #mouth
            if int(str(Last_hour).split(' ')[0].split('-')[1]) > int(str(current_time).split(' ')[0].split('-')[1]):
                return 'max'
            #day
            if int(str(current_time).split(' ')[0].split('-')[2]) + int(str(Last_hour).split(' ')[0].split('-')[2]) >= 2:
                return 'max'
        
            #hour negative
            if str(Last_hour).split(' ')[1].split(':')[0] < str(current_time).split(' ')[1].split(':')[0]:
                minutos_trabalhados = (int(str(current_time).split(' ')[1].split(':')[1]) + 60) - int(str(Last_hour).split(' ')[1].split(':')[1])
                return round(minutos_trabalhados * money_hour/24)
            #hour
            if int(str(Last_hour).split(' ')[1].split(':')[0]) > int(str(current_time).split(' ')[1].split(':')[0]):
                horas_trabalhadas = int(str(current_time).split(' ')[1].split(':')[0]) - int(str(Last_hour).split(' ')[1].split(':')[0])
                minutos_trabalhados = (int(str(current_time).split(' ')[1].split(':')[1]) + 60) - int(str(Last_hour).split(' ')[1].split(':')[1])
                dinheiro = round((money_hour * horas_trabalhadas) + (money_hour * minutos_trabalhados/60))
                return dinheiro
            #min
            if str(Last_hour).split(' ')[1].split(':')[1] < str(current_time).split(' ')[1].split(':')[1]:
                minutos_trabalhados = int(str(current_time).split(' ')[1].split(':')[1]) - int(str(Last_hour).split(' ')[1].split(':')[1])
                return round(minutos_trabalhados * money_hour/60)

        looting_time = await user_get(ctx.guild.id, ctx.author.id, 'Time_loot')

        current_time = datetime.datetime.now(pytz.timezone('America/Santarem')).replace(microsecond=0, tzinfo=None)

        empresas = await user_get(ctx.guild.id, ctx.author.id, 'empresas')

        if current_time <= looting_time:
            await ctx.channel.send(f'{ctx.author.name}, espere `{looting_time - current_time}` para poder receber novamente.')
            return

        embed=discord.Embed(title=f"{ctx.author.name} Resgatou sua recompensa", color=0x11ff00)
        num = random.randint(0, 1000)
        if num == 777:
            value = 1000
        if num < 600:
            value = 100
        if num > 600 and num < 800:
            value = 200
        if num > 800 and num < 950:
            value = 300
        if num > 950 and num < 990:
            value = 400
        if num > 990:
            value = 500
            
        embed.add_field(name="número gerado", value=num, inline=False)
        embed.add_field(name="valor resgatado", value=f"{value}$", inline=False)
        if 'vendinha' not in empresas and 'mercado' not in empresas and 'shoopping' not in empresas and 'fazenda' not in empresas:
            await update_user(ctx.guild.id, ctx.author.id, 'coins', value, 'inc')
            await update_user(ctx.guild.id, ctx.author.id, 'Time_loot', current_time + datetime.timedelta(minutes=3), 'set')
            await update_user(ctx.guild.id, ctx.author.id, 'Last_time', current_time + datetime.timedelta(), 'set')
            await ctx.channel.send(embed=embed)
            return
        if 'vendinha' in empresas:
            if await fatura(200, ctx) == 'max':
                valuelocal = 200*24
                embed.add_field(name="Valor recebido da vendinha: ", value=f'{valuelocal}$', inline=False)
                value+=valuelocal
            else:
                valuelocal = int(await fatura(200,ctx))
                value += valuelocal
                embed.add_field(name="Valor recebido da vendinha: ", value=f'{valuelocal}$', inline=False)

        if 'mercado' in empresas:
            if await fatura(500,ctx) == 'max':
                valuelocal = 500*24
                embed.add_field(name="Valor recebido do mercado:", value=f'{valuelocal}$', inline=False)
                value+=valuelocal
            else:
                valuelocal = int(await fatura(500,ctx))
                value += valuelocal
                embed.add_field(name="Valor recebido do mercado:", value=f'{valuelocal}$', inline=False)

        if 'shopping' in empresas:
            if await fatura(500,ctx) == 'max':
                valuelocal = 800 * 24
                embed.add_field(name="Valor recebido do shopping:", value=f'{valuelocal}$', inline=False)
                value+=valuelocal
            else:
                valuelocal = int(await fatura(800,ctx))
                value += valuelocal  
                embed.add_field(name="Valor recebido do shopping:", value=f'{valuelocal}$', inline=False)
        
        if 'fazenda' in empresas:
            if await fatura(500,ctx) == 'max':
                valuelocal = 1000*24
                embed.add_field(name="Valor recebido da fazenda:", value=f'{valuelocal}$', inline=False)
                value+=valuelocal
            else:
                valuelocal = int(await fatura(1000,ctx))
                value += valuelocal
                embed.add_field(name="Valor recebido da fazenda:", value=f'{valuelocal}$', inline=False)
        if 'concessionaria' in empresas:
            if await fatura(500,ctx) == 'max':
                valuelocal = 2000*24
                embed.add_field(name="Valor recebido da concessionaria:", value=f'{valuelocal}$', inline=False)
                value += valuelocal
            else:
                valuelocal = int(await fatura(2000,ctx))
                value += valuelocal
                embed.add_field(name="Valor recebido da concessionaria:", value=f'{valuelocal}$', inline=False)

        embed.add_field(name=f"Valor total recebido:", value=f'{value}$', inline=False)

        await ctx.channel.send(embed=embed)
        await update_user(ctx.guild.id, ctx.author.id, 'coins', value, 'inc')
        await update_user(ctx.guild.id, ctx.author.id, 'Time_loot', current_time + datetime.timedelta(minutes=3), 'set')
        await update_user(ctx.guild.id, ctx.author.id, 'Last_time', current_time + datetime.timedelta(), 'set')

    @commands.command()
    async def depositar(self, ctx, qtdcoins:int):
        if qtdcoins > await user_get(ctx.guild.id, ctx.author.id, 'coins'):
            await ctx.send(f"Você não tem {qtdcoins}$ para depositar")
            return
        embed=discord.Embed(title="Valor depositado", color=0x11ff00)
        embed.add_field(name=f"{ctx.author.name} depositou", value=f"{qtdcoins} no banco", inline=False)
        await ctx.channel.send(embed=embed)
        await update_user(ctx.guild.id, ctx.author.id, 'banco', qtdcoins, 'inc')
        await update_user(ctx.guild.id, ctx.author.id, 'coins', -qtdcoins, 'inc')

    @commands.command()
    async def sacar(self, ctx, qtdcoins:int):
        if qtdcoins > await user_get(ctx.guild.id, ctx.author.id, 'banco'):
            await ctx.channel.send(f"Você não tem {qtdcoins}$ para sacar")
            return
        embed=discord.Embed(title="Valor sacado", color=0x11ff00)
        embed.add_field(name=f"{ctx.author.name} sacou", value=f"{qtdcoins} do banco", inline=False)
        await ctx.send(embed=embed)
        await update_user(ctx.guild.id, ctx.author.id, 'coins', +qtdcoins, 'inc')
        await update_user(ctx.guild.id, ctx.author.id, 'banco', -qtdcoins, 'inc')

    @commands.command(aliases=['p'])
    async def perfil(self, ctx, user: discord.Member = None):

        if user == None:
            embed = discord.Embed(color=0xFFD488)
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.add_field(name='Carteira', value=f"{await user_get(ctx.guild.id, ctx.author.id, 'coins')}$", inline=False)
            embed.add_field(name='Banco', value=f"{await user_get(ctx.guild.id, ctx.author.id, 'banco')}$", inline=False)
            embed.add_field(name='Quantia total apostada', value=f"{await user_get(ctx.guild.id, ctx.author.id, 'valor_apostado')}$", inline=False)
            embed.add_field(name='Quantia ganha em apostas', value=f"{await user_get(ctx.guild.id, ctx.author.id, 'valor_ganho')}$", inline=False)
            embed.add_field(name='Quantia perdida em apostas', value=f"{await user_get(ctx.guild.id, ctx.author.id, 'valor_perdido')}$", inline=False)
            aux = 0
            embed.add_field(name='Empresas compradas por', value=f'{ctx.author.name}', inline=False)
            for i in await user_get(ctx.guild.id, ctx.author.id, 'empresas'):
                aux+=1 
                embed.add_field(name='----------', value=f'**{i}**', inline=False)

        else:
            embed = discord.Embed(color=0xFFD488)
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_author(name=user.name, icon_url=user.avatar_url)
            embed.add_field(name='Carteira', value=f"{await user_get(ctx.guild.id, user.id, 'coins')}$", inline=False)
            embed.add_field(name='Banco', value=f"{await user_get(ctx.guild.id, user.id, 'banco')}$", inline=False)
            embed.add_field(name='Quantia total apostada', value=f"{await user_get(ctx.guild.id, user.id, 'valor_apostado')}$", inline=False)
            embed.add_field(name='Quantia ganha em apostas', value=f"{await user_get(ctx.guild.id, user.id, 'valor_ganho')}$", inline=False)
            embed.add_field(name='Quantia perdida em apostas', value=f"{await user_get(ctx.guild.id, user.id, 'valor_perdido')}$", inline=False)
            aux = 0
            if await user_get(ctx.guild.id, user.id, 'empresas') == []:
                pass
            else:
                embed.add_field(name='Empresas compradas por', value=f'{user.name}', inline=False)
                for i in await user_get(ctx.guild.id, user.id, 'empresas'):
                    aux+=1 
                    embed.add_field(name=f'{aux}:', value=f'**{i}**', inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=['ranking'])
    async def top(self, ctx):
        content = await get_guild_ranking(self.client, ctx.guild.id)
        embed = discord.Embed(title="Ranking", description=f"{content}", color=0x8BEAFF)
        await ctx.channel.send(embed=embed)
def setup(client):
  client.add_cog(User(client))
