import discord
from discord.ext import commands

from utils.database import change_prefix, update_user,get_prefix
class Admin(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.has_permissions(ban_members=True)
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


def setup(client):
  client.add_cog(Admin(client))
