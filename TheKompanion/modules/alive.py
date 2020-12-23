from TheKompanion.helpers import command
from TheKompanion import Kompanion
from telethon import events

@Kompanion.on(command(pattern = "alive"))
async def alive(event):
    pic = "https://telegra.ph/file/b5e4873219528bda2a40a.jpg"
    msg = """
    **Powfu is on.**
    `Ready to serve...`
    """
    await event.reply(msg, file=pic)
    
@Kompanion.on(events.NewMessage(outgoing=True, pattern="^.help"))   
async def help(event):
    msg = """
        **Powfu.**
        `.alive` -> get userbot alive message.
        `.adminhelp` -> help for admin mod.
        `.stickerhelp` -> help for sticker mod.
        `.devhelp` -> help for dev mod.
        `.whois` -> get user info.
        `.weebhelp` -> help for weeb mod.
        `.ping` -> pings to tg as usual.
    """
    await event.edit(msg)
