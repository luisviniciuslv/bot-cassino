from dotenv import load_dotenv
import os
from pymongo import MongoClient
from datetime import datetime
load_dotenv()
client = MongoClient(os.getenv("database_connection"))
db = client['server']

async def findall():
    collection = db[str(933020401632677888)]
    return collection.find({})

async def createguild():
    collection = db[str(933020401632677888)]
    if not collection.find_one({'_id': 0}):
        collection.insert_one({'_id': 0, 'criptocoin': 0.1})
        print('servidor criado!')
    else:
        print('servidor já criado')

async def change_prefix(guildID : int, nPrefix : str):
  collection = db[str(guildID)]
  prefix = collection.find_one({'_id': 0})['prefix']
  if prefix == nPrefix:
    return False
  collection.update_one({'_id': 0}, {'$set': {'prefix': nPrefix}})

async def get_prefix(client, ctx):
  guildID = str(ctx.guild.id)

  if guildID in db.list_collection_names():
    collection = db[guildID]
    prefix = collection.find_one({'_id': 0})['prefix']
    return prefix
  else:
    collection = db.create_collection(guildID)
    collection.insert_one({'_id': 0, 'prefix': '!'})
    return '!'

async def create_account(guildID : int, userID : int):
    collection = db[str(guildID)]
    if not collection.find_one({'_id': userID}):
        collection.insert_one({'_id': userID, 'coins': 0, 'banco': 0, 'valor_ganho': 0, 'valor_perdido':0,'valor_apostado':0, 'empresas':[], 'Time_loot': datetime.min, 'Last_time':datetime.min, 'xp': 0, 'lvl': 0})

async def update_user(guildID : int, userID : int, field : str, val, updateType : str):
    await create_account(guildID, userID)
    collection = db[str(guildID)]

    if updateType == 'inc':
        collection.update_one({'_id': userID}, {'$inc': {field:val}})
    elif updateType == 'set':
        collection.update_one({'_id': userID}, {'$set':{field:val}})

async def user_get(guildID : int, userID : int, field : str):
    await create_account(guildID, userID)
    collection = db[str(guildID)]
    try:
        return collection.find_one({'_id': userID})[field]
    except:
        return None

async def get_guild_ranking(bot, guildId : int):
    collection = db[str(guildId)]

    def soma(user):
        aux = 0
        if 'vendinha' in user:
            aux += 1
        if 'mercado' in user:
            aux += 2
        if 'shopping' in user:
            aux += 3
        if 'fazenda' in user:
            aux += 4
        if 'concessionaria' in user:
            aux += 5
        return aux

    users = collection.find()
    users = sorted(users, key = lambda x: (soma(x['empresas'])), reverse=True)

    content = ''
    aux = 1
    
    for i in users:
        user = await bot.fetch_user(i['_id'])
        content += "**{}. {}**\nPontos de empresa: {}\n".format(aux, user.name, soma(i['empresas']))
        aux += 1
        if aux > 10: return content

    return content
