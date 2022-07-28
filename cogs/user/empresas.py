import discord
from discord.ext import commands
from utils.database import update_user, user_get


class Empresas(commands.Cog):
  def __init__(self, client):
    self.client = client
  @commands.command(aliases=['empresas'])
  async def comprar(self, ctx, empresa:str=None):
    if empresa == None:
      embed = discord.Embed(title="Empresas", description=f"Qual deseja comprar?", color=0x4FABF7)
      embed.add_field(name=f'Vendinha', value=f"**Resgate 200 coins por hora\n preço: 10000 coins**\nPara comprar digite: **!comprar vendinha**\nequivale a 1 ponto no ranking", inline=False)
      embed.add_field(name=f'Mercado', value=f"**Resgate 500 coins por hora\n preço: 25000 coins**\nPara comprar digite: **!comprar mercado**\nequivale a 2 pontos no ranking", inline=False)
      embed.add_field(name=f'Shopping', value=f"**Resgate 800 coins por hora hora\n preço: 35000 coins**\nPara comprar digite: **!comprar shopping**\nequivale a 3 pontos no ranking", inline=False)
      embed.add_field(name=f'Fazenda', value=f"**Resgate 1000 coins por hora\n preço: 45000 coins**\nPara comprar digite: **!comprar fazenda**\nequivale a 4 pontos no ranking", inline=False)
      embed.add_field(name=f'concessionaria', value=f"**Resgate 2000 coins por hora\n preço: 75000 coins**\nPara comprar digite: **!comprar concessionaria**\nequivale a 5 pontos no ranking", inline=False)
      await ctx.channel.send(embed=embed)
      return

    if empresa == 'vendinha':
      if 'vendinha' in await user_get(ctx.guild.id, ctx.author.id, 'empresas'):
        await ctx.channel.send('Você já tem a vendinha comprada!')
        return
      if await user_get(ctx.guild.id, ctx.author.id, 'coins') < 10000:
        await ctx.channel.send("Você não tem 10000 para comprar a vendinha")
        return

      empresas = await user_get(ctx.guild.id, ctx.author.id, 'empresas')
      empresas.append('vendinha')
      await update_user(ctx.guild.id, ctx.author.id, 'empresas', empresas, 'set')
      await update_user(ctx.guild.id, ctx.author.id, 'coins', -10000, 'inc')
      embed = discord.Embed(title="Empresas", description=f"", color=0x4FABF7)
      embed.add_field(name=f'Você comprou a vendinha', value=f"**digite !recompensa ou !rec para resgatar seu dinheiro**", inline=False)
      await ctx.channel.send(embed=embed)
      return

    if empresa == 'mercado':
      if 'mercado' in await user_get(ctx.guild.id, ctx.author.id, 'empresas'):
        await ctx.channel.send('Você já tem o mercado comprado!')
        return
      if await user_get(ctx.guild.id, ctx.author.id, 'coins') < 25000:
        await ctx.channel.send("Você não tem 25000 para comprar o mercado")
        return

      empresas = await user_get(ctx.guild.id, ctx.author.id, 'empresas')
      empresas.append('mercado')
      await update_user(ctx.guild.id, ctx.author.id, 'empresas', empresas, 'set')
      await update_user(ctx.guild.id, ctx.author.id, 'coins', -25000, 'inc')
      embed = discord.Embed(title="Empresas", description=f"", color=0x4FABF7)
      embed.add_field(name=f'Você comprou o mercado', value=f"**digite digite !recompensa ou !rec para resgatar seu dinheiro**", inline=False)
      await ctx.channel.send(embed=embed)

      return
    if empresa == 'shopping':
      if 'shopping' in await user_get(ctx.guild.id, ctx.author.id, 'empresas'):
        await ctx.channel.send('Você já tem o shopping comprado!')
        return
      if await user_get(ctx.guild.id, ctx.author.id, 'coins') < 35000:
        await ctx.channel.send("Você não tem 35000 para comprar o shopping")
        return

      empresas = await user_get(ctx.guild.id, ctx.author.id, 'empresas')
      empresas.append('shopping')
      await update_user(ctx.guild.id, ctx.author.id, 'empresas', empresas, 'set')
      await update_user(ctx.guild.id, ctx.author.id, 'coins', -35000, 'inc')
      embed = discord.Embed(title="Empresas", description=f"", color=0x4FABF7)
      embed.add_field(name=f'Você comprou o shopping', value=f"**digite digite !recompensa ou !rec para resgatar seu dinheiro**", inline=False)
      await ctx.channel.send(embed=embed)
      return

    if empresa == 'fazenda':
      if 'fazenda' in await user_get(ctx.guild.id, ctx.author.id, 'empresas'):
        await ctx.channel.send('Você já tem a fazenda comprada!')
        return
      if await user_get(ctx.guild.id, ctx.author.id, 'coins') < 45000:
        await ctx.channel.send("Você não tem 45000 para comprar a fazenda")
        return
        
      empresas = await user_get(ctx.guild.id, ctx.author.id, 'empresas')
      empresas.append('fazenda')
      await update_user(ctx.guild.id, ctx.author.id, 'empresas', empresas, 'set')
      await update_user(ctx.guild.id, ctx.author.id, 'coins', -45000, 'inc')
      embed = discord.Embed(title="Empresas", description=f"", color=0x4FABF7)
      embed.add_field(name=f'Você comprou a fazenda', value=f"**digite digite !recompensa ou !rec para resgatar seu dinheiro**", inline=False)
      await ctx.channel.send(embed=embed)
      return

    if empresa == 'concessionaria':
      if 'concessionaria' in await user_get(ctx.guild.id, ctx.author.id, 'empresas'):
        await ctx.channel.send('Você já tem a concessionária comprada!')
        return
      if await user_get(ctx.guild.id, ctx.author.id, 'coins') < 75000:
        await ctx.channel.send("Você não tem 75000 para comprar a concessionária")
        return
        
      empresas = await user_get(ctx.guild.id, ctx.author.id, 'empresas')
      empresas.append('concessionaria')
      await update_user(ctx.guild.id, ctx.author.id, 'empresas', empresas, 'set')
      await update_user(ctx.guild.id, ctx.author.id, 'coins', -75000, 'inc')
      embed = discord.Embed(title="concessionria", description=f"", color=0x4FABF7)
      embed.add_field(name=f'Você comprou a concessionaria', value=f"**digite digite !recompensa ou !rec para resgatar seu dinheiro**", inline=False)
      await ctx.channel.send(embed=embed)
      return
    else:
      await ctx.channel.send('Essa empresa não existe para ser comprada')

def setup(client):
  client.add_cog(Empresas(client))
