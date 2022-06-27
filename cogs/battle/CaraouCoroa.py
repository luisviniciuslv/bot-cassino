import asyncio
import random
import discord
from discord.ext import commands
from utils.funcoes import level
from utils.database import user_get, update_user

class Battle(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.on_duel = []

  @commands.command(aliases=['cac'])
  async def caraoucoroa(self, ctx, qtdcoins : int, escolha:str, member : discord.Member = None):
    if escolha != "cara" and escolha != "coroa":
        await ctx.send(f"{ctx.author.name}, escolha entre cara ou coroa!")
        return
    if qtdcoins < 0:
      await ctx.send(f"{ctx.author.name}, você não pode duelar apostando um valor negativo.")
      return

    if await user_get(ctx.guild.id, ctx.author.id, 'coins') < qtdcoins:
      await ctx.send(f'{ctx.author.name}, você não possui coins suficientes.')
      return

    if ctx.author.id in self.on_duel:
      await ctx.channel.send(f'{ctx.author.name}, você já está em uma batalha!')
      return   

    if escolha == "cara":
        cara = ctx.author
    else:
        coroa = ctx.author

    if member is None:
      embed = discord.Embed(title="Duelo", description=f"**```{ctx.author.name} quer jogar cara ou coroa com alguém valendo {qtdcoins}$!```\nPara entrar no duelo basta reagir com ⚔**", color=0x4FABF7)
      embed.add_field(name=f'escolha do {ctx.author.name}', value=f"**{escolha}**", inline=False)
      embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
    else:
      if member.id == ctx.author.id:
        await ctx.send(f"@{ctx.author.name}, você não pode duelar contra você mesmo.")
        return
      elif await user_get(ctx.guild.id, member.id, 'coins') < qtdcoins:
        await ctx.send(f'@{ctx.author.name}, @{member.name} não possui coins suficientes na carteira.')
        return

      embed = discord.Embed(title="Duelo", description=f"**```{ctx.author.name} quer jogar cara ou coroa com {member.name}! Valendo {qtdcoins}```\nPara aceitar basta reagir com ⚔**", color=0x4FABF7)
      embed.add_field(name=f'escolha do {ctx.author.name}', value=f"**{escolha}**", inline=False)
      embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")


    msg = await ctx.channel.send(embed=embed)

    await msg.add_reaction('⚔')

    def check(reaction, user):
      return user != self.client.user and user != ctx.author and str(reaction.emoji) == '⚔' and reaction.message.id == msg.id and user not in self.on_duel
    while True:
      try:
        reaction, user = await self.client.wait_for('reaction_add', timeout=20.0, check=check)
      except asyncio.TimeoutError:
        return await msg.delete()
      else:
        if user != member: member = user

        if await user_get(ctx.guild.id, member.id, 'coins') < qtdcoins:
          await ctx.send(f'{member.name}, você não possui coins suficientes na carteira.')
          return

        await update_user(ctx.guild.id, member.id, 'coins', -qtdcoins, 'inc')
        await update_user(ctx.guild.id, ctx.author.id, 'coins', -qtdcoins, 'inc')
        await update_user(ctx.guild.id, member.id, 'valor_apostado', qtdcoins, 'inc')
        await update_user(ctx.guild.id, ctx.author.id, 'valor_apostado', qtdcoins, 'inc')
        await asyncio.sleep(5)
        

        if escolha == "cara":
            coroa = member
        else:
            cara = member
        break

    result = random.randint(1, 2)
    if result == 1:
        embed = discord.Embed(title="Sorteado", description=f"**CARA**", color=0x4FABF7)
        embed.add_field(name=f'vencedor', value=f"**{cara.name}**", inline=False)
        embed.add_field(name='Valor ganho', value=f"**{qtdcoins}**", inline=False)
        await update_user(ctx.guild.id, cara.id, 'coins', qtdcoins*2, 'inc')
        await level(ctx.guild.id, ctx.cara.id, qtdcoins*2)
        
        await ctx.channel.send(embed=embed)
        
    else:
        embed = discord.Embed(title="Sorteado", description=f"**COROA**", color=0x4FABF7)
        embed.add_field(name=f'vencedor', value=f"**{coroa.name}**", inline=False)
        embed.add_field(name=f'Valor ganho', value=f"**{qtdcoins}**", inline=False)
        await update_user(ctx.guild.id, coroa.id, 'coins', qtdcoins*2, 'inc')
        await level(ctx.guild.id, coroa.id, qtdcoins*2) 
        await ctx.channel.send(embed=embed)
            
def setup(client):
  client.add_cog(Battle(client))
