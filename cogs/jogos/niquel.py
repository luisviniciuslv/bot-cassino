import asyncio
import random

import discord
from discord.ext import commands
from utils.database import update_user, user_get
from utils.funcoes import level


class Niquel(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.on_duel = []
    
  @commands.command(aliases=['níquel'])
  async def niquel(self, ctx, aposta:int):

      if aposta >  await user_get(ctx.guild.id, ctx.author.id, 'coins'):
          await ctx.channel.send(f"você tem apenas {await user_get(ctx.guild.id, ctx.author.id, 'coins')} coins na carteira")
          return

      if aposta < 1:
          await ctx.channel.send(f"você não pode apostar menos que 1 coin")
          return
  
      await update_user(ctx.guild.id,ctx.author.id,'coins', -aposta, 'inc')
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

          await level(ctx.guild.id, ctx.author.id, aposta*1000)
          await update_user(ctx.guild.id,ctx.author.id,'coins', aposta*1000, 'inc')
          await update_user(ctx.guild.id,ctx.author.id,'valor_ganho',aposta*1000, 'inc')
          await update_user(ctx.guild.id,ctx.author.id,'coins', aposta, 'inc')
          await msg.edit(embed=new_embed)

          return
  
      if bobina.count('💎') == 3:
          new_embed=discord.Embed(title="Caça-níquel", color=0x2bff00)
          new_embed.set_author(name=ctx.author.name)
          new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
          new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
          new_embed.add_field(name="Valor ganho", value=aposta*100, inline=False)

          await level(ctx.guild.id, ctx.author.id, aposta*100)
          await update_user(ctx.guild.id,ctx.author.id,'coins', aposta*100, 'inc')
          await update_user(ctx.guild.id,ctx.author.id,'valor_ganho',aposta*100, 'inc')
          await update_user(ctx.guild.id,ctx.author.id,'coins', aposta, 'inc')
          await msg.edit(embed=new_embed)
    
          return

      if bobina.count('🪙') == 3:
          new_embed=discord.Embed(title="Caça-níquel", color=0x2bff00)
          new_embed.set_author(name=ctx.author.name)
          new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
          new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
          new_embed.add_field(name="Valor ganho", value=aposta*10, inline=False)

          await level(ctx.guild.id, ctx.author.id, aposta*10)
          await update_user(ctx.guild.id,ctx.author.id,'coins', aposta*10, 'inc')
          await update_user(ctx.guild.id,ctx.author.id,'valor_ganho',aposta*10, 'inc')
          await update_user(ctx.guild.id,ctx.author.id,'coins', aposta, 'inc')
          await msg.edit(embed=new_embed)

          return

      if bobina.count('🔥') >= 2:
          new_embed=discord.Embed(title="Caça-níquel", color=0x2bff00)
          new_embed.set_author(name=ctx.author.name)
          new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
          new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
          new_embed.add_field(name="Valor ganho", value=aposta*5, inline=False)

          await level(ctx.guild.id, ctx.author.id, aposta*5)
          await update_user(ctx.guild.id,ctx.author.id,'coins', aposta*5, 'inc')
          await update_user(ctx.guild.id,ctx.author.id,'valor_ganho',aposta*5, 'inc')
          await update_user(ctx.guild.id,ctx.author.id,'coins', aposta, 'inc')
          await msg.edit(embed=new_embed)

          return

      if bobina.count('x3') >= 2:
          new_embed=discord.Embed(title="Caça-níquel", color=0x2bff00)
          new_embed.set_author(name=ctx.author.name)
          new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
          new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
          new_embed.add_field(name="Valor ganho", value=aposta*3, inline=False)

          await level(ctx.guild.id, ctx.author.id, aposta*3)
          await update_user(ctx.guild.id,ctx.author.id,'coins', aposta*3, 'inc')
          await update_user(ctx.guild.id,ctx.author.id,'valor_ganho',aposta*3, 'inc')
          await update_user(ctx.guild.id,ctx.author.id,'coins', aposta, 'inc')
          await msg.edit(embed=new_embed)

          return

      if bobina.count('x3500') == 3:
          new_embed=discord.Embed(title="Caça-níquel", color=0x2bff00)
          new_embed.set_author(name=ctx.author.name)
          new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
          new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
          new_embed.add_field(name="Valor ganho", value=aposta*3500, inline=False)

          await level(ctx.guild.id, ctx.author.id, aposta*3500)
          await update_user(ctx.guild.id,ctx.author.id,'coins', aposta*3500, 'inc')
          await update_user(ctx.guild.id,ctx.author.id,'valor_ganho',aposta*3500, 'inc')
          await update_user(ctx.guild.id,ctx.author.id,'coins', aposta, 'inc')                  
          await msg.edit(embed=new_embed)

          return

      if bobina.count('x0.5') >= 2:
          new_embed=discord.Embed(title="Caça-níquel", color=0xffdd00)
          new_embed.set_author(name=ctx.author.name)
          new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
          new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
          new_embed.add_field(name="Valor ganho", value=round(aposta*0.5), inline=False)

          await level(ctx.guild.id, ctx.author.id, round(aposta*0.5))
          await update_user(ctx.guild.id,ctx.author.id,'coins', round(aposta*0.5), 'inc')
          await update_user(ctx.guild.id,ctx.author.id,'coins', -aposta, 'inc')
          await update_user(ctx.guild.id,ctx.author.id,'valor_perdido', aposta*0.5, 'inc')
          await update_user(ctx.guild.id,ctx.author.id,'coins', aposta, 'inc')                  
          await msg.edit(embed=new_embed)

      else:
          new_embed=discord.Embed(title="Caça-níquel", color=0xffdd00)
          new_embed.set_author(name=ctx.author.name)
          new_embed.add_field(name="Valor apostado", value=aposta, inline=False)
          new_embed.add_field(name="Girando bobinas", value=f'{bobina[0]}---{bobina[1]}---{bobina[2]}', inline=False) 
          new_embed.add_field(name="Valor ganho", value='0', inline=False)
    
          await update_user(ctx.guild.id,ctx.author.id,'valor_perdido', aposta, 'inc')
          await msg.edit(embed=new_embed)
          
          return

def setup(client):
  client.add_cog(Niquel(client))
