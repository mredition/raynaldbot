from userbot.utils import register

@register(outgoing=True, pattern="^.group$")

async def join(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("This is my community.\n\n[Channel](http://t.me/freeitemsinside)\n\n[Chat Group](http://t.me/freenetedition)\n\n[UserBot Tutorial]")
