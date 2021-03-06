import discord
from discord.ext import commands

from utils.database import change_prefix, update_user,get_prefix
class Admin(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.has_permissions(ban_members=True) #arapaz é assim q comenta, izi
  @commands.command(aliases=['ac', 'setcoins'])
  async def addcoins(self, ctx, user : discord.Member = None, coins : int = None):
    if user == None:
      return await ctx.channel.send(f"{ctx.author.name}, Especifique um usuário para adicionar coins.")
    if coins == None or coins <= 0:
      return await ctx.channel.send("Quantidade de coins invalida.")

    await update_user(ctx.guild.id, user.id, 'coins', coins, 'inc')

    await ctx.channel.send(f"Foram adicionados {coins} coin(s) ao usuário {user.name}")
  @addcoins.error
  async def addcoins_error(self, ctx, error): pass

  @commands.has_any_role('〘 ADM 〙')
  @commands.command(aliases=['addMp'])
  async def addMafiaPoints(self, ctx, user : discord.Member = None, mp : int = None):
    if user == None:
      return await ctx.channel.send(f"{ctx.author.name}, Especifique um usuário para adicionar MP.")
    if mp == None or mp <= 0:
      return await ctx.channel.send("Quantidade de MP invalida.")

    await update_user(ctx.guild.id, user.id, 'mp', mp, 'inc')

    await ctx.channel.send(f"Foram adicionados {mp} MP(s) ao usuário {user.name}")

def setup(client):
  client.add_cog(Admin(client))
