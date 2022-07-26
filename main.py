
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix='!', case_insensitive=True)
client.remove_command('help')

for i in os.listdir('./cogs'):
  for e in os.listdir(f'./cogs/{i}'):
    if str(e).startswith('__py'):
      pass
    else:
      print('loaded ', e)
      client.load_extension(f'cogs.{i}.{e[:-3]}')

@commands.has_guild_permissions(administrator=True)
@client.command()
async def reload(ctx):
  for i in os.listdir('./cogs'):
    for e in os.listdir(f'./cogs/{i}'):
      if str(e).startswith('__py'):
        pass
      else:
        client.reload_extension(f'cogs.{i}.{e[:-3]}')
        print('loaded ', e)

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.errors.MissingRequiredArgument):
      msg = "está faltando informações, digite !help para consultar os comandos"
      await ctx.send(msg)

  if isinstance(error, commands.errors.CommandOnCooldown):
      tempo = '{:.0f}'.format(error.retry_after)
      tempo = int(tempo)

      if tempo > 60:
        tempo = tempo/60
        msg = f"Espere {str(tempo).split('.')[0]} minutos para resgatar novamente"
        await ctx.send(msg)
        return
        
      msg = "Espere {:.0f}s para resgatar novamente".format(error.retry_after)
      await ctx.send(msg)

client.run(os.getenv('bot_token'))
#perae
#KKKKKKKKKKKK NAMORADA OPRESSORA EH ISSO?
#sim lekkkkk
