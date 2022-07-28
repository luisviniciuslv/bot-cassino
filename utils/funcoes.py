from utils.database import update_user, user_get


async def level(guildid, userid, coins):
    xp = await user_get(guildid, userid, 'xp')
    lvl = await user_get(guildid, userid, 'lvl')
    xpmax = lvl * 20000
    xp = xp + coins 
    await update_user(guildid, userid, 'xp', xp, 'set')

    while True:
        if xp >= xpmax:
            await update_user(guildid, userid, 'lvl', 1, 'inc')
            lvl = await user_get(guildid, userid, 'lvl')
            xpmax = lvl * 20000
            xp = await user_get(guildid, userid, 'xp')
            xp = xp - xpmax
            await update_user(guildid, userid, 'xp', xp, 'set')
            if xp < 0:
                await update_user(guildid, userid, 'xp', 0, 'set')
                return
        else:
            return
